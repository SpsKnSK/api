# Triedy - Hlbšie poznatky

Táto kapitola sa už vážne zaoberá detailmi objektovo orientovaného programovania. Je odporúčaná tým, ktorí sa vážne venujú programovaniu.

## Dekorátor `@property` - Getter a Setter

Pomocou dekorátora `@property` môžeme kontrolovať, ako pristupujeme k atribútu a ako nastavujeme jeho hodnotu.

### Jednoduchá property

```py
class Teplomer:
    def __init__(self):
        self._celsius = 0
    
    @property
    def celsius(self):
        """Getter - získanie hodnoty celsius"""
        return self._celsius
    
    @celsius.setter
    def celsius(self, hodnota):
        """Setter - nastavenie hodnoty celsius s kontrolou"""
        if hodnota < -273.15:
            raise ValueError("Teplota nemôže byť nižšia ako -273.15°C")
        self._celsius = hodnota
    
    @property
    def fahrenheit(self):
        """Výpočet hodnoty Fahrenheit z celsius"""
        return self._celsius * 9/5 + 32
    
    @fahrenheit.setter
    def fahrenheit(self, hodnota):
        """Nastavenie Fahrenheit, prevod na celsius"""
        self.celsius = (hodnota - 32) * 5/9

# Použitie
t = Teplomer()
t.celsius = 25
print(f"{t.celsius}°C = {t.fahrenheit}°F")  # 25°C = 77.0°F

t.fahrenheit = 100
print(f"{t.celsius}°C = {t.fahrenheit}°F")  # 37.77°C = 100.0°F

# t.celsius = -300  # ValueError: Teplota nemôže byť nižšia ako -273.15°C
```

### Property deleter

```py
class Pouzivatel:
    def __init__(self, meno, heslo):
        self._meno = meno
        self._heslo = heslo
    
    @property
    def heslo(self):
        raise AttributeError("Heslo nie je čitateľné!")
    
    @heslo.setter
    def heslo(self, nove_heslo):
        if len(nove_heslo) < 8:
            raise ValueError("Heslo musí mať aspoň 8 znakov")
        self._heslo = nove_heslo
        print("Heslo úspešne zmenené")
    
    @heslo.deleter
    def heslo(self):
        print("Heslo vymazané, nastavené predvolené heslo")
        self._heslo = "default123"

user = Pouzivatel("Ján", "tajne123")
user.heslo = "noveheslo2024"  # Heslo úspešne zmenené
# print(user.heslo)  # AttributeError: Heslo nie je čitateľné!
del user.heslo  # Heslo vymazané, nastavené predvolené heslo
```

## Triedne premenné vs Inštančné premenné

### Rozdiely

```py
class Pes:
    # Triedna premenná - spoločná pre všetky inštancie
    druh = "Canis familiaris"
    pocet_jedincov = 0
    
    def __init__(self, meno, vek):
        # Inštančné premenné - každá inštancia má vlastné
        self.meno = meno
        self.vek = vek
        # Úprava triednej premennej
        Pes.pocet_jedincov += 1
    
    @classmethod
    def vsetci_psi(cls):
        return cls.pocet_jedincov

# Triedna premenná je prístupná cez triedu
print(Pes.druh)  # Canis familiaris

# Vytvorenie inštancií
buddy = Pes("Buddy", 5)
max_pes = Pes("Max", 3)

print(buddy.druh)  # Canis familiaris
print(max_pes.druh)  # Canis familiaris
print(Pes.pocet_jedincov)  # 2

# Úprava triednej premennej - ovplyvní všetky inštancie
Pes.druh = "Canis lupus familiaris"
print(buddy.druh)  # Canis lupus familiaris

# Vytvorenie inštančnej premennej s rovnakým názvom
buddy.druh = "Len Buddy verzia"
print(buddy.druh)  # Len Buddy verzia
print(max_pes.druh)  # Canis lupus familiaris (nezmenilo sa)
```

### Nebezpečenstvo meniteľných triednych premenných

