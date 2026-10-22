🗺️ [Vissza a tananyag térképéhez](../../Lessons_hu/00_Terkep_hu.md) · [Vissza a téma áttekintéséhez](README.md)

# `input()` függvény

Adat, szöveg (karakterlánc) beolvasása, amit utána egy változóba menthetünk el.

```py
>>> szoveg = input()
alma
>>> print(szoveg)
alma
```

A Python érdekessége, hogy az `input()` utasítással üzenetet küldhetünk a felhasználónak arról, hogy milyen adatra van szükségünk.

Ezt az üzenetet az `input` zárójelébe macskakörmök közé írjuk. A program lefuttatásakor az üzenet megjelenik a képernyőn, a program pedig várni fog a kért adat megadására. Megspórolunk egy print-et!

## Példa

```py
>>> szoveg = input("Hany ora van? ")
Hany ora van? 9
>>> print(szoveg)
9
```

## `input()` – számok (egész számok)

`szam = input("Adj meg egy szamot!")`

A `szam` értéke a bevitel után: `"50"`.

Miért nem jó ez, ha számolni szeretnénk vele? Próbáljunk meg hozzáadni `12`-t a `szam` változóhoz.

### Javított kód

```py
szam = int(input("Adj meg egy szamot!"))
print(szam + 12)
```

Ha a felhasználó `50`-et ír be, a kimenet `62`. Az `int()` az egész számmá alakítást végzi.

Tizedes szám beolvasásához a `float()` használható:

```py
ar = float(input("Add meg az árat: "))
print(ar * 2)
```

Ha a felhasználó `1.5` értéket ad meg, a kimenet `3.0`.

**Fontos:** az `int(input(...))` egész számot vár. Ha betűt vagy `1.5`-öt adunk meg, a konvertálás hibát okoz. A tizedes számhoz `float(input(...))` kell.

A kérdéseket, a hibakeresést és a gyakorlófeladatokat külön fájlokban találod: [kérdések](04_questions.md), [rontsátok el](03_break_it.md), [gyakorlófeladatok](05_exercises.md).
