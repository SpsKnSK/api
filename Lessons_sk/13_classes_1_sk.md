> # ✏️ Triedy (`class`)
>
> Trieda je **plán**, inštancia (objekt) je z nej vytvorená **konkrétna vec**.
>
> ```py
> class Macka:
>     def __init__(self, meno, farba) -> None:
>         self.Meno = meno
>         self.Farba = farba
>
>     def Predie(self):
>         print(f"{self.Meno} je {self.Farba} mačka a pradie")
>
> cica = Macka("Cilka", "strieborná")   # vytvorenie inštancie - konkrétny objekt
> cica.Predie()
> ```
>
> - `class Nazov:` - vytvorenie triedy (plánu)
> - `__init__(self, ...)` - spustí sa pri každom vytvorení inštancie, nastaví počiatočné vlastnosti
> - `self` - "táto konkrétna inštancia", cez ňu pristupujeme k vlastným vlastnostiam a funkciám
> - `self.Vlastnost = hodnota` - nastavenie vlastnosti
> - `__str__(self)` - určuje, ako bude objekt vyzerať po prevedení na text (`str`) alebo pri výpise
>
> **Metafora:** trieda je ako **forma na sušienky**: samotná forma nie je sušienka, ale každá sušienka z nej dostane rovnaký základný tvar (a pritom ju môžeme ozdobiť inak).

# Triedy, vlastné/zložené dátové typy `class`

Doposiaľ sme sa stretli a pracovali s dátovými typmi ako `int`, `float`, `str`, `random`, `list`, `dict`, ale teraz sme schopní ísť ďalej a definovať si vlastný dátový typ.

S `class` príkazom definujeme, hovoríme Pythonu, ako by sme chceli, aby náš vlastný dátový typ vyzeral:
- s akými vlastnosťami (attributes, property) by mal byť vybavený -> čo **má**
- s akými funkciami by mal byť vybavený -> čo vie **robiť**

`class` je akýsi **návrh**, ako by sme chceli, aby vyzerali **objekty**, **inštancie**, ktoré z neho vytvoríme.

> **Objekt** alebo **inštancia** je súhrn dát, ktorý je reálne uložený v pamäti. Premenná ukazuje na túto konkrétnu adresu a tak určuje alebo mení jej hodnotu.

Definovanie triedy pomocou príkazu `class`. V nasledujúcom príklade vytvárame návrh triedy, ktorá sa volá `MyClass` a má vlastnosť `x`:

```py
class MyClass:
  x = 5
```

Ak chceme z tejto triedy, návrhu, vytvoriť objekt, môžeme to urobiť nasledovne:

```py
p1 = MyClass()
print(p1.x)
```

S triedou ešte nevieme pracovať (okrem niekoľkých výnimiek), z nej musíme vytvoriť objekt, inštanciu.

## Mačka
Môžeme si to predstaviť aj tak, že v prírode je **mačka**, vieme, že je obvykle chlpatá, má 4 nohy, má meno, mňauká, mazná sa, spí, atď. - toto je návrh na "výrobu" mačky. Ale ak už máme konkrétnu mačku u nás doma, alebo v susedstve (Murko, Labka, Belka, Cilka), už pre ňu udeľujeme konkrétne vlastnosti.

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
    
    note for Macka "Trieda = Návrh</br>Určuje štruktúru"
    note for mojaMacka "Inštancia = Konkrétny objekt</br>S konkrétnymi hodnotami"
```

```py
class Macka:
    def __init__(self, meno, pocetNoh, farba) -> None:
        self.Meno = meno
        self.PocetNoh = pocetNoh
        self.Farba = farba

    def PredstavSa(self):
        print(f"Som mačka a volam sa {self.Meno}. Mam {self.PocetNoh} noh a moj kozuch je {self.Farba}")

mojaMacka = Macka("Belka", 3, "strieborna")
mojaMacka.PredstavSa()
```

## `__init__()` funkcia
> Počas **inicializácie** vytvárame inštanciu objektu z triedy, to znamená, že v pamäti počítača sa sa alokuje, prideluje oblasť vo veľkosti potrebnej pre vytvorenie danej triedy. Takže z všeobecného opisu (čo je tá trieda) vytvárame konkrétny objekt v pamäti pomocou funkcie `__init__()`.

Táto funkcia nám hovorí, ako by sme chceli, aby vyzeralo vytváranie objektu z našej triedy. Môže to fungovať aj bez nej, v tedy funkcia nemá vstupné parametre, ale v tom prípade by používateľ musel vlastnosti nastaviť "ručne". Funkcia `__init__()` **zabezpečuje**, že z triedy môžeme vytvoriť objekt **len vtedy**, ak mu poskytneme uvedené vlastnosti.
```py
class Macka:

    Meno: str
    PocetNoh: float
    Farba: str

    def PredstavSa(self):
        print(f"Som mačka a volam sa {self.Meno}. Mam {self.PocetNoh} noh a moj kozuch je {self.Farba}")

