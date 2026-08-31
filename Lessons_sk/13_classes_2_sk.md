🗺️ [Späť na mapu](00_Mapa_sk.md)

> # ?? Triedy - pokrocil� (`__repr__`, `__dict__`, JSON)
>
> *Voliteln�, pokrocil� ucivo.*
>
> - `__str__(self)` - pou��vatelsky pr�vetiv� v�pis (`print(objekt)`)
> - `__repr__(self)` - v�voj�rsky pr�vetiv�, podrobn� v�pis (v zoznamoch sa zobraz� tento)
> - `objekt.__dict__` - vlastnosti objektu ako slovn�k
> - `json.dump(data, file)` / `json.load(file)` - ulo�enie a nac�tanie z JSON s�boru
> - `Trieda(**slovnik)` - vytvor� objekt zo slovn�ka ("rozbalenie")
>
> ```py
> class Kniha:
>     def __init__(self, nazov, cena):
>         self.nazov = nazov
>         self.cena = cena
>     def __repr__(self):
>         return f"Kniha(nazov='{self.nazov}', cena={self.cena})"
>
> kniha = Kniha("1984", 3500)
> print(kniha.__dict__)                 # {'nazov': '1984', 'cena': 3500}
> nova_kniha = Kniha(**kniha.__dict__)  # sp�t na objekt
> print(nova_kniha)
> ```
>
> **Metafora:** `__dict__` je, akoby sme objekt **vybalili zo �katule**: ka�d� jeho vlastnost je v oznacenej priehradke, ktor� vieme lahko ulo�it (do JSON-u) a nesk�r ju rovnako lahko znovu zabalit.

# Triedy - Pokrocil� t�my

T�to kapitola je urcen� �tudentom, ktor� sa chc� hlb�ie zaoberat programovan�m a pou��van�m tried.

## Funkcia `__repr__()`

Funkcia `__repr__()` vracia "ofici�lnu" textov� reprezent�ciu triedy. Je urcen� predov�etk�m pre v�voj�rov a ide�lne by mala vr�tit retazec, pomocou ktor�ho m�eme znovu vytvorit objekt.

### Rozdiel medzi `__str__()` a `__repr__()`

- `__str__()`: Pou��vatelsky pr�vetiv�, citateln� v�stup
- `__repr__()`: Pre v�voj�rov, jednoznacn�, podrobn� inform�cia

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

# Pri v�pise prvkov zoznamu sa pou��va __repr__
auta = [Auto("Ford", 2019, 4500000), Auto("BMW", 2021, 8000000)]
print(auta)
# [Auto(znacka='Ford', rok=2019, cena=4500000), Auto(znacka='BMW', rok=2021, cena=8000000)]
```

## Atrib�t `__dict__`

`__dict__` je �peci�lny atrib�t, ktor� obsahuje v�etky in�tancn� premenn� objektu vo forme slovn�ka.

```py
class Osoba:
    def __init__(self, meno, vek, mesto):
        self.meno = meno
        self.vek = vek
        self.mesto = mesto

osoba = Osoba("Kov�cs J�nos", 25, "Budape�t")

# Zobrazenie atrib�tov objektu
print(osoba.__dict__)
# {'meno': 'Kov�cs J�nos', 'vek': 25, 'mesto': 'Budape�t'}

# Dynamick� pridanie atrib�tu
osoba.povolanie = "in�inier"
print(osoba.__dict__)
# {'meno': 'Kov�cs J�nos', 'vek': 25, 'mesto': 'Budape�t', 'povolanie': 'in�inier'}
```

### Pou�itie `__dict__` na iter�ciu

```py
class Produkt:
    def __init__(self, nazov, cena, sklad):
        self.nazov = nazov
        self.cena = cena
        self.sklad = sklad
    
    def info(self):
        print("�daje produktu:")
        for kluc, hodnota in self.__dict__.items():
            print(f"  {kluc}: {hodnota}")

