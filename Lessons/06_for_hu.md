# Ciklusok bevezető és `for`
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

## Szintaxis, szabálykészlet, leírás
```py
for [ciklusvaltozo] in range(x,y):
    if feltetel1:
        continue
    utasitas #ciklusmag
    utasitas #ciklusmag
    utasitas #ciklusmag
    if feltetel2:
        break
else:
    utasitas
```
## Értelmezés
- Az `x` és `y` változók a tartomány elejét és végét jelölik, pl. <1;10)
- A `ciklusvaltozo`t, ha egész szám, általában `i`vel jelöljük, értéket pedig a `range` által határolt intervallumban vesz fel
- Ahogy az `if`nél a `for` ciklusnál is van lehetőség `else` ágat létrehozni (Python nyelv különlegessége), akkor kerül lefutásra, ha a ciklusmagot **nem** szakítottuk meg `break` paranccsal
- A `continue` utáni utasítások nem futnak le (de figyelem, ebben az esetben feltételhez kötött)
- A `break` befejezi a ciklusmag futtatását, és a ciklus utáni parancsot hajtja végre
### `range()`
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
```py
for i in range(0,10,3):
    print(x)
```
# For ciklus tulajdonságai
A for ciklus mindig egy tartományon, intervallumon belül fut, amely egyértelműen behatárolható. Nem mindig szükséges a `range()` függvény, mivel ilyen behatárolható tartomány egy `string` is lehet.

```py
text = "apple"
for c in text: # c mint character
    print(c)
```
## Feladat
Készítsetek egy programot, amely 1-től 15-ig kiírja az összes egész számot és mellé a szám négyzetét is.


# Kérdések
1. Mi a különbség a nyitott és a zárt intervallum között? 
1. Milyen értékek tartoznak bele a következő intervallumokba: <1; 6), <-2;1>, (6;3)?
1. Milyen típusú ciklusokat ismertek? Vázoljátok a különbségeket.
1. Mennyi parancs lehet a ciklusmagban? 
1. Írjátok fel a `for` ciklus szintaxiságt
1. `for` ciklus segítségével írjátok ki a szorzótáblát, amelyiket a felhasználótól bekéritek.
1. Számoljatok vissza 20tól 0ig `for` ciklussal, és írassátok ki a képernyőre
1. Mi a különbség a `break` és a `continue` parancsok között?
1. Hány `else` ága lehet a `for` ciklusnak? 
1. Kell-e mindig `else` ág?
1. Működik a `for` ciklus `break` nélkül?
1. Működik a `for` ciklus `continue` nélkül?