mojaMacka = Macka()
mojaMacka.Meno = "Belka"
mojaMacka.PocetNoh = 3.5
#mojaMacka.Farba = "strieborna"
mojaMacka.PredstavSa()
```
> Každá trieda má funkciu s názvom `__init__()`, ktorá je vždy vykonaná pri vytváraní objektu, aj keď neposkytneme žiadne vstupné parametre. Ak je funkcia `__init__()` prázdna, nemusíte ju samostatne vytvárať.
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
    
    note for Auto "*VypisZnacku()* - s parametrom self</br>Patrí k objektu</br>*Vypis()* - bez self</br>Patrí k triede (statická)"
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
Pomocou `self` môžeme pristupovať k vlastnostiam a funkciám konkrétneho objektu:
- `VypisVyrobcu` funguje len na objekte `test`, to sa nazýva **funkcia objektu** alebo funkcia priradená k objektu
- `test.Vypis()` nebude fungovať, pretože objekt `test` nemá funkciu `Vypis()` (chýba `self`)
- `Auto.Vypis()` funguje, a je to **funkcia triedy**, alebo v iných programovacích jazykoch je to považované za **statickú** funkciu
- `Auto.VypisVyrobcu()` nebude fungovať, pretože to nie je funkcia triedy, ale funkcia inštancie, objektu
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
Výstup by mal byť podobný:
```
<__main__.Osoba object at 0x00000185EC9D75D0>
Janko
36
```
## Funkcia `__str__()`
Pomocou tejto funkcie môžeme ovplyvniť, ako bude naša trieda vyzerať, keď ju premeníme na `str`

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
    
    note for Osoba "__str__() určuje,</br>ako vyzerá objekt</br>keď ho prevedieme na string"
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
Kľúče slovníka môžeme považovať vlastnosťami triedy, pri slovníku musíme dávať pozor, aby sme **vždy** správne zadali kľúč, pri triede nám Python editor sám ponúkne názov vlastnosti Trieda môže byť rozšírená o rôzne funkcie.

> # 💥 Pokazte to!
>
> Aká je chyba v tomto programe?
>
> ```py
> class Macka:
>     def __init__(self, meno, farba) -> None:
>         self.Meno = meno
>         self.Farba = farba
>
> cirmi = Macka("Cirmi", "strieborná")
> print(cirmi.Predie())
> ```
>
> Prečo to nefunguje? Čo treba doplniť, aby trieda `Macka` vedela priasť a nielen uchovávať svoje meno a farbu?
>
> # 📋 Úlohy
> - [e01_fish.md](../Exercies/13_classes/e01_fish.md)
> - [e02_worker.md](../Exercies/13_classes/e02_worker.md)
> - [e03_bankAccount.md](../Exercies/13_classes/e03_bankAccount.md)
> - [e04_figureSkating.md](../Exercies/13_classes/e04_figureSkating.md)
>
> # ❓ Otázky
>
> 1. Vytvorte triedu `Pes`, ktorá má meno a farbu. Tieto hodnoty nastavte pri vytvorení inštancie pomocou funkcie `__init__`. Vytvorte 2 inštancie:
>    1. meno nech je Cezar, farbu si zvoľte sami
>    2. meno si zvoľte sami, farba nech je biela
>    - Vypíšte ich vlastnosti na obrazovku.
> 2. Vytvorte triedu `Auto` s týmito vlastnosťami: farba, značka, model, rok výroby. Môžete použiť funkciu `__init__`, ale nemusíte. Definujte tieto 2 funkcie:
>    1. `Start` - vypíše na obrazovku: "[farba] auto z roku [rok výroby], značky [značka] [model], sa rozbehlo"
>    2. `Stop` - vypíše na obrazovku: "Auto sa zastavilo"
>    - vytvorte 3 inštancie
>    - vložte ich do zoznamu
>    - a zavolajte na nich obe funkcie
> 3. Vytvorte triedu `Pracovnik` s týmito vlastnosťami: id, plat, pohlavie, vek. Upravte funkciu `__str__` tak, aby vracala tento reťazec: "Zamestnanec s id [id] je [pohlavie], zarába [plat] eur a má [vek] rokov." Pomocou knižnice `random`:
>    - vygenerujte náhodný počet zamestnancov v intervale <75;120>
>      - `id` nech je z intervalu <10000;100000>
>      - `plat` nech je z intervalu <1000;5000>
>      - `pohlavie`: muž alebo žena
>      - `vek` nech je z intervalu <20;99>
>    - vygenerované inštancie `Pracovnik` vložte do zoznamu a vypíšte ich hodnoty na obrazovku
> 4. Na čo slúži parameter `self` a kedy ho môžeme vynechať z definície funkcie?