```py
class Chybne:
    zoznam = []  # POZOR! Spoločný pre všetky inštancie!
    
    def __init__(self, hodnota):
        self.zoznam.append(hodnota)

a = Chybne(1)
b = Chybne(2)
print(a.zoznam)  # [1, 2] - NEOČAKÁVANÉ!
print(b.zoznam)  # [1, 2] - Ten istý zoznam!

# SPRÁVNE riešenie
class Spravne:
    def __init__(self, hodnota):
        self.zoznam = []  # Každá inštancia má vlastný zoznam
        self.zoznam.append(hodnota)

a = Spravne(1)
b = Spravne(2)
print(a.zoznam)  # [1]
print(b.zoznam)  # [2]
```

## `@staticmethod` a `@classmethod`

### Static method - Bez self alebo cls

```py
class Matematika:
    @staticmethod
    def stvorec(x):
        """Statická metóda - nemá prístup ani k triede, ani k inštancii"""
        return x * x
    
    @staticmethod
    def plocha_kruhu(polomer):
        return 3.14159 * polomer * polomer

# Volanie cez triedu
print(Matematika.stvorec(5))  # 25

# Volanie cez inštanciu tiež funguje
m = Matematika()
print(m.plocha_kruhu(10))  # 314.159
```

### Class method - cls parameter

```py
class Datum:
    def __init__(self, rok, mesiac, den):
        self.rok = rok
        self.mesiac = mesiac
        self.den = den
    
    @classmethod
    def z_retazca(cls, datum_retazec):
        """Alternatívny konštruktor - vytvorí objekt Datum z reťazca"""
        rok, mesiac, den = map(int, datum_retazec.split('-'))
        return cls(rok, mesiac, den)
    
    @classmethod
    def dnes(cls):
        """Factory metóda - vráti dnešný dátum"""
        from datetime import date
        today = date.today()
        return cls(today.year, today.month, today.day)
    
    def __str__(self):
        return f"{self.rok}-{self.mesiac:02d}-{self.den:02d}"

# Normálny konštruktor
d1 = Datum(2026, 1, 7)

# Class method ako alternatívny konštruktor
d2 = Datum.z_retazca("2026-03-15")
print(d2)  # 2026-03-15

# Factory metóda
d3 = Datum.dnes()
print(d3)
```

## Špeciálne metódy (Magic Methods)

### Porovnávacie metódy

```py
class Peniaze:
    def __init__(self, suma, mena="HUF"):
        self.suma = suma
        self.mena = mena
    
    def __eq__(self, other):
        """Rovnosť: =="""
        return self.suma == other.suma and self.mena == other.mena
    
    def __lt__(self, other):
        """Menšie ako: <"""
        if self.mena != other.mena:
            raise ValueError("Nie je možné porovnávať rôzne meny")
        return self.suma < other.suma
    
    def __le__(self, other):
        """Menšie alebo rovné: <="""
        return self < other or self == other
    
    def __gt__(self, other):
        """Väčšie ako: >"""
        return not self <= other
    
    def __ge__(self, other):
        """Väčšie alebo rovné: >="""
        return not self < other
    
    def __repr__(self):
        return f"Peniaze({self.suma}, '{self.mena}')"

p1 = Peniaze(1000)
p2 = Peniaze(2000)
p3 = Peniaze(1000)

print(p1 == p3)  # True
print(p1 < p2)   # True
print(p2 > p1)   # True
print(p1 <= p3)  # True
```

### Aritmetické operátory

```py
class Vektor:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        """Sčítanie: +"""
        return Vektor(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        """Odčítanie: -"""
        return Vektor(self.x - other.x, self.y - other.y)
    
    def __mul__(self, skalar):
        """Násobenie skalárom: *"""
        return Vektor(self.x * skalar, self.y * skalar)
    
    def __truediv__(self, skalar):
        """Delenie skalárom: /"""
        return Vektor(self.x / skalar, self.y / skalar)
    
    def __abs__(self):
        """Absolútna hodnota (dĺžka): abs()"""
        return (self.x**2 + self.y**2)**0.5
    
    def __repr__(self):
        return f"Vektor({self.x}, {self.y})"

v1 = Vektor(3, 4)
v2 = Vektor(1, 2)

print(v1 + v2)     # Vektor(4, 6)
print(v1 - v2)     # Vektor(2, 2)
print(v1 * 2)      # Vektor(6, 8)
print(v1 / 2)      # Vektor(1.5, 2.0)
print(abs(v1))     # 5.0
```

### Kontajnerové metódy

