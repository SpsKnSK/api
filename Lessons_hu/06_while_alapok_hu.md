🗺️ [Vissza a tananyag térképéhez](00_Terkep_hu.md) · [Részletesebb tananyag: while ciklus](06_while_hu.md)

# 06 – Ciklus: while – alapok

## Mit fogok megtanulni?

A lecke végére képes leszek a `while` ciklussal megismételni egy utasítást addig, amíg egy feltétel igaz. Meg fogom érteni, miért kell a ciklusban gyakran megváltoztatni egy változó értékét.

## Miért van erre szükségem?

Képzeld el, hogy egy játékban addig lépsz tovább, amíg van még életed. Nem tudod előre, pontosan hány lépésre lesz szükség. A programnak minden kör után újra ellenőriznie kell: van még életed?

Ilyen helyzetekben hasznos a `while`: **amíg a feltétel igaz, ismétel**.

## Nézzünk meg egy rövid példát!

```python
lepes = 1

while lepes <= 3:
    print(lepes)
    lepes = lepes + 1

print("Vége!")
```

**Kimenet:**

```text
1
2
3
Vége!
```

### Soronként

- **`lepes = 1`**: elindítjuk a számlálást 1-ről.
- **`while lepes <= 3:`**: a program ellenőrzi, hogy a `lepes` értéke legfeljebb 3-e.
- **`print(lepes)`**: kiírja az aktuális értéket.
- **`lepes = lepes + 1`**: növeli a változót eggyel, így közelebb kerülünk a befejezéshez.
- **`print("Vége!")`**: ez már a cikluson kívül van, ezért csak akkor fut le, amikor a ciklus befejeződött.

**Figyeld meg:**
- A `while` sor végén kettőspont (`:`) áll.
- A ciklusmag sorai beljebb kezdődnek: ezt nevezzük **behúzásnak**.
- Ha a feltétel soha nem válik hamissá, a ciklus nem áll le magától.

## Futtatás előtt tippelj!

Még ne futtasd le a programot. Írd le, mit fog kiírni, és hányszor fut le a `print` sor.

```python
szam = 2

while szam < 6:
    print(szam)
    szam = szam + 2
```

1. Milyen számokat ír ki a program, és milyen sorrendben?
2. Mi lesz a `szam` értéke az utolsó kör után?
3. Mi történne, ha a `szam = szam + 2` sort kitörölnénk?

Most futtasd le, és ellenőrizd a tippedet.

## Próbáld ki önállóan!

### 1. Vezetett feladat

Egészítsd ki a hiányzó részeket úgy, hogy a program 1-től 5-ig írja ki a számokat.

```python
szam = 1

while szam <= _____:
    print(szam)
    szam = szam + _____
```

### 2. Önálló feladat

Írd ki a számokat 5-től 1-ig visszafelé, majd a ciklus után jelenjen meg a `Kész!` üzenet.

### 3. Önálló feladat

Kérj be egy jelszót. Amíg a felhasználó nem a `python123` szót írja be, kérd be újra. Ha helyes a jelszó, írd ki: `Sikeres belépés!`

*Segítség: az `input()` eredményét egy változóban tárold, és a cikluson belül kérdezd be újra.*

### ⭐ Opcionális kihívás

Készíts számkitalálós játékot: a titkos szám legyen 7. A program addig kérjen új tippet, amíg a felhasználó el nem találja. Találatkor írja ki: `Eltaláltad!`

További gyakorlófeladatok: [while – feladatok](../Exercies/06_while/exercises_hu.md).

## Ellenőrizd, érted-e!

Próbálj válaszolni az alábbi kérdésekre a példa megnézése nélkül.

1. Mit jelent az, hogy a `while` „amíg” ismétel?
2. Miért fontos, hogy a ciklusban változzon a megfelelő változó?
3. Hol kezdődik a ciklusmag?

**Mini feladat:** Mit ír ki ez a program?

```python
i = 1

while i < 4:
    print("Szia")
    i = i + 1
```

Hányszor jelenik meg a `Szia`?

## 💥 Rontsátok el!

### Kiinduló kód: számlálás

Másoljátok ki a programot, futtassátok le, majd változtassatok meg benne valamit úgy, hogy hibát vagy váratlan működést okozzatok. Először próbáljátok megjósolni, mi fog történni!

```python
i = 0

while i < 3:
    print(i)
    i = i + 1
```

Ötletek:
- Töröljétek ki az `i = i + 1` sort. Miért nem áll le a program? Ha végtelenül fut, állítsátok le a terminálban a `Ctrl + C` billentyűkkel.
- Változtassátok meg a feltételt `i < 3` helyett `i < 0` alakra. Mi történik?
- Tegyétek a számláló növelését a `print(i)` elé. Hogyan változik a kimenet?
- Próbáljátok elrontani a kettőspontot vagy a behúzást.

Beszéljétek meg:
- Melyik változtatás okozott hibaüzenetet?
- Melyiknél futott a program, de mást csinált, mint vártátok?
- Hogyan javítottátok ki?
