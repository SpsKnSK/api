🗺️ [Vissza a tananyag térképéhez](../../Lessons_hu/00_Terkep_hu.md) · [Részletesebb tananyag](02_main.md)

# 06 – Ciklus: while – alapok

## Mit fogok megtanulni?

A `while` ciklussal megismételni utasításokat addig, amíg egy feltétel igaz. Megértem, miért kell a ciklusban gyakran megváltoztatni egy változó értékét.

## Miért van erre szükségem?

Képzeld el, hogy egy játékban addig lépsz tovább, amíg van még életed. Nem tudod előre, pontosan hány lépésre lesz szükség. A programnak minden kör után újra ellenőriznie kell: van még életed?

## Rövid példa

```python
lepes = 1
while lepes <= 3:
    print(lepes)
    lepes = lepes + 1
print("Vége!")
```

Kimenet:
```text
1
2
3
Vége!
```

- `lepes = 1`: elindítjuk a számlálást.
- `while lepes <= 3:`: ellenőrizzük a feltételt.
- `print(lepes)`: kiírjuk az aktuális értéket.
- `lepes = lepes + 1`: növeljük a változót, így a ciklus egyszer befejeződik.
- A ciklus utáni `print` csak a ciklus befejezése után fut le.

A `while` sor végén kettőspont áll, a ciklusmag behúzott. Ha a feltétel soha nem válik hamissá, a ciklus nem áll le magától.

## Futtatás előtt tippelj!

```python
szam = 2
while szam < 6:
    print(szam)
    szam = szam + 2
```

1. Milyen számokat ír ki?
2. Mi lesz a `szam` értéke az utolsó kör után?
3. Mi történne, ha törölnénk a növelést?

## Próbáld ki önállóan!

1. Egészítsd ki a kódot, hogy 1-től 5-ig írja ki a számokat:
   ```python
   szam = 1
   while szam <= _____:
       print(szam)
       szam = szam + _____
   ```
2. Írd ki a számokat 5-től 1-ig visszafelé, majd a ciklus után jelenjen meg a `Kész!` üzenet.
3. Kérj be egy jelszót addig, amíg a felhasználó a `python123` szót nem írja be. Helyes jelszónál írd ki: `Sikeres belépés!`

⭐ **Kihívás:** Készíts számkitalálós játékot, amely addig kér tippet, amíg a felhasználó el nem találja a 7-es számot.

További feladatok: [while – gyakorlófeladatok](05_exercises.md).

## Ellenőrizd, érted-e!

1. Mit jelent az, hogy a `while` „amíg” ismétel?
2. Miért fontos, hogy a ciklusban változzon egy megfelelő változó?
3. Hol kezdődik a ciklusmag?

Mit ír ki a program, és hányszor jelenik meg a „Szia”?

```python
i = 1
while i < 4:
    print("Szia")
    i = i + 1
```
