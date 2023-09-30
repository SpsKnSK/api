
# `while` ciklus
## Szintaxis, szabálykészlet, leírás
```py
while foFeltetel:
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
- a ciklusmagot egy bekezdéssel, tabbal, tanbulátorral válasszuk külön a `while` parancstól, így tudja a fordító, hogy éppen a ciklusmagban van.
- A `while` ciklus addig fut le, amíg a `foFeltetel` **igaz** (állhat több összehasonlításból is, amiket logakai operátorokkal `and`, `or`, `not` kötünk össze)
- Itt nincs kimondott ciklusváltozó
- Ahogy az `if`nél a `while` ciklusnál is van lehetőség `else` ágat létrehozni (_Python nyelv különlegessége_), akkor kerül lefutásra, ha a ciklusmagot **nem** szakítottuk meg `break` paranccsal
- A `continue` utáni utasítások nem futnak le,  viszont a ciklus újra kiértékeli a `foFeltetel`t, és ha az még mindig igaznak bizonyul, lefut a ciklusmag (de figyelem, ebben az esetben feltételhez kötött)
- A `break` befejezi a ciklusmag futtatását, és a ciklus utáni parancsot hajtja végre (de figyelem, ebben az esetben feltételhez kötött)

### Példák
```py
i = 0
while (i<3):
    print(i)
    i = i+1
```
```py
a = 10
i = 1
while (i<5):
    print(i+a)
    i = i+1
```

## Feladatok mellekelve

# Kérdések
1. Írjátok fel a `while` ciklus szintaxisát.
1. `while` ciklus segítségével írjátok ki a szorzótáblát, amelyiket a felhasználó határozza meg.
1. Számoljatok vissza 20tól 0ig `while` ciklussal, és írassátok ki a képernyőre minden 4. számot.
1. Mi a különbség a `break` és a `continue` parancsok között?
1. Hány `else` ága lehet a `while` ciklusnak? 
1. Kell-e mindig `else` ág?
1. Mikor fut le az `else` ág?
1. Működik a `while` ciklus `break` nélkül?
1. Működik a `while` ciklus `continue` nélkül?
1. Hogyan lehet végtelenig futó `while` ciklust létrehozni?
1. Mit ír ki a képernyőre az alábbi program?
    ```py
    while 1==1:
        break
        print("a")
    else:
        print("Else")
    print("Szep napot!")
    ```
1. Mit ír ki a képernyőre az alábbi program?
    ```py
    while 10 > 20:
        print("a")
    else:
        print("Else")
    ```