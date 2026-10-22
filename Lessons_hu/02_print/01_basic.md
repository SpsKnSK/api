🗺️ [Vissza a tananyag térképéhez](../../Lessons_hu/00_Terkep_hu.md) · [Részletesebb tananyag](02_main.md)

# 02 – Kiíratás: `print()`

## Mit fogok megtanulni?

Megtanulom, hogyan írhatok ki szöveget, számot, változót és műveleti eredményt a képernyőre, valamint hogyan befolyásolhatom a kiírás formáját.

## Rövid példa

```python
nev = "Anna"
print("Szia", nev)
print(1 + 1)
print("Szia", "világ", sep="-")
```

**Kimenet:**

```text
Szia Anna
2
Szia-világ
```

- A szöveget idézőjelek közé írjuk, a számot nem.
- A változó neve helyett a változó értéke jelenik meg.
- A vesszővel több értéket adhatunk meg egy `print()` hívásban; alapértelmezés szerint szóköz kerül közéjük.
- A `sep` az értékek közötti elválasztót, az `end` a sor végére kerülő szöveget határozza meg.
- A `\n` új sort, a `\t` tabulátort jelöl. A `#` utáni rész megjegyzés.

A részletes magyarázatokat és további példákat a [részletes tananyagban](02_main.md), a feladatokat a [gyakorlófeladatok között](05_exercises.md) találod.
