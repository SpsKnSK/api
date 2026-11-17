# Discord homework scheduling

Queue file: `homeworks.json` on the `homework-scheduler` branch.
The workflow and dispatcher live on `main`.

New item format:
```json
[
  {
    "id": "hu-2026-11-18-stringek",
    "language": "HU",
    "send_at": "2026-11-18T12:00:00+01:00",
    "status": "pending",
    "message": "@everyone Szerbusztok, a házi feladat..."
  },
  {
    "id": "sk-2026-11-19-stringy",
    "language": "SK",
    "send_at": "2026-11-19T14:00:00+01:00",
    "status": "pending",
    "message": "@everyone Ahojte, domáca úloha..."
  }
]
```

This example is documentation only; the live queue is empty until a homework item is added.

- `id`: unique per homework item.
- `language`: `HU` or `SK`.
- `send_at`: ISO 8601 with explicit UTC offset. Winter in Slovakia/Hungary: `+01:00`; summer: `+02:00`.
- `status`: use `pending` for new items. After delivery, the script sets `sent`.
- `message`: Discord Markdown (max 2000 characters).
- Repository Actions secrets: `DISCORD_WEBHOOK_URL_HU` and `DISCORD_WEBHOOK_URL_SK`; never add their values to the repository.

The workflow checks every five minutes, but GitHub may delay scheduled jobs. Due items are sent in scheduled-time order and marked sent afterward. GitHub Actions must have permission to push changes to `homework-scheduler`. If delivery succeeds but the Git push fails, a retry could send a duplicate; don't claim exactly-once delivery. Test with an ordinary message first.