```py
class Kniznica:
    def __init__(self):
        self.knihy = []
    
    def pridaj(self, kniha):
        self.knihy.append(kniha)
    
    def __len__(self):
        """Dĺžka: len()"""
        return len(self.knihy)
    
    def __getitem__(self, index):
        """Indexovanie: kniznica[index]"""
        return self.knihy[index]
    
    def __setitem__(self, index, kniha):
        """Priradenie na index: kniznica[index] = kniha"""
        self.knihy[index] = kniha
    
    def __delitem__(self, index):
        """Vymazanie: del kniznica[index]"""
        del self.knihy[index]
    
    def __contains__(self, kniha):
        """Obsahuje: kniha in kniznica"""
        return kniha in self.knihy
    
    def __iter__(self):
        """Iterácia: for kniha in kniznica"""
        return iter(self.knihy)

kniznica = Kniznica()
kniznica.pridaj("1984")
kniznica.pridaj("Zvieracia farma")
kniznica.pridaj("Hviezdy nad Egerom")

print(len(kniznica))           # 3
print(kniznica[0])             # 1984
print("1984" in kniznica)      # True

kniznica[1] = "Brave New World"
for kniha in kniznica:
    print(kniha)
```

## Súkromné a chránené atribúty

### Konvencie názvov

```py
class BankovyUcet:
    def __init__(self, vlastnik, zostatok):
        self.vlastnik = vlastnik              # public
        self._zostatok = zostatok             # protected (konvencia)
        self.__pin = "1234"                   # private (name mangling)
    
    def _interny_vypocet(self):
        """Protected metóda - podľa konvencie len pre dedičnosť"""
        return self._zostatok * 0.05
    
    def __tajna_operacia(self):
        """Private metóda - ťažko prístupná kvôli name mangling"""
        print("Tajná operácia vykonaná")
    
    def vypocet_uroku(self):
        return self._interny_vypocet()

ucet = BankovyUcet("Ján", 100000)

# Public - prístupné pre všetkých
print(ucet.vlastnik)

# Protected - podľa konvencie by sa nemalo používať zvonka (ale funguje)
print(ucet._zostatok)

# Private - name mangling spôsobí premenovanie
# print(ucet.__pin)  # AttributeError
print(ucet._BankovyUcet__pin)  # 1234 - takto je prístupné, ale nerob to!
```

### Name Mangling podrobne

```py
class Test:
    def __init__(self):
        self.public = "Všetci to vidia"
        self._protected = "Podľa konvencie interné použitie"
        self.__private = "Name mangling - ťažko prístupné"
    
    def __private_method(self):
        return "Toto je súkromná metóda"
    
    def public_method(self):
        # V rámci triedy je všetko prístupné
        return self.__private_method()

t = Test()
print(t.public)
print(t._protected)
# print(t.__private)  # AttributeError

# Name mangling: __nazov -> _NazovTriedy__nazov
print(t._Test__private)
print(t._Test__private_method())
```

## Context Manager - príkaz `with`

### Základné použitie

```py
class SpravcaSuborov:
    def __init__(self, nazov_suboru, mod):
        self.nazov_suboru = nazov_suboru
        self.mod = mod
        self.subor = None
    
    def __enter__(self):
        """Vykoná sa na začiatku bloku with"""
        print(f"Otváranie súboru: {self.nazov_suboru}")
        self.subor = open(self.nazov_suboru, self.mod, encoding='utf-8')
        return self.subor
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Vykoná sa na konci bloku with (aj pri chybe)"""
        if self.subor:
            self.subor.close()
            print(f"Súbor zatvorený: {self.nazov_suboru}")
        
        # Ak vrátime False, výnimka sa šíri ďalej
        # Ak vrátime True, výnimka sa potlačí
        return False

# Použitie
with SpravcaSuborov('test.txt', 'w') as f:
    f.write('Ahoj, svet!')
# Súbor sa automaticky zatvorí, aj pri chybe
```

### Praktický príklad - Meranie času

```py
import time

class Casomiera:
    def __enter__(self):
        self.zaciatok = time.time()
        return self
    
    def __exit__(self, *args):
        self.koniec = time.time()
        self.uplynulo = self.koniec - self.zaciatok
        print(f"Čas vykonania: {self.uplynulo:.4f} sekúnd")

# Použitie
with Casomiera():
    # Tu sa vykonáva ľubovoľný kód
    sucet = sum(range(1000000))
    print(f"Súčet: {sucet}")
# Automaticky vypíše čas
```

