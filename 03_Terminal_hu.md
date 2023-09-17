# Print() és Input() utasítások
## print()
- Adatok, információk kiíratása a képernyőre
- Kiírathatunk:
    - Szöveget
    - Számokat
    - Változó tartalmát
    - Több változóval elvégzett matematikai műveletek eredményét

### Feladat
1. Szöveg kiíratása (mi a különség?):
    ```py
    print("Hello World")
    print('Hello World')
    ```
1. Szám kiíratása (mi a különség?):
    ```py
    print(123.45)
    print(12, 45)
    ```
1. Változó kiíratása
    ```py
    szam1=5
    szam2=11
    print(szam1)
    ```
1. Összeg kiíratása
    ```py
    szam1=5
    szam2=11
    print(szam1+szam2)
    ```

## `print()` – vegyes kiíratás
Lehetőség van egy print-en belül több adat kiíratására.

Ezeket az adatokat vesszővel választjuk el egymástól

```py
darab = 12
print(darab, "gitárhúr")
```
Lehetőségünk van műveleteket végrehajtani a printen belül több féle típusú adattal.

```py
szam1 = 12
szam2 = 8
print(szam1+szam2, szam1*szam2)
```
Szöveg - tehát string – esetében a következő a helyzet.
```py
print('egy csomag', 'gitar'+'hur')
```
### Egymás mellé vs. egymás alá
Egymás mellé írt szöveg esetén 1 printet használunk, és mindent a zárójelébe írunk.
```py
print('Szia', 'Peti!')
```
Egymás alá írt szöveg esetében minden sorra egy-egy printet használunk.
```py
print('Szia')
print('Peti!')
```
vagy az újsor karaktert `\n`
```py
print('Szia\nPeti!')
```
## Gyakorlat
Adott 3 változó a következő értékekkel:
```py
elso=12
masodik=24
harmadik=34
```
1. Írassátok ki ezt a három számot a képernyőre a köv. formában: 
```
Elso szam: 12
Masodik szám: 24
Harmadik szám: 34
```
2. Írassátok ki a három szám összegét és az első két szám szorzatát.

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

Próbáljunk meg most hozzáadni 12-t a Szam változóhoz.

## Kód írása
- Új szkript létrehozása
- Megírt szkript mentése
    - Midnenki a saját nevéhez tartozó könyvtárba!
    - Gyakori mentés (Ctrl+S), nem csak ha teljesen kész a program!!!
- Szkript futtatása (F5, vagy a Fájl menüből)

## Feladatok
1. Írjatok programot, amely megkérdezi, hogy hogy hívnak. Miután megadtuk nevünket, kérdezze meg, hány évesek vagyunk, majd írjon ki egy összegző mondatot, hogy ki ül a gép előtt.
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
