# `input()` függvény

Adat (karakterlánc) beolvasása és elmentése egy változóba.
```py
>>> szoveg = input()
alma
>>> print(szoveg)
alma
```

A Python érdekessége, hogy az `input()` utasítással üzenetet küldhetünk a felhasználónak arról, hogy milyen adatra van szükségünk.
Ezt az üzenetet az `input` zárójelébe macskakörmök közé írjuk.
A program lefuttatásakor az üzenet megjelenik a képernyőn, a program pedig várni fog a kért adat megadására. Megspórolunk egy print-et!
## Példa 

```py
>>> szoveg = input("Hány óra van?")
hány óra van?9
>>> print(szoveg)
9
```

## `input()` – számok(integer) 
`szam=input("Adj meg egy szamot!")`

`szam` értéke a bevitel után: `"50"`

Miért nem jó ez?
Próbáljunk meg hozzáadni `12`-t a szam változóhoz.

### Javított kód:
`szam=int(input("Adj meg egy szamot!"))`

Mi változott? 
Mit takar az `int` szócska?

Próbáljunk meg most hozzáadni 12-t a szam változóhoz.

## Feladatok
1. Írjatok programot, amely megkérdezi, hogy hogy hívnak. Miután megadtuk nevünket, kérdezze meg, hány évesek vagyunk, majd írjon ki egy összegző mondatot, hogy ki ül a gép előtt. `Szia [evszam] eves [nev], latom, te ulsz a gep elott`
1. Írjatok programot, amely a bekért adatokból összeállít egy névjegykártyát és kiírja a képernyőre.
Adataink: Név, Lakhely, Elérhetőség
1. Kérjünk be három természetes számot, ezek rendre 5, 2 és 1 eurósaink számát jelentik. Határozzuk meg, és írassuk ki a teljes összeget.
példa:
```
5 eurosok szama: 2
2 eurosok szama: 3
1 eurosok szama: 1
Ez osszesen 17 euro.
```
# Kerekítés
- `round` függvénnyel
- `round(a, x)`
- `a` – szám
- `x` - tizedes helyek száma

Pl. `round(12.345, 2)` eredménye `12.35`
A szám helyére változó is írható!
## Feladatok
1. Írjatok programot, amely bekér két számot, majd kiírja a hányadosukat 3 tizedes helyre.
Ezután írassátok ki az egész részre való osztás eredményét és a maradékot.
Ügyeljetek rá, hogy a program laikus felhasználók számára is használható legyen (a program írjon egy-két szót is, ne csak a konkrét eredményeket).
1. Írjunk programot a kör kerületének és területének kiszámítására.
Adatok, amiket megadunk: kör átmérője, Pí értéke: `3.14159`.
Végeredmény:
`Az X cm átmérőjű körnek Y cm a kerülete és Z négyzetcm a területe.`
1. Írjatok programot, amely kiírja a kis szorzótáblát a beadott számra (1-től 10-ig).
    ```
    Melyik szorzótáblát írjam ki? 11
    1*11=11
    2*11=22
    3*11=33
    ...
    10*11=110
    ```
1. Gyümölcsöt vásárolunk a sarki kisboltban.
    - Az alma kilója 0.65€
    - A citrom 1.2€ 
    - A narancs 1.5€
    
    Írjatok programot, amely megmondja, mennyi pénzt vigyünk magunkkal, ha 1 kg almát, 1,5 kg citromot és 2 kg narancsot veszünk.
    Próbáljunk ki más értékeket is.
    Pl. mindenből 3 kilót, 5 kilót veszünk, stb.

## Kérdések
1. Mire szolgál a `round` függvény, írjatok rá példát.
1. Írjatok kódot, amelyik megkérdezi a felhaználótól, hogy hívják és hány éves, majd írjátok ki a képernyőre, hogy 10 év múlva hány éves lesz. `Szia [nev], most 16 éves vagy, 10 év múlva 26 leszel`
1. Milyen adattípust olvas be az `input` függvény a billentyűzetről?
