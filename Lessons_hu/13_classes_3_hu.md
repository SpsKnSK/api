# Osztályok - Mélyebb ismeretek

Ez a fejezet már komolyan belemegy az objektumorientált programozás részleteibe. Azoknak ajánlott, akik komolyabban foglalkoznak a programozással.

## `@property` dekorátor - Getter és Setter

A `@property` dekorátor segítségével kontrollálhatjuk, hogyan férhetünk hozzá egy attribútumhoz, és hogyan állíthatjuk be annak értékét.

### Egyszerű property

```py
class Hőmérő:
    def __init__(self):
        self._celsius = 0
    
    @property
    def celsius(self):
        """Getter - celsius érték lekérdezése"""
        return self._celsius
    
    @celsius.setter
    def celsius(self, érték):
        """Setter - celsius érték beállítása ellenőrzéssel"""
        if érték < -273.15:
            raise ValueError("A hőmérséklet nem lehet alacsonyabb mint -273.15°C")
        self._celsius = érték
    
    @property
    def fahrenheit(self):
        """Fahrenheit érték számítása celsius-ból"""
        return self._celsius * 9/5 + 32
    
    @fahrenheit.setter
    def fahrenheit(self, érték):
        """Fahrenheit beállítása, celsius-ra váltás"""
        self.celsius = (érték - 32) * 5/9

# Használat
h = Hőmérő()
h.celsius = 25
print(f"{h.celsius}°C = {h.fahrenheit}°F")  # 25°C = 77.0°F

h.fahrenheit = 100
print(f"{h.celsius}°C = {h.fahrenheit}°F")  # 37.77°C = 100.0°F

# h.celsius = -300  # ValueError: A hőmérséklet nem lehet alacsonyabb mint -273.15°C
```

### Property deleter

```py
class Felhasználó:
    def __init__(self, név, jelszó):
        self._név = név
        self._jelszó = jelszó
    
    @property
    def jelszó(self):
        raise AttributeError("A jelszó nem olvasható!")
    
    @jelszó.setter
    def jelszó(self, új_jelszó):
        if len(új_jelszó) < 8:
            raise ValueError("A jelszónak legalább 8 karakter hosszúnak kell lennie")
        self._jelszó = új_jelszó
        print("Jelszó sikeresen megváltoztatva")
    
    @jelszó.deleter
    def jelszó(self):
        print("Jelszó törölve, alapértelmezett jelszó beállítva")
        self._jelszó = "default123"

user = Felhasználó("János", "titkos123")
user.jelszó = "újjelszó2024"  # Jelszó sikeresen megváltoztatva
# print(user.jelszó)  # AttributeError: A jelszó nem olvasható!
del user.jelszó  # Jelszó törölve, alapértelmezett jelszó beállítva
```

## Osztályváltozók vs Példányváltozók

### Különbségek

```py
class Kutya:
    # Osztályváltozó - minden példány között közös
    faj = "Canis familiaris"
    egyedek_száma = 0
    
    def __init__(self, név, kor):
        # Példányváltozók - minden példánynak saját
        self.név = név
        self.kor = kor
        # Osztályváltozó módosítása
        Kutya.egyedek_száma += 1
    
    @classmethod
    def összes_kutya(cls):
        return cls.egyedek_száma

# Osztályváltozó elérhető osztályon keresztül
print(Kutya.faj)  # Canis familiaris

# Példányok létrehozása
buddy = Kutya("Buddy", 5)
max_kutya = Kutya("Max", 3)

print(buddy.faj)  # Canis familiaris
print(max_kutya.faj)  # Canis familiaris
print(Kutya.egyedek_száma)  # 2

# Osztályváltozó módosítása - minden példányra hat
Kutya.faj = "Canis lupus familiaris"
print(buddy.faj)  # Canis lupus familiaris

# Példányváltozó létrehozása ugyanazzal a névvel
buddy.faj = "Csak Buddy változata"
print(buddy.faj)  # Csak Buddy változata
print(max_kutya.faj)  # Canis lupus familiaris (nem változott)
```

### Mutable osztályváltozók veszélyei

