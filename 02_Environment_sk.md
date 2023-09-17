# Python programovacie prostredie

## Základné informácie

- Zdarma na stiahnutie
- Možnosť spustenia na akomkoľvek operačnom systéme
- Malá náročnosť na miesto
- Množstvo knižníc -> Veľmi využiteľný na rôznych oblastiach
    - Základné programovanie
    - Riadenie procesov
    - Správa databáz
    - Atď.

## Podrobne o prostredí
- Z hľadiska syntaxe a pokročilosti sa podobá jazyku C.
- Pracujeme s dvoma hlavnými oknami.
    - **Príkazový riadok** – tu spúšťame napísaný program
    - **Editor skriptov** – tu píšeme programy

# Premenné

- Premenné sú prvky programu, ktoré môžu nadobúdať rôzne hodnoty a slúžia na uchovávanie rôznych údajov.
- Miesto v pamäti s menom
- Napr. x, z, cislo, meno, zoznam

## Typy 
- **Číslo** – `int` – pre ukladanie celých čísel v rozpätí približne -36 000 až 36 000. 10, -9, 0
- **Desatinné číslo**– `float` – pre ukladanie desatinných čísel 95,78, 3,14, 79,21
- **Komplexné číslo**– `complex` – pre ukladanie komplexných čísel -9+6j, 1-8j
- **Reťazec** – `str` – pre ukladanie textu a ľubovoľných významných/ne-významných postupností znakov, môžete použiť jednoduché `''` alebo dvojité `""` úvodzovky
    - napr. `'jablko'`, `'3tlacitko'`, atď.
- **Logická hodnota** – `bool` - Môže mať dve hodnoty:
    - `True` – Pravda (číselná hodnota môže byť čokoľvek okrem 0)
    - `False` – Nepravda/nedokázané (číselná hodnota je 0)
# Operácie
## Matematickí operátori
- `5 + 3` súčet
- `5 – 3` rozdiel
- `5 * 3` súčin
- `5 / 3` delenie
- `5 // 3` celočíselné delenie
- `5 % 3` zvyšok po delení
- `5 ** 3` umocňovanie
- `sqrt(5)` odmocnina (na to je potrebný matematický modul)

## Logickí operátori
- rovnosť `==`
    - napr. X==5 – skontrolujeme, či je X rovnaké 5
- menšie `<`
- menšie alebo rovné `<=`
- väčšie `>`
- väčšie alebo rovné `>=`
- nerovnosť `!=`
- priradenie `=`
    - napr. X=12 – premenná X sa nastaví na hodnotu 12

# Pravidlá písania programu
- V Pythone musíme rozlišovať medzi malými a veľkými písmenami,
- Názvy premenných môžu obsahovať písmená, číslice a podčiarkovník `_`.
- Názvy premenných:
    - Nesmú začínať číslom,
    - Nesmú obsahovať medzery, tabulátory,
    - Nesmú byť rezervované slová (príkazy), napr. Max, min, print, atď.

## Správny názov pre premennú
```py
mujvar = "Janko"  
moje_premenna = "Janko"  
_moje_premenna = "Janko"  
mojePremenna = "Janko"  
MOJAPREMENNA = "Janko"  
mujvar2 = "Janko"
```
## Nesprávny názov pre premennú, program sa nepustí
```py
2moje_premenna = "Janko"  
moje-premenna = "Janko"  
moje premenna = "Janko"
```

# Cvičenie 
1. Vytvorte 2 premenné pre každý spomenutý typ a pomocou funkcie `print()` ich vypíšte na obrazovku.
1. Pri premenných typu číslo vyskúšajte všetky matematické operátory!

## Pomoc
- **Číslo** – `int`
- **Desatinné číslo**– `float`
- **Komplexné číslo** - `complex`
- **Reťazec** – `str` 
- **Logická hodnota** – `bool` 
- rovnosť `==`
- menšie `<`
- menšie alebo rovné `<=`
- väčšie `>`
- väčšie alebo rovné `>=`
- nerovnosť `!=`
- priradenie `=`