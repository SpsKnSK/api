# Triedy - Pokročilé témy

Táto kapitola je určená študentom, ktorí sa chcú hlbšie zaoberať programovaním a používaním tried.

## Funkcia `__repr__()`

Funkcia `__repr__()` vracia "oficiálnu" textovú reprezentáciu triedy. Je určená predovšetkým pre vývojárov a ideálne by mala vrátiť reťazec, pomocou ktorého môžeme znovu vytvoriť objekt.

### Rozdiel medzi `__str__()` a `__repr__()`

- `__str__()`: Používateľsky prívetivý, čitateľný výstup
- `__repr__()`: Pre vývojárov, jednoznačný, podrobná informácia

```py
class Auto:
    def __init__(self, znacka, rok, cena):
        self.znacka = znacka
        self.rok = rok
        self.cena = cena
    
    def __str__(self):
        return f"{self.znacka} ({self.rok})"
    
    def __repr__(self):
        return f"Auto(znacka='{self.znacka}', rok={self.rok}, cena={self.cena})"

auto1 = Auto("Toyota", 2020, 5000000)

print(str(auto1))   # Toyota (2020)
print(repr(auto1))  # Auto(znacka='Toyota', rok=2020, cena=5000000)

# Pri výpise prvkov zoznamu sa používa __repr__
auta = [Auto("Ford", 2019, 4500000), Auto("BMW", 2021, 8000000)]
print(auta)
# [Auto(znacka='Ford', rok=2019, cena=4500000), Auto(znacka='BMW', rok=2021, cena=8000000)]
```

## Atribút `__dict__`

`__dict__` je špeciálny atribút, ktorý obsahuje všetky inštančné premenné objektu vo forme slovníka.

```py
class Osoba:
    def __init__(self, meno, vek, mesto):
        self.meno = meno
        self.vek = vek
        self.mesto = mesto

osoba = Osoba("Kovács János", 25, "Budapešť")

# Zobrazenie atribútov objektu
print(osoba.__dict__)
# {'meno': 'Kovács János', 'vek': 25, 'mesto': 'Budapešť'}

# Dynamické pridanie atribútu
osoba.povolanie = "inžinier"
print(osoba.__dict__)
# {'meno': 'Kovács János', 'vek': 25, 'mesto': 'Budapešť', 'povolanie': 'inžinier'}
```

### Použitie `__dict__` na iteráciu

```py
class Produkt:
    def __init__(self, nazov, cena, sklad):
        self.nazov = nazov
        self.cena = cena
        self.sklad = sklad
    
    def info(self):
        print("Údaje produktu:")
        for kluc, hodnota in self.__dict__.items():
            print(f"  {kluc}: {hodnota}")

produkt = Produkt("Laptop", 250000, 15)
produkt.info()
# Údaje produktu:
#   nazov: Laptop
#   cena: 250000
#   sklad: 15
```

## Práca s JSON a objektami

JSON (JavaScript Object Notation) je populárny formát údajov, ktorý sa často používa na ukladanie a prenos dát. V Pythone s ním pracujeme pomocou modulu `json`.

### Uloženie objektu do JSON súboru

```py
import json

class Student:
    def __init__(self, meno, vek, znamky):
        self.meno = meno
        self.vek = vek
        self.znamky = znamky
    
    def to_dict(self):
        """Prevod objektu na slovník"""
        return {
            'meno': self.meno,
            'vek': self.vek,
            'znamky': self.znamky
        }

# Vytvorenie objektu Student
student1 = Student("Nagy Anna", 18, [5, 4, 5, 4, 5])

# Uloženie do JSON súboru
with open('student.json', 'w', encoding='utf-8') as f:
    json.dump(student1.to_dict(), f, ensure_ascii=False, indent=4)

print("Údaje študenta uložené do súboru student.json")
```

Obsah súboru `student.json`:
```json
{
    "meno": "Nagy Anna",
    "vek": 18,
    "znamky": [5, 4, 5, 4, 5]
}
```

### Načítanie JSON súboru a vytvorenie objektu

```py
import json

class Student:
    def __init__(self, meno, vek, znamky):
        self.meno = meno
        self.vek = vek
        self.znamky = znamky
    
    @classmethod
    def from_dict(cls, data):
        """Vytvorenie objektu zo slovníka"""
        return cls(data['meno'], data['vek'], data['znamky'])
    
    def __str__(self):
        return f"{self.meno} ({self.vek} rokov), známky: {self.znamky}"

# Načítanie JSON súboru
with open('student.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Vytvorenie objektu z načítaných údajov
student = Student.from_dict(data)
print(student)
# Nagy Anna (18 rokov), známky: [5, 4, 5, 4, 5]
```

### Uloženie viacerých objektov do JSON súboru

```py
import json

class Student:
    def __init__(self, meno, vek, znamky):
        self.meno = meno
        self.vek = vek
        self.znamky = znamky
    
    def to_dict(self):
        return {
            'meno': self.meno,
            'vek': self.vek,
            'znamky': self.znamky
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(data['meno'], data['vek'], data['znamky'])
    
    def __repr__(self):
        return f"Student(meno='{self.meno}', vek={self.vek}, znamky={self.znamky})"

# Vytvorenie študentov
studenti = [
    Student("Nagy Anna", 18, [5, 4, 5]),
    Student("Kovács Péter", 19, [4, 5, 4]),
    Student("Szabó Kata", 18, [5, 5, 5])
]

# Uloženie do JSON súboru
studenti_dict = [student.to_dict() for student in studenti]
with open('studenti.json', 'w', encoding='utf-8') as f:
    json.dump(studenti_dict, f, ensure_ascii=False, indent=4)

print("Študenti uložení")

# Načítanie zo JSON súboru
with open('studenti.json', 'r', encoding='utf-8') as f:
    nacitane_data = json.load(f)

# Vytvorenie objektov
nacitani_studenti = [Student.from_dict(data) for data in nacitane_data]

print("\nNačítaní študenti:")
for student in nacitani_studenti:
    print(student)
```