```py
class Hibás:
    lista = []  # VIGYÁZAT! Közös minden példány között!
    
    def __init__(self, érték):
        self.lista.append(érték)

a = Hibás(1)
b = Hibás(2)
print(a.lista)  # [1, 2] - VÁRATLÁN!
print(b.lista)  # [1, 2] - Ugyanaz a lista!

# HELYES megoldás
class Helyes:
    def __init__(self, érték):
        self.lista = []  # Minden példánynak saját listája
        self.lista.append(érték)

a = Helyes(1)
b = Helyes(2)
print(a.lista)  # [1]
print(b.lista)  # [2]
```

## `@staticmethod` és `@classmethod`

### Static method - Nincs self vagy cls

```py
class Matematika:
    @staticmethod
    def négyzet(x):
        """Statikus metódus - nem fér hozzá sem az osztályhoz, sem a példányhoz"""
        return x * x
    
    @staticmethod
    def kör_terület(sugár):
        return 3.14159 * sugár * sugár

# Hívás osztályon keresztül
print(Matematika.négyzet(5))  # 25

# Hívás példányon keresztül is működik
m = Matematika()
print(m.kör_terület(10))  # 314.159
```

### Class method - cls paraméter

```py
class Dátum:
    def __init__(self, év, hó, nap):
        self.év = év
        self.hó = hó
        self.nap = nap
    
    @classmethod
    def string_ből(cls, dátum_string):
        """Alternatív konstruktor - string-ből hoz létre Dátum objektumot"""
        év, hó, nap = map(int, dátum_string.split('-'))
        return cls(év, hó, nap)
    
    @classmethod
    def ma(cls):
        """Factory metódus - mai dátumot ad vissza"""
        from datetime import date
        today = date.today()
        return cls(today.year, today.month, today.day)
    
    def __str__(self):
        return f"{self.év}-{self.hó:02d}-{self.nap:02d}"

# Normál konstruktor
d1 = Dátum(2026, 1, 7)

# Class method mint alternatív konstruktor
d2 = Dátum.string_ből("2026-03-15")
print(d2)  # 2026-03-15

# Factory metódus
d3 = Dátum.ma()
print(d3)
```

## Speciális metódusok (Magic Methods)

### Összehasonlító metódusok

```py
class Pénz:
    def __init__(self, összeg, pénznem="HUF"):
        self.összeg = összeg
        self.pénznem = pénznem
    
    def __eq__(self, other):
        """Egyenlőség: =="""
        return self.összeg == other.összeg and self.pénznem == other.pénznem
    
    def __lt__(self, other):
        """Kisebb mint: <"""
        if self.pénznem != other.pénznem:
            raise ValueError("Különböző pénznemeket nem lehet összehasonlítani")
        return self.összeg < other.összeg
    
    def __le__(self, other):
        """Kisebb vagy egyenlő: <="""
        return self < other or self == other
    
    def __gt__(self, other):
        """Nagyobb mint: >"""
        return not self <= other
    
    def __ge__(self, other):
        """Nagyobb vagy egyenlő: >="""
        return not self < other
    
    def __repr__(self):
        return f"Pénz({self.összeg}, '{self.pénznem}')"

p1 = Pénz(1000)
p2 = Pénz(2000)
p3 = Pénz(1000)

print(p1 == p3)  # True
print(p1 < p2)   # True
print(p2 > p1)   # True
print(p1 <= p3)  # True
```

### Aritmetikai operátorok

```py
class Vektor:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        """Összeadás: +"""
        return Vektor(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        """Kivonás: -"""
        return Vektor(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        """Szorzás skalárral: *"""
        return Vektor(self.x * scalar, self.y * scalar)
    
    def __truediv__(self, scalar):
        """Osztás skalárral: /"""
        return Vektor(self.x / scalar, self.y / scalar)
    
    def __abs__(self):
        """Abszolút érték (hossz): abs()"""
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

### Konténer metódusok

```py
class Könyvtár:
    def __init__(self):
        self.könyvek = []
    
    def hozzáad(self, könyv):
        self.könyvek.append(könyv)
    
    def __len__(self):
        """Hossz: len()"""
        return len(self.könyvek)
    
    def __getitem__(self, index):
        """Indexelés: könyvtár[index]"""
        return self.könyvek[index]
    
    def __setitem__(self, index, könyv):
        """Értékadás indexen: könyvtár[index] = könyv"""
        self.könyvek[index] = könyv
    
    def __delitem__(self, index):
        """Törlés: del könyvtár[index]"""
        del self.könyvek[index]
    
    def __contains__(self, könyv):
        """Tartalmazás: könyv in könyvtár"""
        return könyv in self.könyvek
    
    def __iter__(self):
        """Iterálás: for könyv in könyvtár"""
        return iter(self.könyvek)

