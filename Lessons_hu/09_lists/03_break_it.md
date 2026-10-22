🗺️ [Vissza a tananyag térképéhez](../../Lessons_hu/00_Terkep_hu.md) · [Részletes tananyag](02_main.md)

# 💥 Rontsátok el!

Másold ki a programot, futtasd le, majd javítsd ki úgy, hogy a kimenet a rendezett lista legyen: `[1, 2, 3]`.

```python
szamok = [3, 1, 2]

sorted(szamok)
print(szamok)
```

Miért nem változik meg a `szamok` lista? A `sorted()` függvény új listát ad vissza, de a program nem használja fel az eredményt.

## Hibakeresési feladat

1. Javítsd ki a programot úgy, hogy a rendezett lista kerüljön a `szamok` változóba.
2. Próbáld ki a `szamok.sort()` utasítást. Mi változik meg, és miért?
3. Nevezd át a `szamok` változót `Szamok` névre csak az egyik sorban. Milyen hibát kapsz, és miért?
4. Állítsd át a listát üres listára (`szamok = []`). Mit ad vissza a `len(szamok)`? Mi történik a `min(szamok)` hívásakor?

Ne csak javítsd a kódot: minden változtatás előtt próbáld meg megjósolni a kimenetet.
