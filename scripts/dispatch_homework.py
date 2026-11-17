#!/usr/bin/env python3
"""Send due HU/SK homework through Discord webhooks.

The queue lives on the homework-scheduler branch, separately from this script.
All send_at values must include an explicit UTC offset (e.g. +01:00).
"""
import json
import os
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


def run_git(directory: Path, *args: str) -> None:
    subprocess.run(["git", "-C", str(directory), *args], check=True)


def parse_time(value: str) -> datetime:
    scheduled = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if scheduled.tzinfo is None or scheduled.utcoffset() is None:
        raise ValueError("send_at must contain a timezone offset")
    return scheduled.astimezone(timezone.utc)


def send_discord(webhook_url: str, message: str) -> str | None:
    if not 1 <= len(message) <= 2000:
        raise ValueError("Discord messages must be between 1 and 2000 characters")

    separator = "&" if "?" in webhook_url else "?"
    url = f"{webhook_url}{separator}wait=true"
    payload = json.dumps({
        "content": message,
        "allowed_mentions": {"parse": ["everyone"]},
    }, ensure_ascii=False).encode("utf-8")

    for attempt in range(4):
        request = Request(
            url,
            data=payload,
            headers={"Content-Type": "application/json", "User-Agent": "SpsKnSK-homework-scheduler/1.0"},
            method="POST",
        )
        try:
            with urlopen(request, timeout=25) as response:
                raw = response.read()
                result = json.loads(raw) if raw else {}
                return str(result["id"]) if "id" in result else None
        except HTTPError as error:
            if error.code == 429 and attempt < 3:
                try:
                    delay = min(30.0, max(1.0, float(error.headers.get("Retry-After", "2"))))
                except (TypeError, ValueError):
                    delay = 2.0
                time.sleep(delay)
                continue
            raise RuntimeError(f"Discord returned HTTP {error.code}; no queue update was made") from None
        except (URLError, TimeoutError):
            raise RuntimeError("Cannot confirm Discord delivery; no queue update was made") from None

    raise RuntimeError("Discord rate limit retries exhausted")


def persist(queue_file: Path, items: list, homework_id: str) -> None:
    queue_file.write_text(
        json.dumps(items, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    repo_dir = queue_file.parent
    run_git(repo_dir, "config", "user.name", "github-actions[bot]")
    run_git(repo_dir, "config", "user.email", "41898282+github-actions[bot]@users.noreply.github.com")
    run_git(repo_dir, "add", queue_file.name)
    run_git(repo_dir, "commit", "-m", f"Mark homework {homework_id} as sent")
    run_git(repo_dir, "push", "origin", "HEAD:homework-scheduler")


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("Usage: dispatch_homework.py <path/to/homeworks.json>")
    queue_file = Path(sys.argv[1]).resolve()
    items = json.loads(queue_file.read_text(encoding="utf-8"))
    if not isinstance(items, list):
        raise ValueError("homeworks.json must be a JSON array")

    now = datetime.now(timezone.utc)
    due = []
    seen_ids = set()
    for item in items:
        if not isinstance(item, dict):
            raise ValueError("Every homework must be a JSON object")
        homework_id = str(item.get("id", ""))
        if not homework_id or homework_id in seen_ids:
            raise ValueError("Every homework must have a unique nonempty id")
        seen_ids.add(homework_id)
        if item.get("status") != "pending":
            continue
        planned = parse_time(str(item["send_at"]))
        if planned <= now:
            due.append((planned, item))

    if not due:
        print("No homework due.")
        return

    for _, item in sorted(due, key=lambda pair: pair[0]):
        language = str(item.get("language", "")).upper()
        if language not in ("HU", "SK"):
            raise ValueError(f"Invalid language for homework {item['id']}: {language}")
        webhook = os.environ.get(f"DISCORD_WEBHOOK_URL_{language}", "")
        if not webhook.startswith("https://"):
            raise RuntimeError(f"Missing DISCORD_WEBHOOK_URL_{language} secret")

        message = item.get("message")
        if not isinstance(message, str):
            raise ValueError(f"Homework {item['id']} has no text message")

        discord_id = send_discord(webhook, message)
        item["status"] = "sent"
        item["sent_at"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
        if discord_id:
            item["discord_message_id"] = discord_id

        persist(queue_file, items, str(item["id"]))
        print(f"Sent homework {item['id']} to {language} Discord channel.")


if __name__ == "__main__":
    main()