könyvtár = Könyvtár()
könyvtár.hozzáad("1984")
könyvtár.hozzáad("Állatfarm")
könyvtár.hozzáad("Egri csillagok")

print(len(könyvtár))           # 3
print(könyvtár[0])             # 1984
print("1984" in könyvtár)      # True

könyvtár[1] = "Brave New World"
for könyv in könyvtár:
    print(könyv)
```

## Private és Protected attribútumok

### Névkonvenciók

```py
class BankSzámla:
    def __init__(self, tulajdonos, egyenleg):
        self.tulajdonos = tulajdonos           # public
        self._egyenleg = egyenleg              # protected (konvenció)
        self.__pin = "1234"                    # private (name mangling)
    
    def _belső_számítás(self):
        """Protected metódus - konvenció szerint csak öröklésnél használandó"""
        return self._egyenleg * 0.05
    
    def __titkos_művelet(self):
        """Private metódus - name mangling miatt nehezen hozzáférhető"""
        print("Titkos művelet végrehajtva")
    
    def kamat_számítás(self):
        return self._belső_számítás()

számla = BankSzámla("János", 100000)

# Public - bárki hozzáférhet
print(számla.tulajdonos)

# Protected - konvenció szerint ne használd kívülről (de működik)
print(számla._egyenleg)

# Private - name mangling miatt átnevezve
# print(számla.__pin)  # AttributeError
print(számla._BankSzámla__pin)  # 1234 - így elérhető, de ne csináld!
```

### Name Mangling részletesen

```py
class Test:
    def __init__(self):
        self.public = "Mindenki láthatja"
        self._protected = "Konvenció szerint belső használatra"
        self.__private = "Name mangling - nehezen elérhető"
    
    def __private_method(self):
        return "Ez egy privát metódus"
    
    def public_method(self):
        # Osztályon belül minden elérhető
        return self.__private_method()

t = Test()
print(t.public)
print(t._protected)
# print(t.__private)  # AttributeError

# Name mangling: __név -> _OsztályNév__név
print(t._Test__private)
print(t._Test__private_method())
```

## Context Manager - `with` utasítás

### Alapvető használat

```py
class Fájlkezelő:
    def __init__(self, fájlnév, mód):
        self.fájlnév = fájlnév
        self.mód = mód
        self.fájl = None
    
    def __enter__(self):
        """A with blokk elején fut le"""
        print(f"Fájl megnyitása: {self.fájlnév}")
        self.fájl = open(self.fájlnév, self.mód, encoding='utf-8')
        return self.fájl
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """A with blokk végén fut le (még hiba esetén is)"""
        if self.fájl:
            self.fájl.close()
            print(f"Fájl bezárva: {self.fájlnév}")
        
        # Ha False-t adunk vissza, a kivétel tovább terjed
        # Ha True-t adunk vissza, a kivétel elnyomódik
        return False

# Használat
with Fájlkezelő('teszt.txt', 'w') as f:
    f.write('Hello, World!')
# A fájl automatikusan bezáródik, még hiba esetén is
```

### Gyakorlati példa - Időmérő

```py
import time

class Időmérő:
    def __enter__(self):
        self.kezdés = time.time()
        return self
    
    def __exit__(self, *args):
        self.vég = time.time()
        self.eltelt = self.vég - self.kezdés
        print(f"Végrehajtási idő: {self.eltelt:.4f} másodperc")

# Használat
with Időmérő():
    # Itt bármi végrehajtható
    összeg = sum(range(1000000))
    print(f"Összeg: {összeg}")
