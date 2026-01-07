# Osztályok - Haladó témák

Ez a fejezet azoknak a diákoknak szól, akik mélyebben szeretnének foglalkozni a programozással és az osztályok használatával.

## `__repr__()` függvény

A `__repr__()` függvény az osztály "hivatalos" string reprezentációját adja vissza. Elsősorban a fejlesztők számára készül, és ideális esetben olyan stringet ad vissza, amivel újra létre lehet hozni az objektumot.

### Különbség a `__str__()` és `__repr__()` között

- `__str__()`: Felhasználóbarát, olvasható kimenet
- `__repr__()`: Fejlesztőbarát, egyértelmű, részletes információ

```py
class Auto:
    def __init__(self, marka, ev, ar):
        self.marka = marka
        self.ev = ev
        self.ar = ar
    
    def __str__(self):
        return f"{self.marka} ({self.ev})"
    
    def __repr__(self):
        return f"Auto(marka='{self.marka}', ev={self.ev}, ar={self.ar})"

auto1 = Auto("Toyota", 2020, 5000000)

print(str(auto1))   # Toyota (2020)
print(repr(auto1))  # Auto(marka='Toyota', ev=2020, ar=5000000)

# Lista elemek kiírásánál a __repr__ használódik
autok = [Auto("Ford", 2019, 4500000), Auto("BMW", 2021, 8000000)]
print(autok)
# [Auto(marka='Ford', ev=2019, ar=4500000), Auto(marka='BMW', ev=2021, ar=8000000)]
```

## `__dict__` attribútum

A `__dict__` egy speciális attribútum, amely az objektum összes példányváltozóját egy szótárként tartalmazza.

```py
class Szemely:
    def __init__(self, nev, kor, varos):
        self.nev = nev
        self.kor = kor
        self.varos = varos

szemely = Szemely("Kovács János", 25, "Budapest")

# Az objektum attribútumainak megtekintése
print(szemely.__dict__)
# {'nev': 'Kovács János', 'kor': 25, 'varos': 'Budapest'}

# Dinamikus attribútum hozzáadása
szemely.foglalkozas = "mérnök"
print(szemely.__dict__)
# {'nev': 'Kovács János', 'kor': 25, 'varos': 'Budapest', 'foglalkozas': 'mérnök'}
```

### `__dict__` használata iteráláshoz

```py
class Termek:
    def __init__(self, nev, ar, keszlet):
        self.nev = nev
        self.ar = ar
        self.keszlet = keszlet
    
    def info(self):
        print("Termék adatai:")
        for kulcs, ertek in self.__dict__.items():
            print(f"  {kulcs}: {ertek}")

termek = Termek("Laptop", 250000, 15)
termek.info()
# Termék adatai:
#   nev: Laptop
#   ar: 250000
#   keszlet: 15
```

## JSON kezelés objektumokkal

A JSON (JavaScript Object Notation) egy népszerű adatformátum, amelyet gyakran használnak adatok tárolására és átvitelére. Pythonban a `json` modul segítségével dolgozhatunk vele.

### Objektum mentése JSON fájlba

```py
import json

class Diak:
    def __init__(self, nev, kor, jegyek):
        self.nev = nev
        self.kor = kor
        self.jegyek = jegyek
    
    def to_dict(self):
        """Az objektumot szótárrá alakítja"""
        return {
            'nev': self.nev,
            'kor': self.kor,
            'jegyek': self.jegyek
        }

# Diák objektum létrehozása
diak1 = Diak("Nagy Anna", 18, [5, 4, 5, 4, 5])

# Mentés JSON fájlba
with open('diak.json', 'w', encoding='utf-8') as f:
    json.dump(diak1.to_dict(), f, ensure_ascii=False, indent=4)

print("Diák adatai elmentve a diak.json fájlba")
```

A `diak.json` fájl tartalma:
```json
{
    "nev": "Nagy Anna",
    "kor": 18,
    "jegyek": [5, 4, 5, 4, 5]
}
```

