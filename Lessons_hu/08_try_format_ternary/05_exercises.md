# 📋 Gyakorlófeladatok

A feladatok egyszerűtől a nehezebb felé haladnak. A témakör opcionális; ha valamelyik rész új, előbb olvasd el a [részletes tananyagot](02_main.md).

## 1. F-string alapok

Hozz létre `nev` és `kor` változókat, majd f-string segítségével írd ki például: `Anna 16 éves.`

## 2. Művelet beillesztése a szövegbe

Tárold el két szám összegét, majd írd ki f-stringgel ilyen formában: `12 + 8 = 20`. A számokat változtasd meg, és ellenőrizd, hogy a kimenet követi-e őket.

## 3. Formázott számok

Egy változóban tárolj egy tizedes számot, és írd ki két tizedesjeggyel. Ezután egy 0 és 1 közötti arányt jeleníts meg százalékként, egy tizedesjeggyel.

## 4. Ternary: páros vagy páratlan

Adj értéket a `szam` változónak. Egy ternary kifejezéssel válaszd ki a `"páros"` vagy `"páratlan"` szöveget, majd írd ki. Próbáld ki páros és páratlan számmal is.

## 5. Hibás szám kezelése

Kérj be egy szöveget, majd próbáld egész számmá alakítani. Ha a felhasználó nem számot ad meg, a program ne álljon le hibaüzenettel; írjon ki érthető tájékoztatást. Használj konkrét hibakezelést.

## 6. Saját hiba

Ha egy változóban tárolt pontszám 0 és 100 közötti tartományon kívül van, a `raise ValueError("A pontszám 0 és 100 közé essen!")` sorral jelezz hibát. Kezeld a hibát `try-except` segítségével.

## 7. Két egész szám beolvasása – összetett feladat

Kérj be két egész számot a felhasználótól, és addig ismételd a bekérést, amíg két érvényes egész számot nem ad meg. Ezután hasonlítsd össze őket, és írd ki, melyik a nagyobb. Használd mindhárom eszközt:

- `try-except` blokkot;
- formázást (f-stringet);
- ternary kifejezést.

Gondold át azt is, mi történjen, ha a két szám egyenlő.

## ⭐ 8. Opcionális kihívás

Kérj be egy összeget, majd jelenítsd meg két tizedesjeggyel. Ha a beolvasott érték nem alakítható számmá, kezeld a hibát. A sikeres esetben ternary kifejezéssel írd ki, hogy az összeg legalább 100-e.