produkt = Produkt("Laptop", 250000, 15)
produkt.info()
# �daje produktu:
#   nazov: Laptop
#   cena: 250000
#   sklad: 15
```

## Pr�ca s JSON a objektami

JSON (JavaScript Object Notation) je popul�rny form�t �dajov, ktor� sa casto pou��va na ukladanie a prenos d�t. V Pythone s n�m pracujeme pomocou modulu `json`.

### Ulo�enie objektu do JSON s�boru

```py
import json

class Student:
    def __init__(self, meno, vek, znamky):
        self.meno = meno
        self.vek = vek
        self.znamky = znamky
    
    def to_dict(self):
        """Prevod objektu na slovn�k"""
        return {
            'meno': self.meno,
            'vek': self.vek,
            'znamky': self.znamky
        }

# Vytvorenie objektu Student
student1 = Student("Nagy Anna", 18, [5, 4, 5, 4, 5])

# Ulo�enie do JSON s�boru
with open('student.json', 'w', encoding='utf-8') as f:
    json.dump(student1.to_dict(), f, ensure_ascii=False, indent=4)

print("�daje �tudenta ulo�en� do s�boru student.json")
```

Obsah s�boru `student.json`:
```json
{
    "meno": "Nagy Anna",
    "vek": 18,
    "znamky": [5, 4, 5, 4, 5]
}
```

### Nac�tanie JSON s�boru a vytvorenie objektu

```py
import json

class Student:
    def __init__(self, meno, vek, znamky):
        self.meno = meno
        self.vek = vek
        self.znamky = znamky
    
    @classmethod
    def from_dict(cls, data):
        """Vytvorenie objektu zo slovn�ka"""
        return cls(data['meno'], data['vek'], data['znamky'])
    
    def __str__(self):
        return f"{self.meno} ({self.vek} rokov), zn�mky: {self.znamky}"

# Nac�tanie JSON s�boru
with open('student.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Vytvorenie objektu z nac�tan�ch �dajov
student = Student.from_dict(data)
print(student)
# Nagy Anna (18 rokov), zn�mky: [5, 4, 5, 4, 5]
```

### Ulo�enie viacer�ch objektov do JSON s�boru

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

# Vytvorenie �tudentov
studenti = [
    Student("Nagy Anna", 18, [5, 4, 5]),
    Student("Kov�cs P�ter", 19, [4, 5, 4]),
    Student("Szab� Kata", 18, [5, 5, 5])
]

# Ulo�enie do JSON s�boru
studenti_dict = [student.to_dict() for student in studenti]
with open('studenti.json', 'w', encoding='utf-8') as f:
    json.dump(studenti_dict, f, ensure_ascii=False, indent=4)

print("�tudenti ulo�en�")

# Nac�tanie zo JSON s�boru
with open('studenti.json', 'r', encoding='utf-8') as f:
    nacitane_data = json.load(f)

# Vytvorenie objektov
nacitani_studenti = [Student.from_dict(data) for data in nacitane_data]

print("\nNac�tan� �tudenti:")
for student in nacitani_studenti:
    print(student)
```

### Pr�ca s JSON pomocou `__dict__`

Ak je trieda jednoduch� (obsahuje len z�kladn� typy), m�eme priamo pou�it atrib�t `__dict__`:

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

# Ulo�enie do JSON pomocou __dict__
with open('kniha.json', 'w', encoding='utf-8') as f:
    json.dump(kniha.__dict__, f, ensure_ascii=False, indent=4)

# Nac�tanie zo JSON
with open('kniha.json', 'r', encoding='utf-8') as f:
    kniha_data = json.load(f)

# Vytvorenie objektu pomocou ** oper�tora (dictionary unpacking)
nova_kniha = Kniha(**kniha_data)
print(nova_kniha)
# Kniha(nazov='1984', autor='George Orwell', rok=1949, cena=3500)
```

## �pln� pr�klad: Spr�vca kni�nice

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
        """Pridanie knihy do kni�nice"""
        self.knihy.append(kniha)
        self.uloz()
        print(f"Kniha pridan�: {kniha}")
    
    def vypis(self):
        """Vyp�sanie v�etk�ch kn�h"""
        if not self.knihy:
            print("Kni�nica je pr�zdna")
            return
        
        print("\nObsah kni�nice:")
        for i, kniha in enumerate(self.knihy, 1):
            print(f"{i}. {kniha}")
    
    def uloz(self):
        """Ulo�enie kn�h do JSON s�boru"""
        knihy_dict = [kniha.__dict__ for kniha in self.knihy]
        with open(self.subor, 'w', encoding='utf-8') as f:
            json.dump(knihy_dict, f, ensure_ascii=False, indent=4)
    
    def nacitaj(self):
        """Nac�tanie kn�h zo JSON s�boru"""
        if not path.exists(self.subor):
            return
        
        try:
            with open(self.subor, 'r', encoding='utf-8') as f:
                knihy_data = json.load(f)
                self.knihy = [Kniha(**data) for data in knihy_data]
                print(f"{len(self.knihy)} kn�h nac�tan�ch")
        except json.JSONDecodeError:
            print("Chyba pri nac�tan� JSON s�boru")

# Pou�itie
kniznica = Kniznica()

# Pridanie nov�ch kn�h
kniznica.pridaj(Kniha("1984", "George Orwell", 1949, 3500))
kniznica.pridaj(Kniha("Zvieracia farma", "George Orwell", 1945, 2800))
kniznica.pridaj(Kniha("Hviezdy nad Egerom", "G�rdonyi G�za", 1901, 3200))

# Vyp�sanie kn�h
kniznica.vypis()
```

## U�itocn� tipy

### 1. Pou�itie `@property` pri ukladan� do JSON

Ak chceme ulo�it aj vypoc�tan� hodnoty:

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
            'priemer': self.priemer  # Vypoc�tan� hodnota sa tie� ulo��
        }
