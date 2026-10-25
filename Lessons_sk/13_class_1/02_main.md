[Späť na mapu](../00_Mapa_sk.md)

# Triedy, vlastné/zložené dátový typy `class`

Doposial sme sa stretli a pracovali s dátovými typmi ako `int`, `float`, `str`, `random`, `list`, `dict`, ale teraz sme schopní ísť dalej a definovat si vlastné dátový typ.

S `class` príkazom definujeme, hovoríme Pythonu, ako by sme chceli, aby náš vlastné dátový typ vyzeral:
- s akými vlastnostami (attributes, property) by mal byt vybavený -> co **má**
- s akými funkciami by mal byt vybavený -> co vie **robit**

`class` je akýsi **návrh**, ako by sme chceli, aby vyzerali **objekty**, **inštancie**, ktorý z neho vytvoríme.

> **Objekt** alebo **inštancia** je súhrn dát, ktorý je reálne uložené v pamäti. Premenná ukazuje na táto konkrétnu adresu a tak urcuje alebo mení jej hodnotu.

Definovanie triedy pomocou príkazu `class`. V nasledujúcom príklade vytvárame návrh triedy, ktorý sa volá `MyClass` a má vlastnost `x`:

```py
class MyClass:
  x = 5
```

Ak chceme z tejto triedy, návrhu, vytvorit objekt, môžeme to urobit nasledovne:

```py
p1 = MyClass()
print(p1.x)
```

S triedou ešte nevieme pracovat (okrem niekoľkých výnimiek), z nej musíme vytvorit objekt, inštanciu.

## Macka
Môžeme si to predstavit aj tak, že v prírode je **macka**, vieme, že je obvykle chlpatá, má 4 nohy, má meno, mňauká, mazná sa, spí, atd. - toto je návrh na "výrobu" macky. Ale ak už máme konkrétnu macku u nás doma, alebo v susedstve (Murko, Labka, Belka, Cilka), už pre nu udelujeme konkrétne vlastnosti.

```mermaid
classDiagram
    class Macka {
        -str Meno
        -float PocetNoh
        -str Farba
        +__init__(meno, pocetNoh, farba)
        +PredstavSa()
    }
    
    class mojaMacka {
        Meno = "Belka"
        PocetNoh = 3.5
        Farba = "strieborna"
    }
    
    Macka <|.. mojaMacka : <<instance>>
    
    note for Macka "Trieda = Návrh</br>Urcuje štruktúru"
    note for mojaMacka "Inštancia = Konkrétny objekt</br>S konkrétnymi hodnotami"
```

```py
class Macka:
    def __init__(self, meno, pocetNoh, farba) -> None:
        self.Meno = meno
        self.PocetNoh = pocetNoh
        self.Farba = farba

    def PredstavSa(self):
        print(f"Som macka a volam sa {self.Meno}. Mam {self.PocetNoh} noh a moj kozuch je {self.Farba}")

mojaMacka = Macka("Belka", 3, "strieborna")
mojaMacka.PredstavSa()
```

## `__init__()` funkcia
> Pocas **inicializácie** vytvárame inštanciu objektu z triedy, to znamená, že v pamäti počítača sa sa alokuje, prideluje oblast vo velkosti potrebnej pre vytvorenie danej triedy. Takže z všeobecného opisu (co je tá trieda) vytvárame konkrétny objekt v pamäti pomocou funkcie `__init__()`.

Táto funkcia nám hovorí, ako by sme chceli, aby vyzeralo vytváranie objektu z našej triedy. Môže to fungovat aj bez nej, v tedy funkcia nemá vstupné parametre, ale v tom prípade by používateľ musel vlastnosti nastavit "rucne". Funkcia `__init__()` **zabezpecuje**, že z triedy môžeme vytvorit objekt **len vtedy**, ak mu poskytneme uvedené vlastnosti.
```py
class Macka:

    Meno: str
    PocetNoh: float
    Farba: str

    def PredstavSa(self):
        print(f"Som macka a volam sa {self.Meno}. Mam {self.PocetNoh} noh a moj kozuch je {self.Farba}")

mojaMacka = Macka()
mojaMacka.Meno = "Belka"
mojaMacka.PocetNoh = 3.5
#mojaMacka.Farba = "strieborna"
mojaMacka.PredstavSa()
```
> Každý trieda má funkciu s názvom `__init__()`, ktorý je vždy vykonaná pri vytvárané objektu, aj ked neposkytneme žiadne vstupné parametre. Ak je funkcia `__init__()` prázdna, nemusíte ju samostatne vytvárať.
```py
class TriedaBezVlastnosti:
    def __init__(self) -> None:
        print("Funkciu init sme zavolali")

test = TriedaBezVlastnosti()
```

