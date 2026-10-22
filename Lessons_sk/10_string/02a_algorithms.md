# Operácie s reťazcami – rýchly prehľad

| Operácia | Čo vráti / na čo slúži? |
|---|---|
| `text[i]` | znak na danom indexe |
| `text[a:b]` | časť reťazca; index `b` už nie je zahrnutý |
| `text.lower()` | verzia s malými písmenami |
| `text.upper()` | verzia s veľkými písmenami |
| `text.replace(old, new)` | nový reťazec s nahradením |
| `text.split()` | zoznam rozdelený podľa medzier |
| `text.split(".")` | zoznam rozdelený podľa zadaného oddeľovača |
| `text.index(x)` | index prvého výskytu; ak chýba, vyvolá `ValueError` |
| `text.count(x)` | počet výskytov |
| `len(text)` | počet znakov |
| `separator.join(parts)` | spojenie reťazcov pomocou oddeľovača |
| `x in text` | `True`, ak sa `x` nachádza v reťazci |
| `list(text)` | zoznam jednotlivých znakov |

## Krátke príklady

```python
text = "Python jazyk"
print(text.lower())                       # python jazyk
print(text.replace("jazyk", "programovanie")) # Python programovanie
print(" ".join(["Dobrý", "deň"]))          # Dobrý deň
```

Oddeľovač metódy `join()` je reťazec, na ktorom metódu voláme. Čísla treba najprv previesť na text pomocou `str()`. Podrobné príklady sú v [02 – Podrobnej lekcii](02_main.md).
