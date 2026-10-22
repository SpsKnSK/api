# ✏️ Cykly - `for`

Cyklus `for` používame vtedy, keď vopred vieme, na akých hodnotách alebo koľkokrát opakujeme.

```py
for i in range(1, 6):
    print(i)
```

Výstup: `1`, `2`, `3`, `4`, `5`

**Najdôležitejšie tvary `range()`:**

| Kód | Vypísané hodnoty |
|---|---|
| `range(5)` | `0, 1, 2, 3, 4` |
| `range(2, 5)` | `2, 3, 4` |
| `range(1, 10, 2)` | `1, 3, 5, 7, 9` |

Horná hranica **nepatrí** do intervalu. Jadro cyklu je aj tu odsadený blok.

**Metafora:** `for` je ako **čítanie zoznamu mien**: vopred vieš, kto je na zozname, a postupne ich všetkých prejdeš — nemusíš si sám počítať, koľkokrát máš opakovať.