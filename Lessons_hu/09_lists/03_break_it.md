🗺️ [Vissza a tananyag térképéhez](../../Lessons_hu/00_Terkep_hu.md) · [Részletes tananyag](02_main.md)

# 💥 Rontsátok el!

Másold ki a programot, futtasd le, majd javítsd ki úgy, hogy a `rendezett` lista `[1, 2, 3]` legyen.

```python
szamok = [3, 1, 2]

rendezett = sorted(szamok)
print("Eredeti:", szamok)
print("Rendezett:", rendezett)

szamok.sort()
print("Helyben rendezve:", szamok)
```

## Hibakeresési feladat

1. Először töröld a `rendezett =` részt, és futtasd a `sorted(szamok)` sort önmagában. Miért marad változatlan az eredeti lista?
2. Próbáld ki a `szamok.sort()` utasítást. Mi változik meg?
3. Nevezd át a `szamok` változót `Szamok` névre csak az egyik sorban. Milyen hibát kapsz, és miért?
4. Állítsd át a listát üres listára (`szamok = []`). Mit adna vissza a `len(szamok)`? Mi történne a `min(szamok)` hívásakor?

Ne csak javítsd a kódot: minden változtatás előtt próbáld meg megjósolni a kimenetet.
