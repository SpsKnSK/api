# `print()`
- Adatok és információk kiírása a képernyőre
- Kiírhatunk:
    - Szöveget
    - Számokat
    - Változó tartalmát
    - Több változóval végzett matematikai műveletek eredményét

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
