
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
