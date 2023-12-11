# Ciklusok bevezető 
A Python programozási nyelvben kétféle ciklusttípust különböztetünk meg:
- számolt `for`, előre tudjuk, hányszor fog lefutni, az ismétlések száma adott
- számolatlan `while`, előre nem tudjuk meghatározni, hányszor fog lefutni, addig fut, míg a feltétel teljesül
## Ciklus
Parancs, amely lehetővé teszik, hogy egy utasítás többször fusson le.
> A ciklusok módosítják a program lefutási irányát, mivel visszaugrunk a ciklus elejére.
## Ciklusmag
A ciklusban lefutó utasítások halmaza.
## Ciklusváltozó (for ciklus)
a ciklus segédváltozója, amely a ciklus minden egyes lefutásakor megváltoztatja az értékét.
Növekszik/csökken egyel/kettővel/tízzel/…

# Intervallumok
Kétfajta intervallumot különböztetünk meg:
- nyitott (0; 5), ahol a két szélső érték **nem** tartozik bele: 1, 2, 3, 4
- zárt <0; 5>, ahol a két szélső érték **bele**tartozik: 0, 1, 2, 3, 4, 5

# `for` ciklus
Számolt ciklus, előre tudjuk, hányszor fog lefutni. Felhasználása:
- valamit x-szer kell végrehajtanunk
- tömb elemeit kell végigjárnunk
## Szintaxis, szabálykészlet, leírás
```py
for [ciklusvaltozo] in range(x,y):
    if feltetel1:   #ciklusmag
        continue    #ciklusmag
    utasitas        #ciklusmag
    utasitas        #ciklusmag
    utasitas        #ciklusmag
    if feltetel2:   #ciklusmag
        break       #ciklusmag
else:
    utasitas
```
## Értelmezés
- a ciklusmagot tabulátorral vagy szóközzel válasszuk külön a `for` parancstól (ajánlom a tabot), így tudja a fordító, hogy éppen a ciklusmagban van.
- Az `x` és `y` változók a tartomány elejét és végét jelölik, pl. <1;10)
- A `ciklusvaltozo`t, ha egész szám, általában `i`vel jelöljük, értéket pedig a `range` által határolt intervallumban vesz fel
- Ahogy az `if`nél a `for` ciklusnál is van lehetőség `else` ágat létrehozni (_Python nyelv különlegessége_), akkor kerül lefutásra, ha a ciklusmagot **nem** szakítottuk meg `break` paranccsal
- A `continue` utáni utasítások nem futnak le,a ciklus veszi a következő értéket, amin le kell futtatni a ciklusmagot (de figyelem, ebben az esetben feltételhez kötött)
- A `break` befejezi a ciklusmag futtatását, és a ciklus utáni parancsot hajtja végre (de figyelem, ebben az esetben feltételhez kötött)

### Példák
```py
for i in range(0,3):
    print(x)
```
```py
a = 10
for i in range(1, 5):
    print(a+i)
```
# For ciklus tulajdonságai
A for ciklus mindig egy tartományon, intervallumon belül fut, amely egyértelműen behatárolható. Nem mindig szükséges a `range()` függvény, mivel ilyen behatárolható tartomány egy `string` is lehet.

```py
text = "alma"
for c in text: # c mint character
    print(c)
```
## Feladat
Készítsetek egy programot, amely 1-től 15-ig kiírja az összes egész számot és mellé a szám négyzetét is.
```
1 1
2 4
3 9
...
14 196
15 225
```
## Feladat
Írjatok programot, amely az általatok megadott tartományból kiírja az összes:
- 2-vel és 4-gyel egyidejűleg osztható számot.
- 5-tel osztható számot.
- 35-nél nagyobb számokat.
> Tehetitek egy `for` ciklusba is vagy 3 külön ciklust csináltok
## Feladat 
Határozzátok meg és írassátok ki az összes hárommal és öttel egyaránt osztható, 1000-nél kisebb természetes számot.
## Feladat
Kérjünk be **N** darab természetes számot (először **N**-t kérjük be). Az adatok beírása után a program írja ki:
- a páros számok darabszámát
- a páratlan számok darabszámát
- a páratlan számok összegét!

# `range()`
```py
class range(
    __start: SupportsIndex,
    __stop: SupportsIndex,
    __step: SupportsIndex = ...,
    /
)
```
- `__start` az intervallum alsó határa, zárt
- `__stop`  az intervallum felső határa, nyitott
- `__step`  lépés

```py
for i in range(0,10,3):
    print(x)
```

- `range(5, 10)`: 5, 6, 7, 8, 9
- `range(0, 10, 3)`: 0, 3, 6, 9 
- `range(-10, -100, -30)`:  -10, -40, -70

## Feladat
- Írassátok ki a 3-mal osztható számokat 100-ig.
- Írassátok ki a 7-tel osztható számokat 50 és 99 közt.
- Számoljatok vissza 50-től 20-ig 4-esével és írassátok ki az egyes számokat!

# Kérdések
1. Mi a különbség a nyitott és a zárt intervallum között? 
1. Milyen értékek tartoznak bele a következő intervallumokba: <1; 6), <-2;1>, (6;3)?
1. Milyen típusú ciklusokat ismertek? Vázoljátok a különbségeket.
1. Mennyi parancs lehet a ciklusmagban? 
1. Írjátok fel a `for` ciklus szintaxisát.
1. `for` ciklus segítségével írjátok ki a szorzótáblát, amelyiket a felhasználó határozza meg.
1. Számoljatok vissza 20tól 0ig `for` ciklussal, és írassátok ki a képernyőre minden 4. számot.
1. Mi a különbség a `break` és a `continue` parancsok között?
1. Hány `else` ága lehet a `for` ciklusnak? 
1. Kell-e mindig `else` ág?
1. Mikor fut le az `else` ág?
1. Működik a `for` ciklus `break` nélkül?
1. Működik a `for` ciklus `continue` nélkül?
1. Mire szolgál a `range()` függvény? Soroljátok fel a paramétereit.
1. Mit ír ki a képernyőre az alábbi program?
    ```py
    for i in range(2, 10, 3):
        print(i, end=" ")
    ```
1. Mit ír ki a képernyőre az alábbi program?
    ```py
    for i in range(0,10):
        break
        print(i)
    else:
        print("Else")
    print("Szep napot!")
    ```
1. Mit ír ki a képernyőre az alábbi program?
    ```py
    for i in range(0,10):
        continue
        print(i)
    else:
        print("Else")
    print("Szep napot!")
    ```