### JSON fájl beolvasása és objektum létrehozása

```py
import json

class Diak:
    def __init__(self, nev, kor, jegyek):
        self.nev = nev
        self.kor = kor
        self.jegyek = jegyek
    
    @classmethod
    def from_dict(cls, adat):
        """Szótárból objektumot hoz létre"""
        return cls(adat['nev'], adat['kor'], adat['jegyek'])
    
    def __str__(self):
        return f"{self.nev} ({self.kor} éves), jegyek: {self.jegyek}"

# JSON fájl beolvasása
with open('diak.json', 'r', encoding='utf-8') as f:
    adat = json.load(f)

# Objektum létrehozása a beolvasott adatokból
diak = Diak.from_dict(adat)
print(diak)
# Nagy Anna (18 éves), jegyek: [5, 4, 5, 4, 5]
```

### Több objektum mentése JSON fájlba

```py
import json

class Diak:
    def __init__(self, nev, kor, jegyek):
        self.nev = nev
        self.kor = kor
        self.jegyek = jegyek
    
    def to_dict(self):
        return {
            'nev': self.nev,
            'kor': self.kor,
            'jegyek': self.jegyek
        }
    
    @classmethod
    def from_dict(cls, adat):
        return cls(adat['nev'], adat['kor'], adat['jegyek'])
    
    def __repr__(self):
        return f"Diak(nev='{self.nev}', kor={self.kor}, jegyek={self.jegyek})"

# Diákok létrehozása
diakok = [
    Diak("Nagy Anna", 18, [5, 4, 5]),
    Diak("Kovács Péter", 19, [4, 5, 4]),
    Diak("Szabó Kata", 18, [5, 5, 5])
]

# Mentés JSON fájlba
diakok_dict = [diak.to_dict() for diak in diakok]
with open('diakok.json', 'w', encoding='utf-8') as f:
    json.dump(diakok_dict, f, ensure_ascii=False, indent=4)

print("Diákok elmentve")

# Beolvasás JSON fájlból
with open('diakok.json', 'r', encoding='utf-8') as f:
    beolvasott_adatok = json.load(f)

# Objektumok létrehozása
beolvasott_diakok = [Diak.from_dict(adat) for adat in beolvasott_adatok]

print("\nBeolvasott diákok:")
for diak in beolvasott_diakok:
    print(diak)
```

### JSON kezelés `__dict__` használatával

Ha az osztály egyszerű (csak alapvető típusokat tartalmaz), használhatjuk közvetlenül a `__dict__` attribútumot:

```py
import json

class Konyv:
    def __init__(self, cim, szerzo, ev, ar):
        self.cim = cim
        self.szerzo = szerzo
        self.ev = ev
        self.ar = ar
    
    def __repr__(self):
        return f"Konyv(cim='{self.cim}', szerzo='{self.szerzo}', ev={self.ev}, ar={self.ar})"

# Könyv létrehozása
konyv = Konyv("1984", "George Orwell", 1949, 3500)

# Mentés JSON-ba a __dict__ használatával
with open('konyv.json', 'w', encoding='utf-8') as f:
    json.dump(konyv.__dict__, f, ensure_ascii=False, indent=4)

# Beolvasás JSON-ból
with open('konyv.json', 'r', encoding='utf-8') as f:
    konyv_adat = json.load(f)

# Objektum létrehozása a ** operátorral (dictionary unpacking)
uj_konyv = Konyv(**konyv_adat)
print(uj_konyv)
# Konyv(cim='1984', szerzo='George Orwell', ev=1949, ar=3500)
```

## Teljes példa: Könyvtár kezelő

