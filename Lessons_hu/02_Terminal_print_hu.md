> # ✏️ `print()`
>
> **Mire jó?** Kiírja a képernyőre azt, amit a zárójelbe teszünk: szöveget, számot, változót, művelet eredményét.
>
> **Alak:** `print(érték1, érték2, sep=" ", end="\n")` a `sep` és az `end` nem kötelező
>
> | Amit írok | Mit jelent |
> |---|---|
> | `print("Szia")` | szöveg (idézőjelben!) |
> | `print(12)` | szám (idézőjel nélkül) |
> | `print(szam)` | változó **tartalma** |
> | `print(a+b)` | előbb számol, aztán ír |
> | `print(a, b)` | a vessző = szóköz a kimenetben |
> | `sep="."` | mi kerüljön az értékek **közé** (alap: szóköz) |
> | `end=" "` | mi kerüljön a sor **végére** (alap: új sor `\n`) |
> | `""` | üres string |
> | `\n` | új sor jele |
> | `\t` | tabulátor |
>
> **Szám vs. szöveg:**
> ```py
> print(1+1)      # 2   -> összeadás
> print("1"+"1")  # 11  -> összeragasztás
> ```
>
> **Példa:**
> ```py
> print(192, 168, 100, 1, sep=".")
> print("Szia", end=" ")
> print("Peter!")
> ```
> képernyőn
> ```
> 192.168.100.1
> Szia Peter!
> ```
>
> **Metafora:** a `print()` olyan, mint egy **kirakat**: bármit teszel bele zárójelbe, azt kiteszi, hogy mindenki lássa a "kirakatban" (a képernyőn).
# print()
- Adatok, információk kiíratása a képernyőre
- Kiírathatunk:
    - Szöveget
    - Számokat
    - Változó tartalmát
    - Több változóval elvégzett matematikai műveletek eredményét

### Feladat
1. Szöveg kiíratása (mi a különbség?):
    ```py
    print("Hello World")
    print('Hello World')
    ```
1. Szám kiíratása (mi a különbség?):
    ```py
    print(123.45)
    print(123,45)
    ```
1. Változó kiíratása
    ```py
    szam1=5
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
láthatjátok, hogy a `*values` a tetszőleges számú kiírandó érték, utána pedig 4 megnevezett (kulcsszavas) paraméter következik. Mi ebből kettővel fogunk foglalkozni: `sep` és `end`.
### `sep`- separator
Ahogy a VS Code segít megérteni a paramétert _string inserted between values, default a space._ Ezzel válasszuk el a bemenő értékeket egymástól:
```py
print("alma", "banan", "cseresznye")
```
> kimenet: `alma banan cseresznye`

Ha más írásjelet szeretnénk tenni közéjük, akkor a `sep` értéket kell változtatni, ezt pedig az alábbi módon tehetjük meg:
```py
print("alma", "banan", "cseresznye", sep=".")
```
> kimenet: `alma.banan.cseresznye`

Próbáljátok meg más karakterekkel.

### `end`
Ezt a karaktert teszi a sor végére. Mivel az alapértelmezett `end` az új sor karakter `\n`, a két print kimenete egymás alá kerül:
```py
print('Szia')
print('Peter!')
```
kimenet
```
Szia
Peter!
```

Ha más írásjelet szeretnénk tenni a sor végére, akkor az `end` értéket kell változtatni, ezt pedig az alábbi módon tehetjük meg:
```py
print('Szia', end=" ")
print('Peter!')
```
kimenet: 
```
Szia Peter!
```

Próbáljátok meg más karakterekkel.

## Speciális karakterek
- `""` üres szöveg (üres string): nem látszik semmi a képernyőn. Olyan, mint a `0` az összeadásnál: `"alma" + ""` továbbra is `alma`
- `"\n"` új sor karakter: innentől a szöveg új sorban folytatódik
- `"\t"` tabulátor: nagyobb, oszlopokba rendező köz
```py
print("alma\nbanan")
print("alma\tbanan")
```
kimenet
```
alma
banan
alma    banan
```

## Megjegyzés (komment) – a `#` jel
A `#` jel utáni részt a Python **nem hajtja végre**, csak nekünk szól emlékeztetőül:
```py
# ez egy megjegyzes, nem fut le
print("Szia")  # a sor vegen is lehet
```

## Mi a különbség az 1 és az "1" között?
- az `1` az szám, ami annyit tesz, mint a matekban 1-es érték
- az `"1"` szöveg, úgy képzeljétek el, mintha azt írnátok a számítógépnek, hogy `egy`, nem érték, hanem szöveg
```py
print(1+1)
print("1"+"1")
```
kimenet
```
2
11
```
> Számoknál a `+` **összead**, szövegnél **összeragaszt**.


## Gyakorlat
Adott 3 változó a következő értékekkel:
```py
elso=12
masodik=24
harmadik=34
```
1. Írassátok ki ezt a három számot a képernyőre a következő formában: 
    ```
    Elso szam: 12
    Masodik szam: 24
    Harmadik szam: 34
    ```
    Oldjátok meg úgy is, hogy csak **egy** `print`-et használtok.
2. Írassátok ki a három szám összegét és az első két szám szorzatát.

> # 💥 Rontsátok el!
> Írjatok olyan `print` sorokat, amiket a Python hibával utasít vissza. Ötletek:
>
> - hiányzó zárójel vagy idézőjel
> - kevert idézőjel
> - a függvény nevének elrontása (pl. nagy `P` betű)
> - idézőjel nélküli szöveg
> - több vessző, pont alkalmazása
>
> Olvassátok el a hibaüzenetet: melyik sorra mutat, és mi a hiba neve? Mire jutottatok?

> # ❓ Kérdések
> 1. Jellemezd a `print` függvényt, mire szolgál?
> 1. Ha több értéket, változót akarunk használni a `print` függvényben, hogyan tehetjük azt meg? Soroljatok fel példákat.
> 1. Hogyan jelenik meg a `""` üres string a képernyőn? Mutassatok rá példát!
> 1. Hogyan jelenik meg a `"\n"` karakter a képernyőn? Mutassatok rá példát!
> 1. Mi a különbség az `5` és az `"5"` között?
> 1. Mire használjuk a `print` függvény `sep` paraméterét, mi az alapértelmezett értéke?
> 1. Mire használjuk a `print` függvény `end` paraméterét, mi az alapértelmezett értéke?
> 1. Változtassátok meg a `sep` paramétert a következő kódban úgy, hogy reális ip-címet kapjatok:
>     ```py
>     print(192,168,100,1)
>     ```
>     elvárt kimenet: `192.168.100.1`
> 1. Változtassátok meg az `end` paramétert a következő kódban úgy, hogy egymás mellé írja ki a szöveget:
>     ```py
>     print('Szia')
>     print('Peter!')
>     ```
>     elvárt kimenet: `Szia Peter!`
> 1. Mire szolgál a `#` jel?
