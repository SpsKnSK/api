🗺️ [Vissza a térképhez](00_Terkep_hu.md)

> # ✏️ `print()`
>
> **Mire jó?** Kiírja a képernyőre azt, amit a zárójelbe írunk: szöveget, számot, változót vagy egy művelet eredményét.
>
> **Alak:** `print(érték1, érték2, sep=" ", end="\n")` – a `sep` és az `end` nem kötelező
>
> | Amit írok | Mit jelent |
> |---|---|
> | `print("Szia")` | szöveg (idézőjelben!) |
> | `print(12)` | szám (idézőjel nélkül) |
> | `print(szam)` | a változó **tartalma** |
> | `print(a+b)` | előbb számol, aztán kiír |
> | `print(a, b)` | a vessző = szóköz a kimenetben |
> | `sep="."` | mi kerüljön az értékek **közé** (alapértelmezetten: szóköz) |
> | `end=" "` | mi kerüljön a sor **végére** (alapértelmezetten: új sor `\n`) |
> | `""` | üres szöveg |
> | `\n` | új sor jele |
> | `\t` | tabulátor |
>
> **Szám vagy szöveg:**
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
> a képernyőn
> ```
> 192.168.100.1
> Szia Peter!
> ```
>
> **Metafora:** a `print()` olyan, mint egy **kirakat**: amit kiállítasz benne (a zárójelbe írsz), azt a vásárló is látja (a képernyőn jelenik meg).

# `print()`
- Adatok és információk kiírása a képernyőre
- Kiírhatunk:
    - Szöveget
    - Számokat
    - Változó tartalmát
    - Több változóval végzett matematikai műveletek eredményét

### Feladatok
1. Szöveg kiírása (mi a különbség?):
    ```py
    print("Szia világ")
    print('Szia világ')
    ```
1. Szám kiírása (mi a különbség?):
    ```py
    print(123.45)
    print(123,45)
    ```
1. Változó kiírása
    ```py
    szam1 = 5
    print(szam1)
    ```
1. Összeg kiírása
    ```py
    szam1 = 5
    szam2 = 11
    print(szam1 + szam2)
    ```

## `print()` – vegyes kiírás
Egy `print()` utasításon belül több adatot is kiírhatunk.

Ezeket az adatokat vesszővel választjuk el.

```py
darab = 12
print(darab, "gitárhúr")
```
Egy `print()` utasításon belül különböző típusú adatokkal is végezhetünk műveleteket.

```py
szam1 = 12
szam2 = 8
print(szam1 + szam2, szam1 * szam2)
```
Szöveg, vagyis string esetén egy kicsit más a helyzet.
```py
print('egy csomag', 'gitár'+'húr')
```
### Kiírás egymás mellé vagy egymás alá
Ha a szöveget egy sorba szeretnénk kiírni, csak egy `print()` utasítást használunk, és az adatokat a zárójelbe írjuk.
```py
print('Szia', 'Peter!')
```
Ha a szöveget külön sorokba szeretnénk kiírni, több `print()` utasítást használunk, minden sorhoz egyet.
```py
print('Szia')
print('Peter!')
```
vagy használhatjuk az új sor jelét, a `\n` karaktert is
```py
print('Szia\nPeter!')
```
## `sep` és `end` paraméterek

Ha megnézzük a `print` függvény definícióját:
```py
(function) def print(
    *values: object,
    sep: str | None = " ",
    end: str | None = "\n",
    file: SupportsWrite[str] | None = None,
    flush: Literal[False] = False
) -> None
```
láthatjuk, hogy a `*values` tetszőleges számú kiírandó értéket jelent, utána pedig 4 megnevezett (kulcsszavas) paraméter következik. Ezek közül kettővel fogunk foglalkozni: a `sep` és az `end` paraméterrel.
### `sep` – elválasztó
Ahogy a Visual Studio Code segít megérteni ezt a paramétert: _string inserted between values, default a space._ Ezzel a szöveggel választjuk el a bemenő értékeket egymástól:
```py
print("alma", "körte", "cseresznye")
```
> kimenet: `alma körte cseresznye`

