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

## 💥 Rontsátok el!

Futtassátok ezt a programot. Miért nem áll le?

```python
i = 0
while i < 3:
    print(i)
```

Javítsátok úgy, hogy 0, 1, 2 jelenjen meg, majd a program leálljon. Utána tegyétek a növelést a `print(i)` elé. Hogyan változik a kimenet?

## 📋 Feladatok

1. Kérj be egy számot, majd írd ki az 1-től a megadott számig terjedő egész számokat.
2. Számolj vissza 100-tól 0-ig, majd írd ki: „Boldog új évet!”
3. Kérj be számokat egymás után, amíg a felhasználó 0-t nem ad meg, majd írd ki az összegüket.
4. Írd ki a 3-mal osztható számokat 50-ig.

## ❓ Kérdések

1. Milyen hétköznapi helyzetet tudsz mondani, amikor valamit „amíg” ismétlünk?
2. Mi a különbség az `if` és a `while` között?
3. Mi a ciklusmag, és hogyan jelöli a Python?
4. Miért kell a `while` feltételének egyszer hamissá válnia?
5. Mit ír ki a következő program?
   ```python
   i = 2
   while i < 8:
       print(i, end=" ")
       i = i + 2
   ```
6. Mire való a `break`, és mire a `continue`?

További gyakorlás: [while – feladatok](05_exercises.md).
