🗺️ [Vissza a tananyag térképéhez](00_Terkep_hu.md) · [Részletesebb tananyag: If–Elif–Else](05_if_hu.md)

# 05 – Elágazás: if

## Mit fogok megtanulni?

A lecke végére képes leszek az if segítségével két lehetőség közül választani: a program egy feltételtől függően más-más utasítást hajt végre.

## Miért van erre szükségem?

Gondolj egy mozijegy-ellenőrzésre: ha valaki már betöltötte a 18. életévét, beléphet egy 18+ filmre; ha még nem, akkor nem.

A programok is gyakran hoznak ilyen döntéseket: például megvizsgálják, hogy egy szám pozitív-e, vagy hogy egy felhasználó elég idős-e valamihez.

## Nézzünk meg egy rövid példát!

~~~python
kor = 17

if kor >= 18:
    print("Beléphetsz.")
else:
    print("Még nem léphetsz be.")
~~~

**Kimenet:**

~~~text
Még nem léphetsz be.
~~~

### Soronként

- **kor = 17**: eltároljuk a vizsgált személy életkorát.
- **if kor >= 18:** a program megvizsgálja, hogy a kor legalább 18-e. A **>=** jelentése: nagyobb vagy egyenlő.
- **print("Beléphetsz.")**: ez a sor csak akkor fut le, ha a feltétel igaz.
- **else:** ez jelenti a másik lehetőséget: mi történjen, ha a feltétel hamis.
- **print("Még nem léphetsz be.")**: ez a sor akkor fut le, ha a kor kisebb 18-nál.

**Figyeld meg:**
- Az if és az else sor végén kettőspont (:) áll.
- A hozzájuk tartozó sorok beljebb kezdődnek. Ezt nevezzük **behúzásnak**.
- A **>=** összehasonlít, az **=** értéket ad egy változónak.

## Futtatás előtt tippelj!

Még ne futtasd le a programot. Írd le, mit fog kiírni!

~~~python
szam = 8

if szam > 10:
    print("A")
else:
    print("B")

print("C")
~~~

1. Mit ír ki a program, és milyen sorrendben?
2. Miért ezt írja ki?
3. Mi változik, ha a szam értékét 12-re cseréled?

Most futtasd le, és ellenőrizd a tippedet. Ha más eredményt kaptál, keresd meg, melyik feltétel alapján döntött a program.

## Próbáld ki önállóan!

### 1. Vezetett feladat

Egészítsd ki a programot úgy, hogy kiírja: "pozitív", ha a szám nagyobb nullánál, különben pedig "nem pozitív".

~~~python
szam = 5

if __________________:
    print("pozitív")
else:
    print("nem pozitív")
~~~

Próbáld ki a programot az 5, a 0 és a -3 értékkel is.

### 2. Önálló feladat

Kérj be egy egész számot, és írd ki, hogy **páros** vagy **páratlan**. Segítség: egy szám akkor páros, ha a 2-vel való osztás maradéka 0. Ha az osztás és a maradék még új neked, kérj segítséget a tanártól.

### 3. Önálló feladat

Kérd be a felhasználó életkorát. Ha legalább 18 éves, írd ki: "Felnőtt"; egyébként írd ki: "Még nem felnőtt".

### ⭐ Opcionális kihívás

Kérj be egy hőmérsékletet, majd írd ki:
- "fagyos", ha kisebb mint 0;
- "nem fagyos", ha 0 vagy nagyobb.

Ezután próbáld meg úgy módosítani a programot, hogy pontosan 0 esetén külön üzenetet írjon ki.

További gyakorlófeladatok: [If – feladatok](../Exercies/05_if/exercises_hu.md).

## Ellenőrizd, érted-e!

Próbálj válaszolni az alábbiakra az előző példa megnézése nélkül.

1. Mit jelent az if utáni feltétel?
2. Mi történik az else ágban?
3. Miért kell behúzni az if és az else alá tartozó sorokat?

**Mini feladat:** Mit ír ki ez a program?

~~~python
pont = 10

if pont >= 10:
    print("Sikerült")
else:
    print("Próbáld újra")
~~~

## 💥 Rontsátok el!

~~~python
kor = 17

if kor >= 18:
    print("Beléphetsz.")
else:
    print("Még nem léphetsz be.")
~~~

Írjatok olyan if szerkezeteket, amelyeket a Python hibával utasít vissza, vagy amelyek **nem azt csinálják**, amit várnánk.

Ötletek:
- Maradjon le a kettőspont: if kor >= 18
- Ne legyen behúzás az if alatti sorban.
- A blokk sorai eltérő behúzással kezdődjenek.
- Írjatok = jelet == helyett egy összehasonlításban: if kor = 18:
- Írjatok feltételt az else mögé: else kor < 18:

Olvassátok el a hibaüzenetet:
- Hogy hívják a hibát, és melyik sorra mutat?
- Melyik hibát jelzi a Python azonnal?
- Melyik esetben fut le a program, mégis rossz eredményt ad?