```py
import json
from os import path

class Konyv:
    def __init__(self, cim, szerzo, ev, ar):
        self.cim = cim
        self.szerzo = szerzo
        self.ev = ev
        self.ar = ar
    
    def __str__(self):
        return f"{self.cim} - {self.szerzo} ({self.ev}), {self.ar} Ft"
    
    def __repr__(self):
        return f"Konyv(cim='{self.cim}', szerzo='{self.szerzo}', ev={self.ev}, ar={self.ar})"

class Konyvtar:
    def __init__(self, fajlnev='konyvtar.json'):
        self.fajlnev = fajlnev
        self.konyvek = []
        self.betoltes()
    
    def hozzaad(self, konyv):
        """Könyv hozzáadása a könyvtárhoz"""
        self.konyvek.append(konyv)
        self.mentes()
        print(f"Könyv hozzáadva: {konyv}")
    
    def listaz(self):
        """Összes könyv listázása"""
        if not self.konyvek:
            print("A könyvtár üres")
            return
        
        print("\nKönyvtár tartalma:")
        for i, konyv in enumerate(self.konyvek, 1):
            print(f"{i}. {konyv}")
    
    def mentes(self):
        """Könyvek mentése JSON fájlba"""
        konyvek_dict = [konyv.__dict__ for konyv in self.konyvek]
        with open(self.fajlnev, 'w', encoding='utf-8') as f:
            json.dump(konyvek_dict, f, ensure_ascii=False, indent=4)
    
    def betoltes(self):
        """Könyvek beolvasása JSON fájlból"""
        if not path.exists(self.fajlnev):
            return
        
        try:
            with open(self.fajlnev, 'r', encoding='utf-8') as f:
                konyvek_adat = json.load(f)
                self.konyvek = [Konyv(**adat) for adat in konyvek_adat]
                print(f"{len(self.konyvek)} könyv betöltve")
        except json.JSONDecodeError:
            print("Hiba a JSON fájl beolvasása során")

# Használat
konyvtar = Konyvtar()

# Új könyvek hozzáadása
konyvtar.hozzaad(Konyv("1984", "George Orwell", 1949, 3500))
konyvtar.hozzaad(Konyv("Állatfarm", "George Orwell", 1945, 2800))
konyvtar.hozzaad(Konyv("Egri csillagok", "Gárdonyi Géza", 1901, 3200))

# Könyvek listázása
konyvtar.listaz()
```

## Hasznos tippek

### 1. `@property` használata JSON mentésnél

Ha bizonyos számított értékeket is szeretnénk menteni:

```py
class Diak:
    def __init__(self, nev, jegyek):
        self.nev = nev
        self.jegyek = jegyek
    
    @property
    def atlag(self):
        return sum(self.jegyek) / len(self.jegyek) if self.jegyek else 0
    
    def to_dict(self):
        return {
            'nev': self.nev,
            'jegyek': self.jegyek,
            'atlag': self.atlag  # Számított érték is mentésre kerül
        }
```

### 2. Dátumok kezelése JSON-ban

```py
import json
from datetime import datetime

class Esemeny:
    def __init__(self, nev, datum):
        self.nev = nev
        self.datum = datum if isinstance(datum, datetime) else datetime.fromisoformat(datum)
    
    def to_dict(self):
        return {
            'nev': self.nev,
            'datum': self.datum.isoformat()  # ISO formátumra alakítás
        }
    
    @classmethod
    def from_dict(cls, adat):
        return cls(adat['nev'], adat['datum'])

esemeny = Esemeny("Programozás verseny", datetime(2026, 3, 15))
print(esemeny.to_dict())
# {'nev': 'Programozás verseny', 'datum': '2026-03-15T00:00:00'}
```

## Feladatok

1. Hozz létre egy `Tanulo` osztályt, amely tartalmazza a tanuló nevét, életkorát és kedvenc tantárgyait (lista). Implementáld a `__str__()` és `__repr__()` metódusokat.

2. Készíts egy `Zenekar` osztályt, amely zenészek listáját tárolja. Valósítsd meg a JSON mentést és betöltést.

3. Bővítsd a Könyvtár kezelő példát egy `kereses(szerzo)` metódussal, amely visszaadja az adott szerző összes könyvét.

4. Készíts egy `Naplo` osztályt, amely napi bejegyzéseket tárol (dátum és szöveg). Használj JSON fájlt az adatok tárolására.