# Automatikusan kiírja az időt
```

### Context manager adatbázishoz

```py
class AdatbázisKapcsolat:
    def __init__(self, db_név):
        self.db_név = db_név
        self.kapcsolat = None
    
    def __enter__(self):
        print(f"Kapcsolódás: {self.db_név}")
        # Itt valós adatbázis kapcsolat lenne
        self.kapcsolat = f"Kapcsolat: {self.db_név}"
        return self.kapcsolat
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print(f"Hiba történt: {exc_val}")
            print("Rollback...")
        else:
            print("Commit...")
        
        print(f"Kapcsolat bontása: {self.db_név}")
        return False  # Hiba továbbterjed

# Használat
with AdatbázisKapcsolat("mydb.db") as db:
    print(f"Munka az adatbázissal: {db}")
    # Művletek...
```

## `@dataclass` - Egyszerűsített osztályok

```py
from dataclasses import dataclass, field
from typing import List

# Hagyományos osztály
class RegiSzemély:
    def __init__(self, név, kor, email):
        self.név = név
        self.kor = kor
        self.email = email
    
    def __repr__(self):
        return f"RegiSzemély(név='{self.név}', kor={self.kor}, email='{self.email}')"
    
    def __eq__(self, other):
        return (self.név == other.név and 
                self.kor == other.kor and 
                self.email == other.email)

# Dataclass - sokkal egyszerűbb!
@dataclass
class Személy:
    név: str
    kor: int
    email: str

p1 = Személy("János", 25, "janos@example.com")
p2 = Személy("János", 25, "janos@example.com")

print(p1)           # Személy(név='János', kor=25, email='janos@example.com')
print(p1 == p2)     # True (automatikus __eq__)
```

### Dataclass haladó funkciók

```py
from dataclasses import dataclass, field
from typing import List

@dataclass
class Termék:
    név: str
    ár: float
    raktáron: int = 0  # Alapértelmezett érték
    címkék: List[str] = field(default_factory=list)  # Mutable alapértelmezett
    
    def __post_init__(self):
        """Inicializálás után fut le"""
        if self.ár < 0:
            raise ValueError("Az ár nem lehet negatív")

@dataclass(order=True)  # Összehasonlító metódusok generálása
class Diák:
    sort_index: float = field(init=False, repr=False)  # Rendezéshez használt
    név: str
    átlag: float
    
    def __post_init__(self):
        self.sort_index = self.átlag

# Használat
t = Termék("Laptop", 250000, 10, ["elektronika", "számítógép"])
print(t)

diákok = [
    Diák("Anna", 4.5),
    Diák("Béla", 3.8),
    Diák("Cecil", 4.9)
]

# Rendezés automatikusan működik (átlag szerint)
for d in sorted(diákok, reverse=True):
    print(d)
```

### Dataclass frozen (immutable)

```py
from dataclasses import dataclass

@dataclass(frozen=True)
class Pont:
    x: float
    y: float

p = Pont(1.0, 2.0)
print(p.x)
# p.x = 3.0  # FrozenInstanceError - nem módosítható!
```

## Absztrakt osztályok (ABC)

### Alapvető használat

```py
from abc import ABC, abstractmethod

class Állat(ABC):
    """Absztrakt ősosztály - nem példányosítható"""
    
    def __init__(self, név):
        self.név = név
    
    @abstractmethod
    def hangot_ad(self):
        """Ezt a metódust minden leszármazottnak implementálnia kell"""
        pass
    
    @abstractmethod
    def mozog(self):
        """Ezt is implementálni kell"""
        pass
    
    def bemutatkozik(self):
        """Ez már konkrét metódus, nem kötelező felülírni"""
        print(f"Szia, én {self.név} vagyok!")

class Kutya(Állat):
    def hangot_ad(self):
        return "Vau vau!"
    
    def mozog(self):
        return "Futkos négy lábon"

class Madár(Állat):
    def hangot_ad(self):
        return "Csirip csirip!"
    
    def mozog(self):
        return "Repül a levegőben"

# állat = Állat("Valami")  # TypeError: Can't instantiate abstract class
kutya = Kutya("Bodri")
madár = Madár("Csöpi")