## `self`
Parameter `self` je odkaz na aktuálnu inštanciu triedy, a slúži na prístup k funkciám a vlastnostiam tejto inštancie.
```mermaid
classDiagram
    class Auto {
        -str Vyrobca
        +__init__(vyrobca)
        +VypisZnacku() : instance method
        +Vypis()$ : static method
    }
    
    class test {
        Vyrobca = "Skoda"
    }
    
    Auto <|.. test : <<instance>>
    
    note for Auto "*VypisZnacku()* - s parametrom self</br>Patrí k objektu</br>*Vypis()* - bez self</br>Patrí k triede (statické)"
```
```py
class Auto:
    def __init__(self, znacka) -> None:
        self.Znacka = znacka
    
    def VypisVyrobcu(self):
        print(f"Výrobca auta je {self.Znacka}")

    def Vypis():
        print("Jednoducho vypíšem")

test = Auto("Skoda")
test.VypisVyrobcu()
Auto.Vypis()
```
Pomocou `self` môžeme pristupovat k vlastnostiam a funkciám konkrétneho objektu:
- `VypisVyrobcu` funguje len na objekte `test`, to sa nazýva **funkcia objektu** alebo funkcia priradené k objektu
- `test.Vypis()` nebude fungovat, pretože objekt `test` nemá funkciu `Vypis()` (chýba `self`)
- `Auto.Vypis()` funguje, a je to **funkcia triedy**, alebo v iných programovacích jazykoch je to považovaná za **statické** funkciu
- `Auto.VypisVyrobcu()` nebude fungovat, pretože to nie je funkcia triedy, ale funkcia inštancie, objektu
### Príklad
```py
class Osoba:
  def __init__(self, meno, vek):
    self.meno = meno
    self.vek = vek

o1 = Osoba("Janko", 36)

print(o1)
print(o1.meno)
print(o1.vek)
```
Výstup by mal byt podobné:
```
<__main__.Osoba object at 0x00000185EC9D75D0>
Janko
36
```
## Funkcia `__str__()`
Pomocou tejto funkcie môžeme ovplyvnit, ako bude naša trieda vyzerat, ked ju premeníme na `str`

```mermaid
classDiagram
    class Osoba {
        -str meno
        -int vek
        +__init__(meno, vek)
        +__str__() str
    }
    
    class p1 {
        meno = "Ján"
        vek = 36
    }
    
    Osoba <|.. p1 : <<instance>>
    
    note for Osoba "__str__() urcuje,</br>ako vyzerá objekt</br>ked ho prevedieme na string"
    note for p1 "*print(p1)* výsledok: Ján(36)</br> Namiesto: *Osoba object*"
```

```py
class Osoba:
  def __init__(self, meno, vek):
    self.meno = meno
    self.vek = vek

  def __str__(self):
    return f"{self.meno}({self.vek})"

o1 = Osoba("Janko", 36)

print(o1, type(o1))
# prípadne
osobaString = str(o1)
print(osobaString, type(osobaString))
```

## `dict` vs `class`
```py
class Osoba:
	def __init__(self, meno, vek):
		self.Meno, self.Vek = meno, vek
    
	def __str__(self) -> str:
		return f"{self.Meno}({self.Vek})"

osobaSlovnik = {"meno":"Janko", "Vek": 16}
osoba = Osoba("Janko", 17)

print(osobaSlovnik, type(osobaSlovnik))
print(osoba, type(osoba))

# vypísanie individuálnych vlastností:
print("osobaSlovnik['Vek']", osobaSlovnik["Vek"])
print('osoba.Vek', osoba.Vek)

# zmena individuálnych vlastností
osobaSlovnik["Vek"] = 98
osoba.Vek = 10

print("osobaSlovnik['Vek']", osobaSlovnik["Vek"])
print('osoba.Vek', osoba.Vek)
```
Kľúče slovníka môžeme považovať vlastnostami triedy, pri slovníku musíme dávať pozor, aby sme **vždy** správne zadali kľúč, pri triede nám Python editor sám ponúkne názov vlastnosti Trieda môže byt rozšírené o rôzne funkcie.