### Context manager pre databázu

```py
class DatabazovePripojenie:
    def __init__(self, nazov_db):
        self.nazov_db = nazov_db
        self.pripojenie = None
    
    def __enter__(self):
        print(f"Pripájanie: {self.nazov_db}")
        # Tu by bolo skutočné databázové pripojenie
        self.pripojenie = f"Pripojenie: {self.nazov_db}"
        return self.pripojenie
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print(f"Nastala chyba: {exc_val}")
            print("Rollback...")
        else:
            print("Commit...")
        
        print(f"Odpojenie: {self.nazov_db}")
        return False  # Chyba sa šíri ďalej

# Použitie
with DatabazovePripojenie("mydb.db") as db:
    print(f"Práca s databázou: {db}")
    # Operácie...
```

## `@dataclass` - Zjednodušené triedy

```py
from dataclasses import dataclass, field
from typing import List

# Tradičná trieda
class StaraOsoba:
    def __init__(self, meno, vek, email):
        self.meno = meno
        self.vek = vek
        self.email = email
    
    def __repr__(self):
        return f"StaraOsoba(meno='{self.meno}', vek={self.vek}, email='{self.email}')"
    
    def __eq__(self, other):
        return (self.meno == other.meno and 
                self.vek == other.vek and 
                self.email == other.email)

# Dataclass - oveľa jednoduchšie!
@dataclass
class Osoba:
    meno: str
    vek: int
    email: str

p1 = Osoba("Ján", 25, "jan@example.com")
p2 = Osoba("Ján", 25, "jan@example.com")

print(p1)           # Osoba(meno='Ján', vek=25, email='jan@example.com')
print(p1 == p2)     # True (automatický __eq__)
```

### Pokročilé funkcie dataclass

```py
from dataclasses import dataclass, field
from typing import List

@dataclass
class Produkt:
    nazov: str
    cena: float
    na_sklade: int = 0  # Predvolená hodnota
    stitky: List[str] = field(default_factory=list)  # Meniteľná predvolená hodnota
    
    def __post_init__(self):
        """Vykoná sa po inicializácii"""
        if self.cena < 0:
            raise ValueError("Cena nemôže byť záporná")

@dataclass(order=True)  # Generovanie porovnávacích metód
class Student:
    sort_index: float = field(init=False, repr=False)  # Použité na triedenie
    meno: str
    priemer: float
    
    def __post_init__(self):
        self.sort_index = self.priemer

# Použitie
p = Produkt("Laptop", 250000, 10, ["elektronika", "počítač"])
print(p)

studenti = [
    Student("Anna", 4.5),
    Student("Béla", 3.8),
    Student("Cecil", 4.9)
]

# Triedenie funguje automaticky (podľa priemeru)
for s in sorted(studenti, reverse=True):
    print(s)
```

### Dataclass frozen (nemeniteľný)

```py
from dataclasses import dataclass

@dataclass(frozen=True)
class Bod:
    x: float
    y: float

b = Bod(1.0, 2.0)
print(b.x)
# b.x = 3.0  # FrozenInstanceError - nie je možné meniť!
```

## Abstraktné triedy (ABC)

### Základné použitie

```py
from abc import ABC, abstractmethod

class Zviera(ABC):
    """Abstraktná rodičovská trieda - nie je možné vytvoriť inštanciu"""
    
    def __init__(self, meno):
        self.meno = meno
    
    @abstractmethod
    def zvuk(self):
        """Túto metódu musia implementovať všetky potomky"""
        pass
    
    @abstractmethod
    def pohyb(self):
        """Toto tiež musí byť implementované"""
        pass
    
    def predstav_sa(self):
        """Toto je už konkrétna metóda, nie je povinné prepísať"""
        print(f"Ahoj, som {self.meno}!")

class Pes(Zviera):
    def zvuk(self):
        return "Hav hav!"
    
    def pohyb(self):
        return "Behá na štyroch nohách"

class Vtak(Zviera):
    def zvuk(self):
        return "Čvirik čvirik!"
    
    def pohyb(self):
        return "Lieta vo vzduchu"

# zviera = Zviera("Niečo")  # TypeError: Can't instantiate abstract class
pes = Pes("Dunčo")
vtak = Vtak("Čipko")

print(pes.zvuk())        # Hav hav!
pes.predstav_sa()        # Ahoj, som Dunčo!
print(vtak.pohyb())      # Lieta vo vzduchu
```