```

### 2. Pr�ca s d�tumami v JSON

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
            'datum': self.datum.isoformat()  # Konverzia do ISO form�tu
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(data['nazov'], data['datum'])

udalost = Udalost("Program�torsk� s�ta�", datetime(2026, 3, 15))
print(udalost.to_dict())
# {'nazov': 'Program�torsk� s�ta�', 'datum': '2026-03-15T00:00:00'}
```

> # ?? Pokazte to!
>
> Ak� je chyba v tomto programe?
>
> ```py
> class Kniha:
>     def __init__(self, nazov, cena):
>         self.nazov = nazov
>         self.cena = cena
>
> kniha = Kniha("1984", 3500)
> print(kniha)
> ```
>
> V�pis bude vyzerat asi takto: `<__main__.Kniha object at 0x...>`. Co v triede ch�ba, aby `print(kniha)` vyp�sal �daje pekne a citatelne?
>
> # ?? �lohy
> 1. Vytvor triedu `Ziak`, ktor� obsahuje meno �iaka, vek a obl�ben� predmety (zoznam). Implementuj met�dy `__str__()` a `__repr__()`.
> 2. Vytvor triedu `Kapela`, ktor� uklad� zoznam hudobn�kov. Implementuj ukladanie a nac�tavanie z JSON.
> 3. Roz��r pr�klad Spr�vca kni�nice o met�du `hladaj(autor)`, ktor� vr�ti v�etky knihy dan�ho autora.
> 4. Vytvor triedu `Dennik`, ktor� uklad� denn� z�znamy (d�tum a text). Pou�ij JSON s�bor na ukladanie �dajov.
>
> Dal�ie �lohy n�jdete v [priecinku s cviceniami](../Exercies/13_classes/).
>
> # ? Ot�zky
>
> 1. Ak� je rozdiel medzi funkciami `__str__()` a `__repr__()`?
> 2. Na co sl��i atrib�t `__dict__` objektu?
> 3. Preco je pohodln� vytvorit objekt zo slovn�ka pomocou oper�tora `**`?
> 4. Preco sa oplat� mat v triede `Kniznica` samostatn� funkcie `uloz()` a `nacitaj()`, namiesto rucnej pr�ce so s�bormi zaka�d�m?