Ha más jelet szeretnénk közéjük tenni, a `sep` értékét így változtathatjuk meg:
```py
print("alma", "körte", "cseresznye", sep=".")
```
> kimenet: `alma.körte.cseresznye`

Próbáljátok ki más elválasztókkal is.

### `end`
Ez a szöveg kerül a sor végére. Mivel az `end` alapértelmezett értéke az új sor jele, a `\n`, két `print` utasítás kimenete egymás alá kerül:
```py
print('Szia')
print('Peter!')
```
kimenet:
```
Szia
Peter!
```

Ha más szöveget szeretnénk a sor végére írni, az `end` értékét így változtathatjuk meg:
```py
print('Szia', end=" ")
print('Peter!')
```
kimenet:
```
Szia Peter!
```

Próbáljátok ki más karakterekkel is.

## Speciális karakterek
- `""` üres szöveg (üres string): nem látszik semmi a képernyőn. Olyan, mint a `0` az összeadásnál: `"alma" + ""` továbbra is `alma`
- `"\n"` új sor jele: a szöveg innen új sorban folytatódik
- `"\t"` tabulátor: nagyobb szóköz, amely oszlopokba rendezi az adatokat
```py
print("alma\nkörte")
print("alma\tkörte")
```
kimenet:
```
alma
körte
alma    körte
```

## Megjegyzés (komment) – a `#` jel
A `#` jel utáni részt a Python **nem hajtja végre**, csak nekünk szóló emlékeztető:
```py
# ez egy megjegyzes, nem fut le
print("Szia")  # a sor végén is lehet
```

## Mi a különbség az `1` és az `"1"` között?
- Az `1` egy szám, amely a matematikai egyes értéket jelenti.
- Az `"1"` szöveg. Képzeljétek el úgy, mintha azt írnátok a számítógépnek, hogy `egy`: nem érték, hanem szöveg.
```py
print(1+1)
print("1"+"1")
```
kimenet:
```
2
11
```
> Számoknál a `+` **összead**, szövegnél **összeragaszt**.


## Példák
Adott három változó a következő értékekkel:
```py
elso = 12
masodik = 24
harmadik = 34
```
1. Írjátok ki ezt a három számot a képernyőre a következőképpen:
    ```
    Elso szam: 12
    Masodik szam: 24
    Harmadik szam: 34
    ```
    Oldjátok meg úgy is, hogy csak **egy** `print` utasítást használtok.

2. Írjátok ki a három szám összegét és az első két szám szorzatát.

> # 💥 Rontsátok el!
> Írjatok olyan `print` sorokat, amelyeket a Python hibával utasít vissza. Ötletek:
>
> - hiányzó zárójel vagy idézőjel
> - kevert idézőjelek
> - a függvény nevének elrontása (például nagy `P` betű)
> - idézőjel nélküli szöveg
> - több vessző vagy pont használata
>
> Olvassátok el a hibaüzenetet: melyik sorra mutat, és mi a hiba neve? Mire jutottatok?

> # ❓ Kérdések
> 1. Jellemezzétek a `print` függvényt! Mire szolgál?
> 1. Ha több értéket vagy változót szeretnénk használni a `print` függvényben, hogyan tehetjük meg? Soroljatok fel példákat.
> 1. Hogyan jelenik meg az üres string, a `""` a képernyőn? Mutassatok rá példát.
> 1. Hogyan jelenik meg a `"\n"` karakter a képernyőn? Mutassatok rá példát.
> 1. Mi a különbség az `5` és az `"5"` között?
> 1. Mire használjuk a `print` függvény `sep` paraméterét, és mi az alapértelmezett értéke?
> 1. Mire használjuk a `print` függvény `end` paraméterét, és mi az alapértelmezett értéke?
> 1. Változtassátok meg a `sep` paramétert a következő kódban úgy, hogy valódi IP-címet kapjatok:
>     ```py
>     print(192,168,100,1)
>     ```
>     elvárt kimenet: `192.168.100.1`
> 1. Változtassátok meg az `end` paramétert a következő kódban úgy, hogy a szövegek egymás mellé kerüljenek:
>     ```py
>     print('Szia')
>     print('Peter!')
>     ```
>     elvárt kimenet: `Szia Peter!`
> 1. Mire szolgál a `#` jel?