print(kutya.hangot_ad())    # Vau vau!
kutya.bemutatkozik()        # Szia, én Bodri vagyok!
print(madár.mozog())        # Repül a levegőben
```

### Absztrakt tulajdonságok

```py
from abc import ABC, abstractmethod

class Forma(ABC):
    @property
    @abstractmethod
    def terület(self):
        """Absztrakt property - kötelező implementálni"""
        pass
    
    @property
    @abstractmethod
    def kerület(self):
        pass

class Téglalap(Forma):
    def __init__(self, szélesség, magasság):
        self.szélesség = szélesség
        self.magasság = magasság
    
    @property
    def terület(self):
        return self.szélesség * self.magasság
    
    @property
    def kerület(self):
        return 2 * (self.szélesség + self.magasság)

class Kör(Forma):
    def __init__(self, sugár):
        self.sugár = sugár
    
    @property
    def terület(self):
        return 3.14159 * self.sugár ** 2
    
    @property
    def kerület(self):
        return 2 * 3.14159 * self.sugár

téglalap = Téglalap(5, 3)
print(f"Terület: {téglalap.terület}")    # 15
print(f"Kerület: {téglalap.kerület}")    # 16

kör = Kör(5)
print(f"Terület: {kör.terület:.2f}")     # 78.54
print(f"Kerület: {kör.kerület:.2f}")     # 31.42
```

## Composition vs Inheritance (Összetétel vs Öröklés)

### Öröklés (IS-A kapcsolat)

```py
class Jármű:
    def __init__(self, sebesség):
        self.sebesség = sebesség
    
    def mozog(self):
        return f"Mozog {self.sebesség} km/h sebességgel"

class Autó(Jármű):
    """Autó IS-A Jármű - öröklés megfelelő"""
    def __init__(self, sebesség, márka):
        super().__init__(sebesség)
        self.márka = márka
```

### Összetétel (HAS-A kapcsolat)

```py
class Motor:
    def __init__(self, lóerő):
        self.lóerő = lóerő
    
    def beindít(self):
        return f"{self.lóerő} LE motor beindult"

class Kerék:
    def __init__(self, méret):
        self.méret = méret
    
    def forog(self):
        return f"{self.méret}\" kerék forog"

class Autó:
    """Autó HAS-A Motor és Kerék - összetétel megfelelő"""
    def __init__(self, márka, motor_lóerő, kerék_méret):
        self.márka = márka
        self.motor = Motor(motor_lóerő)  # Összetétel
        self.kerekek = [Kerék(kerék_méret) for _ in range(4)]  # Összetétel
    
    def indít(self):
        print(f"{self.márka} autó:")
        print(self.motor.beindít())
        for i, kerék in enumerate(self.kerekek, 1):
            print(f"{i}. {kerék.forog()}")

autó = Autó("Toyota", 150, 17)
autó.indít()
```

### Gyakorlati példa - Felhasználó és Jogosultságok

```py
# ROSSZ: Öröklés használata
class AdminFelhasználó(Felhasználó, Admin, Moderátor):
    pass  # Többszörös öröklés zűrzavara

# JÓ: Összetétel használata
class Jogosultság:
    def __init__(self, név, leírás):
        self.név = név
        self.leírás = leírás

class Felhasználó:
    def __init__(self, név):
        self.név = név
        self.jogosultságok = []
    
    def jogosultság_hozzáad(self, jog):
        self.jogosultságok.append(jog)
    
    def van_jogosultsága(self, jog_név):
        return any(jog.név == jog_név for jog in self.jogosultságok)

# Használat
user = Felhasználó("János")
user.jogosultság_hozzáad(Jogosultság("olvasás", "Tartalom olvasása"))
user.jogosultság_hozzáad(Jogosultság("írás", "Tartalom írása"))

if user.van_jogosultsága("írás"):
    print("A felhasználó írhat")
```

## Teljes gyakorlati példa - Webshop

```py
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import List
from datetime import datetime

@dataclass
class Termék:
    név: str
    ár: float
    készlet: int
    
    def elérhető(self, mennyiség: int) -> bool:
        return self.készlet >= mennyiség
    
    def készlet_csökkent(self, mennyiség: int):
        if self.elérhető(mennyiség):
            self.készlet -= mennyiség
        else:
            raise ValueError("Nincs elegendő készlet")