### Abstraktné vlastnosti

```py
from abc import ABC, abstractmethod

class Tvar(ABC):
    @property
    @abstractmethod
    def plocha(self):
        """Abstraktná property - povinné implementovať"""
        pass
    
    @property
    @abstractmethod
    def obvod(self):
        pass

class Obdlznik(Tvar):
    def __init__(self, sirka, vyska):
        self.sirka = sirka
        self.vyska = vyska
    
    @property
    def plocha(self):
        return self.sirka * self.vyska
    
    @property
    def obvod(self):
        return 2 * (self.sirka + self.vyska)

class Kruh(Tvar):
    def __init__(self, polomer):
        self.polomer = polomer
    
    @property
    def plocha(self):
        return 3.14159 * self.polomer ** 2
    
    @property
    def obvod(self):
        return 2 * 3.14159 * self.polomer

obdlznik = Obdlznik(5, 3)
print(f"Plocha: {obdlznik.plocha}")    # 15
print(f"Obvod: {obdlznik.obvod}")      # 16

kruh = Kruh(5)
print(f"Plocha: {kruh.plocha:.2f}")    # 78.54
print(f"Obvod: {kruh.obvod:.2f}")      # 31.42
```

## Composition vs Inheritance (Zloženie vs Dedičnosť)

### Dedičnosť (IS-A vzťah)

```py
class Vozidlo:
    def __init__(self, rychlost):
        self.rychlost = rychlost
    
    def pohyb(self):
        return f"Pohybuje sa rýchlosťou {self.rychlost} km/h"

class Auto(Vozidlo):
    """Auto IS-A Vozidlo - dedičnosť je vhodná"""
    def __init__(self, rychlost, znacka):
        super().__init__(rychlost)
        self.znacka = znacka
```

### Zloženie (HAS-A vzťah)

```py
class Motor:
    def __init__(self, konske_sily):
        self.konske_sily = konske_sily
    
    def nastartuj(self):
        return f"{self.konske_sily} HP motor naštartovaný"

class Koleso:
    def __init__(self, velkost):
        self.velkost = velkost
    
    def toci_sa(self):
        return f"{self.velkost}\" koleso sa točí"

class Auto:
    """Auto HAS-A Motor a Koleso - zloženie je vhodné"""
    def __init__(self, znacka, konske_sily_motora, velkost_kolesa):
        self.znacka = znacka
        self.motor = Motor(konske_sily_motora)  # Zloženie
        self.kolesa = [Koleso(velkost_kolesa) for _ in range(4)]  # Zloženie
    
    def nastartuj(self):
        print(f"{self.znacka} auto:")
        print(self.motor.nastartuj())
        for i, koleso in enumerate(self.kolesa, 1):
            print(f"{i}. {koleso.toci_sa()}")

auto = Auto("Toyota", 150, 17)
auto.nastartuj()
```

### Praktický príklad - Používateľ a Oprávnenia

```py
# ZLE: Použitie dedičnosti
class AdminPouzivatel(Pouzivatel, Admin, Moderator):
    pass  # Chaos viacnásobnej dedičnosti

# DOBRE: Použitie zloženia
class Opravnenie:
    def __init__(self, nazov, popis):
        self.nazov = nazov
        self.popis = popis

class Pouzivatel:
    def __init__(self, meno):
        self.meno = meno
        self.opravnenia = []
    
    def pridaj_opravnenie(self, opravnenie):
        self.opravnenia.append(opravnenie)
    
    def ma_opravnenie(self, nazov_opravnenia):
        return any(opr.nazov == nazov_opravnenia for opr in self.opravnenia)

# Použitie
user = Pouzivatel("Ján")
user.pridaj_opravnenie(Opravnenie("citanie", "Čítanie obsahu"))
user.pridaj_opravnenie(Opravnenie("pisanie", "Písanie obsahu"))

if user.ma_opravnenie("pisanie"):
    print("Používateľ môže písať")
```

## Úplný praktický príklad - Webshop

