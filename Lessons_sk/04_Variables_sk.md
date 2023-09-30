# Premenné

- Premenné sú prvky programu, ktoré môžu nadobúdať rôzne hodnoty a slúžia na uchovávanie rôznych údajov.
- Menom označené miesto v pamäti
- Názov premennej môže byť: x, z, cislo, meno, zoznam

## Typy 
- **Číslo** – `int` – pre ukladanie celých čísel v rozpätí približne -36 000 až 36 000. 10, -9, 0
- **Desatinné číslo**– `float` – pre ukladanie desatinných čísel 95,78, 3,14, 79,21
- **Komplexné číslo**– `complex` – pre ukladanie komplexných čísel -9+6j, 1-8j
- **Reťazec** – `str` – pre ukladanie textu a ľubovoľných významných/ne-významných postupností znakov, môžete použiť jednoduché `''` alebo dvojité `""` úvodzovky
    - napr. `'jablko'`, `'3tlacitko'`, `"hram futbal"` atď.
- **Logická hodnota** – `bool` - Môže mať dve hodnoty:
    - `True` – Pravda (číselná hodnota môže byť čokoľvek okrem 0)
    - `False` – Nepravda/nedokázané (číselná hodnota je 0)
# Operácie
## Matematické operátory
- `5 + 3` súčet
- `5 – 3` rozdiel
- `5 * 3` súčin
- `5 / 3` delenie
- `5 // 3` celočíselné delenie
- `5 % 3` zvyšok po delení
- `5 ** 3` umocňovanie
- `sqrt(5)` odmocnina (na to je potrebný matematický modul)
## Úloha
1. Pomocou funkcie `print()` vypíšte na obrazovku výsledky aspoň 5 vyššie uvedených matematických operácií.
## Logické operátory
- rovnosť `==`
    - napr. X==5 – skontrolujeme, či sa X rovná 5
- menšie `<`
- menšie alebo rovné `<=`
- väčšie `>`
- väčšie alebo rovné `>=`
- nerovnosť `not`
- priradenie `=`
    - napr. `X=12` – premenná X sa nastaví na hodnotu 12

# Pravidlá písania programu
- V Pythone musíme rozlišovať medzi malými a veľkými písmenami,
- Názvy premenných môžu obsahovať písmená, číslice a podčiarkovník `_`.
- Názvy premenných:
    - Nesmú sa začínať číslom,
    - Nesmú obsahovať medzery, tabulátory,
    - Nesmú byť rezervované slová (príkazy), napr. `max`, `min`, `print`, atď.

## Správny názov pre premennú
```py
mojapremenna = "Janko"  
moja_premenna = "Janko"  
_moja_premenna = "Janko"  
mojaPremenna = "Janko"   
MojaPremenna = "Janko"  
MOJAPREMENNA = "Janko"  
mojaPremenna2 = "Janko"
```
## Nesprávny názov pre premennú, program sa nepustí
```py
2moje_premenna = "Janko" #zacina sa cislom  
moje-premenna = "Janko"  #obsahuje -
moje premenna = "Janko" #obsahuje medzeru
```

## Odporúčam používať
```py
moja_premenna = "Janko"
mojaPremenna = "Janko"  
MojaPremenna = "Janko"  
```

# Cvičenie 
1. Vytvorte 2 premenné pre každý spomenutý typ a pomocou funkcie `print()` ich vypíšte na obrazovku.
1. Pri premenných typu číslo vyskúšajte všetky matematické operátory!
1. Vypýtajte si od používateľa 2 celé čísla, potom 2 desatinné čísla a nakoniec 2 komplexné čísla a vypíšte na obrazovku ich súčet a súčin:
    1. načítanie celého čísla: `int(input())`
    1. načítanie desatinného čísla: `float(input())`
    1. načítanie komplexného čísla: `complex(input())`

## Pomoc

### Dátové typy

**Číslo** – `int`|**Desatinné číslo**– `float`|**Komplexné číslo**- `complex`
--|--|--
**Reťazec**– `str`|**Logická hodnota**– `bool`

### Operácie: 

| | | | |
|-|-|-|-|
súčet `+`| rozdiel `-` |  súčin`*`| delenie `/` | 
celočíselné delenie `//` | zvyšok po delení `%` | umocňovanie `**`| rovnosť `==`
menšie `<`|menšie alebo rovné `<=` |väčšie `>`| väčšie alebo rovné `>=`
priradenie `=`|

## Otázky
1. Aký je rozdiel medzi `=` a `==`? Kedy použijete jeden a kedy druhý operátor?
2. Požiadajte používateľa, aby zadal dĺžky obidvoch odvesien trojuholníka a použitím Pytagorovej vety vypočítajte dĺžku prepony.
3. Uveďte 2 príklady povolených názvov premenných.
4. Uveďte 2 príklady **nepovolených** názvov premenných.
5. Ako môžeme overiť, či je číslo `a` deliteľné číslom `b`? Ktorú operáciu použijete?
6. Aký je rozdiel medzi `\` a `\\`?