### Práca s JSON pomocou `__dict__`

Ak je trieda jednoduchá (obsahuje len základné typy), môžeme priamo použiť atribút `__dict__`:

```py
import json

class Kniha:
    def __init__(self, nazov, autor, rok, cena):
        self.nazov = nazov
        self.autor = autor
        self.rok = rok
        self.cena = cena
    
    def __repr__(self):
        return f"Kniha(nazov='{self.nazov}', autor='{self.autor}', rok={self.rok}, cena={self.cena})"

# Vytvorenie knihy
kniha = Kniha("1984", "George Orwell", 1949, 3500)

# Uloženie do JSON pomocou __dict__
with open('kniha.json', 'w', encoding='utf-8') as f:
    json.dump(kniha.__dict__, f, ensure_ascii=False, indent=4)

# Načítanie zo JSON
with open('kniha.json', 'r', encoding='utf-8') as f:
    kniha_data = json.load(f)

# Vytvorenie objektu pomocou ** operátora (dictionary unpacking)
nova_kniha = Kniha(**kniha_data)
print(nova_kniha)
# Kniha(nazov='1984', autor='George Orwell', rok=1949, cena=3500)
```

## Úplný príklad: Správca knižnice

```py
import json
from os import path

class Kniha:
    def __init__(self, nazov, autor, rok, cena):
        self.nazov = nazov
        self.autor = autor
        self.rok = rok
        self.cena = cena
    
    def __str__(self):
        return f"{self.nazov} - {self.autor} ({self.rok}), {self.cena} Ft"
    
    def __repr__(self):
        return f"Kniha(nazov='{self.nazov}', autor='{self.autor}', rok={self.rok}, cena={self.cena})"

class Kniznica:
    def __init__(self, subor='kniznica.json'):
        self.subor = subor
        self.knihy = []
        self.nacitaj()
    
    def pridaj(self, kniha):
        """Pridanie knihy do knižnice"""
        self.knihy.append(kniha)
        self.uloz()
        print(f"Kniha pridaná: {kniha}")
    
    def vypis(self):
        """Vypísanie všetkých kníh"""
        if not self.knihy:
            print("Knižnica je prázdna")
            return
        
        print("\nObsah knižnice:")
        for i, kniha in enumerate(self.knihy, 1):
            print(f"{i}. {kniha}")
    
    def uloz(self):
        """Uloženie kníh do JSON súboru"""
        knihy_dict = [kniha.__dict__ for kniha in self.knihy]
        with open(self.subor, 'w', encoding='utf-8') as f:
            json.dump(knihy_dict, f, ensure_ascii=False, indent=4)
    
    def nacitaj(self):
        """Načítanie kníh zo JSON súboru"""
        if not path.exists(self.subor):
            return
        
        try:
            with open(self.subor, 'r', encoding='utf-8') as f:
                knihy_data = json.load(f)
                self.knihy = [Kniha(**data) for data in knihy_data]
                print(f"{len(self.knihy)} kníh načítaných")
        except json.JSONDecodeError:
            print("Chyba pri načítaní JSON súboru")

# Použitie
kniznica = Kniznica()

# Pridanie nových kníh
kniznica.pridaj(Kniha("1984", "George Orwell", 1949, 3500))
kniznica.pridaj(Kniha("Zvieracia farma", "George Orwell", 1945, 2800))
kniznica.pridaj(Kniha("Hviezdy nad Egerom", "Gárdonyi Géza", 1901, 3200))

# Vypísanie kníh
kniznica.vypis()
```

## Užitočné tipy

### 1. Použitie `@property` pri ukladaní do JSON

Ak chceme uložiť aj vypočítané hodnoty:

```py
class Student:
    def __init__(self, meno, znamky):
        self.meno = meno
        self.znamky = znamky
    
    @property
    def priemer(self):
        return sum(self.znamky) / len(self.znamky) if self.znamky else 0
    
    def to_dict(self):
        return {
            'meno': self.meno,
            'znamky': self.znamky,
            'priemer': self.priemer  # Vypočítaná hodnota sa tiež uloží
        }
```

### 2. Práca s dátumami v JSON

```py
import json
from datetime import datetime

class Udalost:
    def __init__(self, nazov, datum):
        self.nazov = nazov
        self.datum = datum if isinstance(datum, datetime) else datetime.fromisoformat(datum)
    
    def to_dict(self):
        return {
            'nazov': self.nazov,
            'datum': self.datum.isoformat()  # Konverzia do ISO formátu
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(data['nazov'], data['datum'])

udalost = Udalost("Programátorská súťaž", datetime(2026, 3, 15))
print(udalost.to_dict())
# {'nazov': 'Programátorská súťaž', 'datum': '2026-03-15T00:00:00'}
```

## Úlohy

1. Vytvor triedu `Ziak`, ktorá obsahuje meno žiaka, vek a obľúbené predmety (zoznam). Implementuj metódy `__str__()` a `__repr__()`.

2. Vytvor triedu `Kapela`, ktorá ukladá zoznam hudobníkov. Implementuj ukladanie a načítavanie z JSON.

3. Rozšír príklad Správca knižnice o metódu `hladaj(autor)`, ktorá vráti všetky knihy daného autora.

4. Vytvor triedu `Dennik`, ktorá ukladá denné záznamy (dátum a text). Použij JSON súbor na ukladanie údajov.
