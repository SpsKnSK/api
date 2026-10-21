## ✏️ Do zošita – Cyklus: for

**Na čo slúži?** Cyklus `for` používame vtedy, keď vopred vieme, na akých hodnotách alebo koľkokrát opakujeme.

```python
for i in range(1, 6):
    print(i)
```

**Výstup:** `1, 2, 3, 4, 5`

**Najdôležitejšie tvary `range()`:**

| Kód | Hodnoty |
|---|---|
| `range(5)` | `0, 1, 2, 3, 4` |
| `range(2, 5)` | `2, 3, 4` |
| `range(1, 10, 2)` | `1, 3, 5, 7, 9` |

Horná hranica **nepatrí** do postupnosti. Telo cyklu je odsadený blok.

**Počítanie odzadu:**

```python
for i in range(10, 0, -2):
    print(i)
```

Výstup: `10, 8, 6, 4, 2`
