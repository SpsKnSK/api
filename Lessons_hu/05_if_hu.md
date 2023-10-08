# If – Elif - Else
## Rövid ismétlő elmélet

- Hogy fut le egy program, milyen az „iránya“?
- Mi az, ami ezt befolyásolhatja?

> Program futtatása: általában utasítás utasítás után – szekvens haladás.
**A program szekvens haladását a következő utasításokkal lehet megváltoztatni:**
- feltételes utsítás `if`
- ciklusok `while`, `for`,

## Feltételes utasítás
```py
if feltétel_1:
    utasítások_1
elif feltétel_2:
    utasítások_2
...
elif feltétel_n:
    utasítások_n
else:
    utasítások_else
```

# Működése

- `if` szócska beírása kötelező.
- Ha a _feltétel_1_ igaz akkor elvégződnek az _utasítások_1_
- Ha **nem**, akkor az `elif` utasítás következik
- **else if == `elif`**
- Ha egy feltétel se igaz akkor az `else` utáni utasítások végződnek el.

## Szemléltető program

```py
jegy= int(input('Ird ide, hanyast kaptal ma: '))
if jegy == 1:
    print ('Gratulalok, ugyes vagy' )
    print ('Remelem, ebbo a tantargybol is ilyen jegyet kapsz')
elif jegy == 2:
    print ('Gratulalok, ez is egy szep jegy')
elif jegy == 3:
    print('Nem rossz, de legkozelebb olvasd at meg egyszer')
elif jegy == 4:
    print('Ez nem sokon mulott. Tanulj tobbet! ')
else:
    print('Tessek sokat tanulni es elgondolkodni a jovodon! ')
```

### Vizsgáljuk meg az előző programot
> Mit veszünk észre a programkódban:
**Több utasítás esetén elég egymás után begépelni a végrehajtani kívánt utasításokat.**

### Feladat
Készítsetek programot, amely meghatározza a közeg pH értékét.

Ha a pH érték kisebb, mint 7, akkor a közeg savas. Ha 7-tel egyenlő, akkor neutrális, ha nagyobb, mint 7, akkor lúgos.

### Feladat
Mini számológép készítése vezérlőmenüvel.
Alap matematikai műveletek (+-/*) végrehajtása, két megadott számmal.
Kérjétek be a felhasználótól az `a`, a `b` számot meg a `muvelet`et. A művelet alapján írjátok ki a képernyőre a végeredményt.

### Feladat
Kérjünk be 3 számot és döntsük el, melyik a legnagyobb, majd írassuk ki szavakkal a képernyőre

Pelda
```
Adj meg 3 számot.
2
5
1
A legnagyobb szám az: 5
```

Az előző feladatot módosítsuk:
1. A program a **legkisebb** számot írja ki.
2. A program a **középső** számot írja ki.
> Figyelem, a Python megengedi, hogy egyszerre több érteket is összehasonlítsatok `a<b<c`
### Feladat
- Kérjük be a háromszög 3 oldalának méretét.
- Határozzuk meg, megszerkeszthető-e a háromszög.
- Ha igen, írassuk ki a háromszög kerületét.
### Feladat
Készítsünk programot a következő elektrotechnikai mértékegységek megnevezésére:
- Volt
- Ohm
- Amper
- Farad
- Henry

Pl.
Ha beírjuk, hogy Volt, a program kiírja, hogy a feszültség mértékegysége.
```
Adj meg egy mertekegyseget: Volt
Feszultseg, [V]
```
Ha nem ismeri fel a mértékegységet, informálja a felhasználót
### Feladat
Készítsetek programot, amely a megadott évszámból megállapítja, milyen korúak vagyunk.

- Gyerekkor – 0-11
- Kamaszkor – 11-18
- Felnőttkor – 18-60
- Időskor – 60+

# Egymásba ágyazott feltételvizsgálat
Mindig van egy fő `if`. amiben lehet több `if` utasítás

## Szemléltető

```py
print ("gondoltam egy szamra")
szam=55
if szam>30 :
    if szam>40 :
        if szam>50 :
            print ("a szam nagyobb 50-nel")
        else: 
            print ("a szam kisebb 50—nel ")
```

### Fealadat
Kérjünk be egy számot, majd állapítsuk meg páratlan-e, vagy páros.

- Ha **páros**, vizsgáljuk meg:
    - Osztható-e 6-tal.
    - Nagyobb-e 100-nál.

- Ha **páratlan**, vizsgáljuk meg:
    - Oszthaó-e 5-tel.
    - Nagyobb-e 100-nál.

# Logikai kapcsolatok
## `and` logakai és
Akkor igaz, ha **minden** feltétel egyszerre teljesül 

a | b | a `and` b 
-|-|-
0|0|0
0|1|0
1|0|0
1|1|**1**

## `or` logikai vagy
akkor igaz, ha **legalább egy** feltétel teljesül
a | b | a `or` b 
-|-|-
0|0|0
0|1|**1**
1|0|**1**
1|1|**1**

## `not` logikai negálás
megfordítja a logikai változó értékét
a | `not` a 
-|-
0|**1**
1|**0**

```py
szam = int (input ('Adj meg egy szamot'))
if (szam > 3) and (szam < 10) :
    print ('ez a szam 3 es 10 kozott van')
if (szam == 3) or (szam == 5) :
    print('ez a szam 3as vagy 5os')
```
> a `()` nem kellenek, de jobban szemléltei, melyik feltétel tartozik egybe
### Feladat

Készítsetek programot, amely kiszámítja az ellenállás értékét két sorba, vagy két párhuzamosan kötött ellenállásból. A felhasználótól kérjétek be az `r1`, `r2` értékét, és azt, hogy sorosan vagy párhuzamosan vannak-e bekötve.

- Sorba kötött ellenállások kiszámítása: R=R1+R2
- Párhuzamosan kötött ellenállások kiszámítása: R=R1*R2/(R1+R2)

> Létre kell hoznunk még egy változót, amely segítségével meghatározhatjuk, hogy az ellenállások sorba, vagy párhuzamosan vannak-e kötve

# Kérdések
1. Írjátok le az egyutas elágazás szintaxisát, hogyan kell helyesen feltételt írni Pythonban. Vázoljátok fel az összes ágat.
1. Kell-e mindig az `if` parancs? Mikor használjuk?
1. Kell-e mindig az `elif` parancs? Mikor használjuk?
1. Kell-e mindig az `else` parancs? Mikor használjuk?
1. Mikor ad `False`t az `and` logikai operátor?
1. Mikor ad `False`t az `or` logikai operátor?
1. Mikor ad `True`t a `not` operátor?
1. Mikor lesz `True` a következő kifejezés: `(a > b) and (c < b) or (c == 1)`, írjatok rá két példát.
