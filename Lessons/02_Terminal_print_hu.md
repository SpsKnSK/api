# print()
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
## `sep` és `end` paraméterek


Ha megnézzük, hogy a `print` függvény definícióját:
```py
(function) def print(
    *values: object,
    sep: str | None = " ",
    end: str | None = "\n",
    file: SupportsWrite[str] | None = None,
    flush: Literal[False] = False
) -> None
```
láthatjátok, hogy 4 megnevezett paraméter, mi ebből 2vel fogunk foglalkozni.
### `sep`- separator
Ahogy a VS Code segít megérteni a paramétert _string inserted between values, default a space._ Ezzel válasszuk el a bemenő értékeket egymástól:
```py
print("alma", "bananan", "cseresznye")
```
> kimenet: `alma banan cseresznye`

Ha más írásjelet szeretnénk tenni közéjük, akkor a `sep` értéket kell változtatni, ezt pedig az alábbi módon tehetjük meg:
```py
print("alma", "bananan", "cseresznye", sep=".")
```
kimenet:
```
alma.banan.cseresznye
```

Próbáljátok meg más karakterekkel.

### `end`
Ahogy a VS Code segít megérteni a paramétert   _string appended after the last value, default a newline._ Ezt a karaktert teszi a sor végére:
```py
print('Ahoj')
print('Peter!')
```
kimenet
```
Ahoj
Peter
```


Ha más írásjelet szeretnénk tenni a sor végére, akkor az `end` értéket kell változtatni, ezt pedig az alábbi módon tehetjük meg:
```py
print("alma", "banan", end=".")
print("cseresznye")
```
> kimenet: `alma banan.csereszny`

Próbáljátok meg más karakterekkel.

## Speciális karakterek
- `""` üres karakter, úgy képzelhetjük el, mint a `0`t összeadásnál, vagy az `1`est szorzásnál, nem változik meg a végeredmény
- `"\n"` új sor karakter

## Mi a különbség az 1 és az "1" között?
- az `1` az szám, ami annyit tesz, mint a matekban 1-es érték
- az `"1"` karakter, úgy képzeljétek el, mintha azt írnátok a számítógépnek, hogy `egy`, nem érték, hanem szöveg
```py
print(1+1)
print("1"+"1")
```
kimenet
```
2
11
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

## Kérdések
1. Jellemezd a `print` függvényt, mire szolgál?
1. Ha több értéket, változót akarunk használni a `print` függvényben, hogyan tehetjük azt meg? Soroljatok fel példákat.
1. Hogyan jelenik meg a `""` karakter a képernyőn? Mutassatok rá példát!
1. Hogyan jelenik meg a `"\n"` karakter a képernyőn? Mutassatok rá példát!
1. Mi a különbség az `5` és az `"5"` között?
1. Mire használjuk a `print` függvény `sep` paraméterét, mi az alapméretezett értéke?
1. Mire használjuk a `print` függvény `end` paraméterét, mi az alapméretezett értéke?
1. Változtassátok meg a `sep` paramétert a következő kódban úgy, hogy reális ip-címet kapjatok:
    ```py
    print(192,168,100,1)
    ```
    elvárt kimenet:
    > 192.168.100.1
1. Változtassátok meg az `end` paramétert a következő kódban úgy, hogy egymás mellé írja ki a szöveget:
    ```py
    print('Szia')
    print('Peter!')
    ```
    elvárt kimenet:
    >Szia Peter!
1. Mire szolgál a `#` jel? 