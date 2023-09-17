# Príkazy `print()` a `input()`
## `print()`
- Výpis údajov a informácií na obrazovku
- Môžeme vypísať:
    - Text
    - Čísla
    - Obsah premennej
    - Výsledky matematických operácií s viacerými premennými

### Úlohy
1. Výpis textu (čo je rozdiel?):
    ```py
    print("Ahoj svet")
    print('Ahoj svet')
    ```
1. Výpis čísla (čo je rozdiel?):
    ```py
    print(123.45)
    print(12, 45)
    ```
1. Výpis premennej
    ```py
    cislo1 = 5
    cislo2 = 11
    print(cislo1)
    ```
1. Výpis súčtu
    ```py
    cislo1 = 5
    cislo2 = 11
    print(cislo1 + cislo2)
    ```

## `print()` – zmiešaný výpis
V rámci jedného `print()` príkazu je možné vypisovať viac údajov.

Tieto údaje oddelíme čiarkou.

```py
pocet = 12
print(pocet, "gitarových strún")
```
V rámci jedného `print()` príkazu môžeme vykonávať operácie s rôznymi typmi údajov.

```py
cislo1 = 12
cislo2 = 8
print(cislo1 + cislo2, cislo1 * cislo2)
```
Pri texte - reťazci - je situácia trochu iná.
```py
print('jeden balík', 'gitárových'+'strún')
```
### Výpis vedľa seba vs. pod seba
Pri výpise textu na rovnakom riadku použijeme iba jeden príkaz `print()` a údaje zapišeme do zátvoriek.
```py
print('Ahoj', 'Peter!')
```
Pri výpise textu na oddelených riadkoch použijeme viac príkazov `print()`, každý pre svoj riadok.
```py
print('Ahoj')
print('Peter!')
```
alebo môžeme použiť znak pre nový riadok `\n`
```py
print('Ahoj\nPeter!')
```
## Prax
Sú zadané tri premenné s týmito hodnotami:
```py
prva = 12
druha = 24
tretia = 34
```
1. Vypíšte tieto tri čísla na obrazovku nasledovne: 
```
Prvé číslo: 12
Druhé číslo: 24
Tretie číslo: 34
```
2. Vypíšte súčet týchto troch čísel a súčin prvých dvoch čísel.

# Funkcia `input()`

Načítanie údajov (textu) a uloženie do premennej.
```py
>>> text = input()
jablko
>>> print(text)
jablko
```

Python umožňuje pomocou príkazu `input()` poslať správu používateľovi, že potrebujeme určité údaje.
Správu zapíšeme do zátvoriek príkazu `input` medzi jednoduché alebo dvojité úvodzovky.
Program pri spustení zobrazí správu a potom čaká na zadané údaje. Ušetríme tak príkaz `print()`!
## Príklad 

```py
>>> text = input("Koľko je hodín?")
Koľko je hodín?9
>>> print(text)
9
```

## `input()` – čísla(celé čísla) 
`cislo = input("Zadaj číslo!")`

Hodnota premennej `cislo` po zadaní: `"50"`

Prečo toto nie je správne?
Skúsime teraz k premennej `cislo` pridať `12`.

### Opravený kód:
`cislo = int(input("Zadaj číslo!"))`

Čo sa zmenilo? 
Čo znamená slovo `int`?

Skúsime teraz k premennej `cislo` pridať 12.

## Písanie kódu
- Vytvorenie nového skriptu
- Uloženie napísaného skriptu
    - Každý nech si uloží do vlastného priečinka (zložky) s menom
    - Časté ukladanie (Ctrl+S), nielen keď je program úplne hotový!!!
- Spustenie skriptu (F5 alebo z menu Súbor)

## Úlohy
1. Napíšte program, ktorý vás opýta na vaše meno. Keď zadáte svoje meno, opýta sa vás, koľko máte rokov, a potom vypíše súhrnnú vetu o tom, kto sedí pred počítačom.
1. Napíšte program, ktorý zadané údaje zloží do vizitky a vypíše na obrazovku.
Naše údaje: Meno, By

dlisko, Kontakt
1. Poprosíme o tri prirodzené čísla, ktoré postupne znamenajú počet 5, 2 a 1 eurových mincí. Určte a vypíšte celkovú sumu.
príklad:
```
Počet 5 eur: 2
Počet 2 eur: 3
Počet 1 eur: 1
To je celkovo 17 eur.
```
# Zaokrúhlenie
- pomocou funkcie `round`
- `round(a, x)`
- `a` – číslo
- `x` - počet desatinných miest

Napr. `round(12.345, 2)` dáva výsledok `12.35`
Do miesta čísla môže ísť aj premenná!
## Úlohy
1. Napíšte program, ktorý zistí dve čísla od vás, a potom vypíše ich podiel na 3 desatinné miesta.
Potom vypíšte celočíselný výsledok delenia a zvyšok po delení.
Dávajte pozor, aby bol program použiteľný aj pre laických používateľov (nech program napíše aj jedno-dva slová, nie len konkrétne výsledky).
1. Napíšte program na výpočet obvodu a plochy kruhu.
Zadané údaje: priemer kruhu, hodnota Pí: `3.14159`.
Výsledok:
`Kruh s priemerom X cm má obvod Y cm a plochu Z cm².`
1. Napíšte program, ktorý vypíše malú násobilku pre zadané číslo (od 1 do 10).
    ```
    Ktorú násobilku vypíšem? 11
    1*11=11
    2*11=22
    3*11=33
    ...
    10*11=110
    ```
1. Nakupujete ovocie v miestnom obchode.
    - Cena za kilogram jabĺk je 0.65 €
    - Cena za kilogram citrónov je 1.2 € 
    - Cena za kilogram pomarančov je 1.5 €
    
    Napíšte program, ktorý vám povie, koľko peňazí si máte vziať so sebou, ak kúpite 1 kg jabĺk, 1,5 kg citrónov a 2 kg pomarančov.
    Skúste aj iné hodnoty.
    Napr. kúpite 3 kily každého ovocia, 5 kíl, atď.