```py
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import List
from datetime import datetime

@dataclass
class Produkt:
    nazov: str
    cena: float
    sklad: int
    
    def dostupny(self, mnozstvo: int) -> bool:
        return self.sklad >= mnozstvo
    
    def zniz_sklad(self, mnozstvo: int):
        if self.dostupny(mnozstvo):
            self.sklad -= mnozstvo
        else:
            raise ValueError("Nedostatok na sklade")

class Platba(ABC):
    @abstractmethod
    def zaplat(self, suma: float) -> bool:
        pass

class PlatbaKartou(Platba):
    def __init__(self, cislo_karty):
        self.cislo_karty = cislo_karty
    
    def zaplat(self, suma: float) -> bool:
        print(f"Platba kartou: {suma} Ft z karty {self.cislo_karty}")
        return True

class PlatbaPrevodom(Platba):
    def __init__(self, cislo_uctu):
        self.cislo_uctu = cislo_uctu
    
    def zaplat(self, suma: float) -> bool:
        print(f"Prevod: {suma} Ft na účet {self.cislo_uctu}")
        return True

@dataclass
class PolozkaKosika:
    produkt: Produkt
    mnozstvo: int = 1
    
    @property
    def medzisucet(self) -> float:
        return self.produkt.cena * self.mnozstvo

class Kosik:
    def __init__(self):
        self._polozky: List[PolozkaKosika] = []
    
    def pridaj(self, produkt: Produkt, mnozstvo: int = 1):
        if not produkt.dostupny(mnozstvo):
            raise ValueError(f"Nedostatok {produkt.nazov} na sklade")
        
        # Skontroluj, či produkt už je v košíku
        for polozka in self._polozky:
            if polozka.produkt == produkt:
                polozka.mnozstvo += mnozstvo
                return
        
        self._polozky.append(PolozkaKosika(produkt, mnozstvo))
    
    @property
    def celkova_suma(self) -> float:
        return sum(polozka.medzisucet for polozka in self._polozky)
    
    def objednavka(self, sposob_platby: Platba) -> bool:
        if not self._polozky:
            raise ValueError("Košík je prázdny")
        
        # Zníženie skladu
        for polozka in self._polozky:
            polozka.produkt.zniz_sklad(polozka.mnozstvo)
        
        # Platba
        uspech = sposob_platby.zaplat(self.celkova_suma)
        
        if uspech:
            print(f"\nObjednávka úspešná! Celkom: {self.celkova_suma} Ft")
            self._polozky.clear()
        
        return uspech
    
    def __len__(self):
        return sum(polozka.mnozstvo for polozka in self._polozky)
    
    def __str__(self):
        if not self._polozky:
            return "Košík je prázdny"
        
        vysledok = "Obsah košíka:\n"
        for polozka in self._polozky:
            vysledok += f"  {polozka.produkt.nazov} x {polozka.mnozstvo} = {polozka.medzisucet} Ft\n"
        vysledok += f"Celková suma: {self.celkova_suma} Ft"
        return vysledok

# Použitie
laptop = Produkt("Laptop", 250000, 5)
mys = Produkt("Myš", 5000, 20)
klavesnica = Produkt("Klávesnica", 15000, 10)

kosik = Kosik()
kosik.pridaj(laptop, 1)
kosik.pridaj(mys, 2)
kosik.pridaj(klavesnica, 1)

print(kosik)
print(f"\nPočet položiek: {len(kosik)}")

platba = PlatbaKartou("1234-5678-9012-3456")
kosik.objednavka(platba)

print(f"\nLaptop zostávajúci sklad: {laptop.sklad}")
```

## Úlohy

1. Vytvor triedu `PrevodnikTeploty` s použitím `@property`, ktorá dokáže prepínať medzi Celsius, Fahrenheit a Kelvin.

2. Implementuj triedu `Penazenka`, ktorá dokáže pracovať s rôznymi menami. Použij magic methods na sčítanie a odčítanie.

3. Vytvor context manager `Zapisovac`, ktorý do súboru zaznamenáva čas vykonania a prípadné chyby.

4. Vytvor abstraktnú triedu `Tvar` a implementuj z nej triedy `Trojuholnik`, `Stvorec` a `Kruh`.

5. Navrhni systém `Kniznica` s použitím zloženia, kde `Kniznica` obsahuje objekty `Kniha`, objekty `Pozicka` a objekty `Citatel`.
