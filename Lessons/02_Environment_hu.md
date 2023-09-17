# A Python programozói környezet

## Alapvető tudnivalók

- Ingyenesen letölthető
- Bármilyen oprendszeren futtatható
- Kis helyigény
- Számtalan könyvtár -> Nagyon sok területen felhasználható
    - Alapvető programozás
    - Vezérléstechnika
    - Adatbáziskezelés
    - Stb.

## A környezetről közelebbről
- Szintaxis és fejlettség alapján a C nyelvhez hasonlít. 
- Két fő ablakkal dolgozunk.
    - **Shell** – itt futtatjuk a megírt programot
    - **Script szerkesztő** – itt írjuk a programokat

# Változók

- A változók a program azon elemei, amelyek különböző értékeket vehetnek fel, különböző adatok tárolására alkalmasak.
- Névvel ellátott memóriaterület
- Pl. x, z, szam, nev, lista

## Típusai 
- **Szám** – `int` – integer – egész számok tárolására kb. -36.000 és 36.000 közt. 10, -9, 0
- **Tizedes szám**– `float` – tizedes számok tárolására 95.78, 3.14, 79.21
- **Komplex szám**– `complex` – komplex számok tárolására -9+6j, 1-8j
- **Karakterlánc** – `str` – `string` – szöveg és bármilyen értelmes/értelmetlen karaktersorozat tárolására, használhattok `''` vagy `""`
    - pl. `'alma'`, `'3gomb'`, stb.
- **Logikai** – `bool` - Két értéke lehet:
    - `True` – Igaz (számértéke bármi, de nem 0)
    - `False` – Hamis/nem igaz (számértéke 0)
# Műveletek
## Matematikai operátorok
- `5 + 3`összeg
- `5 – 3` különbség
- `5 * 3` szorzat
- `5 / 3` osztás
- `5 // 3` osztás egész része
- `5 % 3` osztás maradéka
- `5 ** 3` hatvány
- `sqrt(5)` négyzetgyökvonás (matematikai modul szükséges hozzá)

## Logikai operátorok
- egyenlőség `==`
    - Pl. X==5 – megvizsgáljuk `X` egyenlő-e `5`-tel
- kisebb `<`
- kisebb vagy egyenlő `<=`
- nagyobb `>`
- nagyobb vagy egyenlő `>=`
- nem egyenlő `!=`
- értékadás `=`
    - Pl. `X=12` – az `X` változóba elmentjük a `12`-es értéket

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
2myvar = "John"  
my-var = "John"  
my var = "John"
```

# Gyakorlat 
1. Hozzatok létre az említett változótípusokból 2-t, és írassátok ki a képernyőre a `print()` függvény segítéségével.
1. A szám adattípusú változóknál próbáljátok ki az összes matematikai operátort!

## Segítség
- **Szám** – `int`
- **Tizedes szám**– `float`
- **Komplex szám** - `complex`
- **Karakterlánc** – `str` 
- **Logikai** – `bool` 
- egyenlőség `==`
- kisebb `<`
- kisebb vagy egyenlő `<=`
- nagyobb `>`
- nagyobb vagy egyenlő `>=`
- nem egyenlő `!=`
- értékadás `=`