class Fizetés(ABC):
    @abstractmethod
    def fizet(self, összeg: float) -> bool:
        pass

class BankkártyásFizetés(Fizetés):
    def __init__(self, kártya_szám):
        self.kártya_szám = kártya_szám
    
    def fizet(self, összeg: float) -> bool:
        print(f"Bankkártyás fizetés: {összeg} Ft a {self.kártya_szám} kártyáról")
        return True

class ÁtutalásFizetés(Fizetés):
    def __init__(self, számlaszám):
        self.számlaszám = számlaszám
    
    def fizet(self, összeg: float) -> bool:
        print(f"Átutalás: {összeg} Ft a {self.számlaszám} számlára")
        return True

@dataclass
class KosárTétel:
    termék: Termék
    mennyiség: int = 1
    
    @property
    def részösszeg(self) -> float:
        return self.termék.ár * self.mennyiség

class Kosár:
    def __init__(self):
        self._tételek: List[KosárTétel] = []
    
    def hozzáad(self, termék: Termék, mennyiség: int = 1):
        if not termék.elérhető(mennyiség):
            raise ValueError(f"Nincs elegendő {termék.név} készleten")
        
        # Ellenőrizzük, van-e már ilyen termék
        for tétel in self._tételek:
            if tétel.termék == termék:
                tétel.mennyiség += mennyiség
                return
        
        self._tételek.append(KosárTétel(termék, mennyiség))
    
    @property
    def végösszeg(self) -> float:
        return sum(tétel.részösszeg for tétel in self._tételek)
    
    def megrendelés(self, fizetési_mód: Fizetés) -> bool:
        if not self._tételek:
            raise ValueError("A kosár üres")
        
        # Készlet csökkentése
        for tétel in self._tételek:
            tétel.termék.készlet_csökkent(tétel.mennyiség)
        
        # Fizetés
        siker = fizetési_mód.fizet(self.végösszeg)
        
        if siker:
            print(f"\nMegrendelés sikeres! Összesen: {self.végösszeg} Ft")
            self._tételek.clear()
        
        return siker
    
    def __len__(self):
        return sum(tétel.mennyiség for tétel in self._tételek)
    
    def __str__(self):
        if not self._tételek:
            return "Kosár üres"
        
        result = "Kosár tartalma:\n"
        for tétel in self._tételek:
            result += f"  {tétel.termék.név} x {tétel.mennyiség} = {tétel.részösszeg} Ft\n"
        result += f"Végösszeg: {self.végösszeg} Ft"
        return result

# Használat
laptop = Termék("Laptop", 250000, 5)
egér = Termék("Egér", 5000, 20)
billentyűzet = Termék("Billentyűzet", 15000, 10)

kosár = Kosár()
kosár.hozzáad(laptop, 1)
kosár.hozzáad(egér, 2)
kosár.hozzáad(billentyűzet, 1)

print(kosár)
print(f"\nTételek száma: {len(kosár)}")

fizetés = BankkártyásFizetés("1234-5678-9012-3456")
kosár.megrendelés(fizetés)

print(f"\nLaptop maradék készlet: {laptop.készlet}")
```

## Feladatok

1. Készíts egy `HőmérsékletÁtalakító` osztályt `@property` használatával, amely Celsius, Fahrenheit és Kelvin között is tud váltani.

2. Implementálj egy `Pénztárca` osztályt, amely különböző valuták kezelésére képes. Használd a magic methodsot az összeadáshoz és kivonáshoz.

3. Készíts egy `Naplózó` context managert, amely fájlba naplózza a végrehajtási időt és esetleges hibákat.

4. Hozz létre egy `Alakzat` absztrakt osztályt és implementálj belőle `Háromszög`, `Négyzet` és `Kör` osztályokat.

5. Tervezz egy `Könyvtár` rendszert composition használatával, ahol a `Könyvtár` tartalmaz `Könyv` objektumokat, `Kölcsönzés` objektumokat és `Olvasó` objektumokat.
