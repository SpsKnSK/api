🗺️ [Vissza a tananyag térképéhez](../../Lessons_hu/00_Terkep_hu.md)

# Ciklusok és a `while`

## Mi a ciklus?

A ciklus olyan programszerkezet, amely egy utasításblokkot ismétel. Például: „amíg van pénzed, lépj egy mezőt”. Minden kör után újra ellenőrizzük a feltételt.

```mermaid
flowchart TD
    A([Start]) --> B{Igaz a feltétel?}
    B -- igen --> C["Ciklusmag: utasítások végrehajtása"]
    C --> B
    B -- nem --> D([A ciklus utáni programrész])
```

## A `while` és az `if`

Mindkettő feltételt vizsgál, de az `if` blokkja legfeljebb egyszer fut le, a `while` blokkja pedig ismétlődik, amíg a feltétel igaz.

```python
if elet > 0:
    print("A játék folytatódik.")

while elet > 0:
    print("Új kör kezdődik.")
```

## A `while` szintaxisa

```python
while feltetel:
    utasitas_1
    utasitas_2
```

A behúzott utasítások alkotják a **ciklusmagot**. A ciklusmag végén a program visszatér a `while` sorhoz, és újra ellenőrzi a feltételt.

## Számlálás

```python
i = 1
while i <= 5:
    print(i)
    i = i + 1
print("Vége")
```

A kimenet 1-től 5-ig a számok, majd „Vége”. Az `i = i + 1` módosítja a feltételben szereplő változót. Amikor `i` értéke 6 lesz, az `i <= 5` hamis, ezért a ciklus befejeződik.

## Végtelen ciklus

```python
i = 1
while i <= 5:
    print(i)
```

Ez a program nem áll le magától, mert `i` értéke nem változik, így a feltétel mindig igaz marad. Futó programot a terminálban a **Ctrl + C** billentyűkkel állíthatsz le.

## `break` és `continue`

- A `break` azonnal kilép a ciklusból.
- A `continue` kihagyja az aktuális kör hátralévő részét, majd újra ellenőrzi a feltételt.

```python
i = 0
while i < 5:
    i = i + 1
    if i == 3:
        continue
    print(i)
```

Kimenet: `1, 2, 4, 5` – a 3-at kihagyjuk.
