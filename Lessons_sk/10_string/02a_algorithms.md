# Operácie s reťazcami – rýchly prehľad

Posledný stĺpec tabuľky obsahuje klikateľný odkaz na podrobné vysvetlenie a príklad v súbore [02_main.md](02_main.md).

| Operácia | Čo vráti / na čo slúži? | Podrobnosti v súbore 02_main.md |
|---|---|---|
| `text[i]` | znak na danom indexe | [Indexovanie a výrezy](02_main.md#co-je-retazec) |
| `text[a:b]` | časť reťazca; index `b` už nie je zahrnutý | [Indexovanie a výrezy](02_main.md#co-je-retazec) |
| `for znak in text` | prejde všetky znaky reťazca | [Prechádzanie znak po znaku](02_main.md#prechadzanie-cyklom-for-po-jednotlivych-znakoch) |
| `text.lower()` | verzia s malými písmenami | [`.lower()`](02_main.md#lower) |
| `text.upper()` | verzia s veľkými písmenami | [`.upper()`](02_main.md#upper) |
| `text.replace(old, new)` | nový reťazec s nahradením | [`.replace()`](02_main.md#replacefrom-to) |
| `text.split()` | zoznam rozdelený podľa medzier | [`.split()`](02_main.md#split) |
| `text.split(".")` | zoznam rozdelený podľa zadaného oddeľovača | [Rozdelenie podľa znaku](02_main.md#split---rozdelenie-podla-zadaneho-znaku) |
| `text.index(x)` | index prvého výskytu; ak chýba, vyvolá `ValueError` | [`.index()`](02_main.md#indexsubstring) |
| `text.count(x)` | počet výskytov | [`.count()`](02_main.md#count-substring) |
| `len(text)` | počet znakov | [`len()`](02_main.md#lentext) |
| `separator.join(parts)` | spojenie reťazcov pomocou oddeľovača | [`join()` a spájanie čísel](02_main.md#oddelovacjoinstringcollection) |
| `x in text` | `True`, ak sa `x` nachádza v reťazci | [Kontrola obsahu](02_main.md#in--kontrola-obsahu) |
| `list(text)` | zoznam jednotlivých znakov | [Reťazec ako kolekcia](02_main.md#str-ako-kolekcia) |

## Krátke príklady

```python
text = "Python jazyk"
print(text.lower())                       # python jazyk
print(text.replace("jazyk", "programovanie")) # Python programovanie
print(" ".join(["Dobrý", "deň"]))          # Dobrý deň
```

Oddeľovač metódy `join()` je reťazec, na ktorom metódu voláme. Čísla treba najprv previesť na text pomocou `str()`. Ďalšie príklady nájdeš v [podrobnej lekcii](02_main.md).
