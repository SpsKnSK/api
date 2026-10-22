🗺️ [Vissza a térképhez](../../Lessons_hu/00_Terkep_hu.md) · [Alapok](01_basic.md) · [Gyakorlófeladatok](05_exercises.md)

# ✏️ Extrák – try, format, ternary

Ez a lecke **nem kötelező tananyag**, hanem hasznos kiegészítő trükkök gyűjteménye. Nem baj, ha most kihagyjátok, később bármikor visszatérhettek rá.

## try-except-finally

A hibák kezelésére szolgál. Hiba merülhet fel például ezekben az esetekben:

- nullával osztunk: `10 / 0`;
- hibás konvertálás: `int("alma")`;
- szöveget próbálunk egész számmal összeadni: `"alma" + 10`.

Ilyenkor a `try-except` szerkezettel kezelhetjük a hibát:

```python
try:
    int("alma")
except Exception as e:
    print(f"Hiba történt: {e}")
```

A `try` blokkban van a megkísérelt művelet, az `except` pedig akkor fut le, ha a megfelelő típusú hiba bekövetkezik. Lehetőség szerint a konkrét hibát kezeld, például a számkonverziónál a `ValueError`-t; az általános `Exception` elkapása kezdő példaként használható, de sok különböző hibát is elfedhet.

A `finally` blokk akkor is lefut, ha hiba történt, és akkor is, ha nem:

```python
try:
    szam = int("12")
    print(szam)
except ValueError:
    print("Nem megfelelő szám!")
finally:
    print("A művelet befejeződött.")
```

Kimenet:
```text
12
A művelet befejeződött.
```

Ha a konvertálást `int("alma")`-ra változtatod, az `except` üzenete jelenik meg, majd a `finally` üzenete is.

### Saját hiba előidézése a `raise` paranccsal

```python
try:
    raise Exception("Ez egy saját hiba")
except Exception as e:
    print(f"Hiba történt: {e}")
```

Kimenet:
```text
Hiba történt: Ez egy saját hiba
```

## format és f-string

További leírások: [a projekt formázási jegyzete](../../UsefulStuff/08_format.md) és [W3Schools – Python String Formatting](https://www.w3schools.com/python/python_string_formatting.asp).

### A `format()` metódus

A szövegben a `{0}`, `{1}` jelölések a `format()` argumentumainak indexére hivatkoznak. Az index 0-tól indul.

```python
sebessegkorlat = 130
sebesseg = 110
sablon = "{0} km/h sebességgel haladsz, a korlát {1} km/h."
print(sablon.format(sebesseg, sebessegkorlat))
```

Kimenet: `110 km/h sebességgel haladsz, a korlát 130 km/h.`

### f-string

Az f-stringben az `f` a szöveg elejére kerül, a behelyettesítendő változó vagy kifejezés pedig kapcsos zárójelbe.

```python
sebessegkorlat = 130
sebesseg = 110
print("A sebességed", sebesseg, "km/h, a korlát", sebessegkorlat, "km/h.")
print(f"A sebességed {sebesseg} km/h, a korlát {sebessegkorlat} km/h.")
```

Kimenet:
```text
A sebességed 110 km/h, a korlát 130 km/h.
A sebességed 110 km/h, a korlát 130 km/h.
```

Nem csak a `print()`-ben használhatjuk: az elkészült szöveget változóban is eltárolhatjuk.

```python
nev = "Anna"
uzenet = f"Szia, {nev}!"
print(uzenet)
```

Kimenet: `Szia, Anna!`

### Számok formázása

A formázási jelöléssel megadhatjuk a tizedesjegyek számát, például `:.2f` két tizedesjegyet jelent.

```python
ar = 12.5
arany = 0.387481
print(f"Ár: {ar:.2f}")
print(f"Arány: {arany:.1%}")
```

Kimenet:
```text
Ár: 12.50
Arány: 38.7%
```

## Ternary operator – feltételes kifejezés

A ternary operator (feltételes kifejezés, egysoros if) feltétel alapján választ két érték közül. Formája:

```python
valtozo = ertek_ha_igaz if feltetel else ertek_ha_hamis
```

Ugyanez hagyományos elágazással:

```python
a = 0
if 10 > 20:
    a = 20
else:
    a = 10
print(a)
```

Kimenet: `10`.

Rövidebben:

```python
a = 20 if 10 > 20 else 10
print(a)
```

Kimenet: `10`.

Valósabb példa:

```python
szam = 7
paros_vagy_paratlan = "páros" if szam % 2 == 0 else "páratlan"
print(paros_vagy_paratlan)
```

Kimenet: `páratlan`.

A ternary kifejezés egyszerű, két lehetőség közötti választásra való. Ha több ág vagy összetett logika kell, inkább hagyományos `if-elif-else` szerkezetet használj.
