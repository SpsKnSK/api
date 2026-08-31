# Változók

- A változók a program azon elemei, amelyek különböző értékeket vehetnek fel, különböző adatok tárolására alkalmasak.
- Névvel ellátott memóriaterület
- Változó nevei lehetnek: x, z, szam, nev, lista

## Típusai 
- **Szám** – `int` – integer – egész számok tárolására kb. -36.000 és 36.000 közt. 10, -9, 0
- **Tizedes szám**– `float` – tizedes számok tárolására 95.78, 3.14, 79.21
- **Karakterlánc** – `str` – `string` – szöveg és bármilyen értelmes/értelmetlen karaktersorozat tárolására, használhattok `''` vagy `""`
    - pl. `'alma'`, `'3gomb'`, stb.
- **Logikai** – `bool` - Két értéke lehet:
    - `True` – Igaz (számértéke bármi, de nem 0)
    - `False` – Hamis/nem igaz (számértéke 0)
# Műveletek
## Matematikai operátorok
- `5 + 3 = 8`összeg
- `5 – 3 = 2` különbség
- `5 * 3 = 15` szorzat
- `5 / 3 = 1.666` osztás
- `5 // 3 = 1` osztás egész része
- `5 % 3 = 2` osztás maradéka
- `5 ** 3 = 125` hatvány
- `sqrt(5)` négyzetgyökvonás (matematikai modul szükséges hozzá)

## Kerekítés
- `round` függvénnyel
- `round(a, x)`
- `a` – szám
- `x` - tizedes helyek száma

Pl. `round(12.345, 2)` eredménye `12.35`

Ha az `x`-et elhagyjuk, egész számra kerekít: `round(12.345)` eredménye `12`.

A szám helyére változó is írható!

## Feladat
1. A `print()` függvény segítségével írassátok ki a képernyőre a fenti matematikai műveltek eredményei közül legalább 5-öt
1. Írjatok programot, amely bekér két számot, majd kiírja a hányadosukat 3 tizedes helyre.
Ezután írassátok ki az egész részre való osztás eredményét és a maradékot.
Ügyeljetek rá, hogy a program laikus felhasználók számára is használható legyen (a program írjon egy-két szót is, ne csak a konkrét eredményeket).
    > `/` tizedes osztás: `18/7=2.5714285714285716`

    > `//` egészszámú osztás: `18//7=2`

    > `%` osztás utáni maradék: `18 % 7=4`
1. Írjunk programot a kör kerületének és területének kiszámítására.
Adatok, amiket megadunk: kör átmérője, Pí értéke: `3.14159`.
Végeredmény:
`Az X cm átmérőjű körnek Y cm a kerülete és Z négyzetcm a területe.`

## Logikai operátorok
A logikai operátorok lehetséges kimenetei:  `True`, `False`
- egyenlőség `==`, pl. X==5 – megvizsgáljuk `X` egyenlő-e `5`-tel
- kisebb `<`
- kisebb vagy egyenlő `<=`
- nagyobb `>`
- nagyobb vagy egyenlő `>=`
- nem egyenlő `!=`

Az értékadás **nem** logikai operátor: `=`, pl. `X=12` – az `X` változóba elmentjük a `12`-es értéket

# Program írásának szabályai
- Python-ban meg kell különböztetni a nagy és kisbetűt,
- A változók neve lehet betű szám és aláhúzás jel `_` kombinációja.
- A változók neve:
    - Nem kezdődhet számmal,
    - Nem tartalmazhat szóközt, tabulátort ,
    - Nem lehet rezervált szó(parancs, pl. Max, min, print, stb.)

## Korrekt változónév
```py
myvar = "John"  
my_var = "John"  
_my_var = "John"  
myVar = "John"  
MYVAR = "John"  
myvar2 = "John"
```
## Nem korrekt változónév, a program nem fut le
```py
2myvar = "John" #szammal kezdodik
my-var = "John" #kotojelet tartalmaz 
my var = "John" #szokozt tartalmaz
```

## Ajánlom a változók következő megnevezését
```py
my_var = "John"
myVar = "John"  
MyVar = "John"  
```

# Gyakorlat 
1. Hozzatok létre az említett változótípusokból 2-t, és írassátok ki a képernyőre a `print()` függvény segítéségével.
1. A szám adattípusú változóknál próbáljátok ki az összes matematikai operátort!
1. Kérjetek a felhasználótól 2 egész számot, tizedes számot, komplex számot, és írjátok ki az összegüket, szorzatukat a képernyőre
    1. egész szám beolvasása: `int(input())`
    1. tizedes szám beolvasása: `float(input())`
    1. komplex szám beolvasása: `complex(input())`

## Segítség
### Adattípusok

**Szám** – `int`|**Tizedes szám**– `float`
--|--
**Karakterlánc** – `str`|**Logikai** – `bool`

### Műveletek: 

| | | | |
|-|-|-|-|
összeadás `+`| kivonás `-` |  szorzás`*`| osztás `/` | 
egész számú osztás `//` | maradékos osztás `%` | hatványra emelés `**`| egyenlőség `==`
kisebb `<`|kisebb vagy egyenlő `<=` |nagyobb `>`| nagyobb vagy egyenlő `>=`
értékadás `=`|

# Kérdések
1. Mi a különbség az `=` és az `==` között. Mikor használod az egyiket, mikor a másikat? 
1. Mire szolgál a `round` függvény, írjatok rá példát.
1. A felhasználótól kérjétek be a háromszög két befogóját, és a Pitagorasz tételének segítségvel határozzátok meg az átfogót.
1. Írjatok 2 példát a megengedett változónevekre.
1. Írjatok 2 példát a **nem** megengedett váltóznevekre.
1. Hogyan ellenőrizhetjük, hogy `a` szám `b` szám osztója? Melyik műveletet használjátok?
1. Mi a különbség a `/` és `//` között?