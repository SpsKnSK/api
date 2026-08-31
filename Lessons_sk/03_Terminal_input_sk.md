> # ✏️ `input()`
>
> **Na čo slúži?** Načíta text z klávesnice, ktorý uložíme do premennej.
>
> **Tvar:** `premenna = input("otázka pre používateľa")`
>
> | Čo napíšem | Čo to robí |
> |---|---|
> | `input()` | čaká, kým niečo napíšeme + Enter |
> | `input("Kolko mas rokov? ")` | najprv vypíše otázku, potom čaká (ušetríme `print`) |
> | `meno = input(...)` | zadaný údaj sa uloží do premennej `meno` |
>
> **⚠️ Najdôležitejšie:** `input()` vracia **vždy text (string)**, aj keď zadáme číslo!
>
> | Čo napíšem | Výsledok |
> |---|---|
> | `cislo = input(...)` | `"50"` – text, nedá sa s ním počítať |
> | `cislo = int(input(...))` | `50` – celé číslo |
> | `cena = float(input(...))` | `1.5` – desatinné číslo |
>
> ```py
> cislo = input("Zadaj cislo: ")   # zadáme: 50
> print(cislo + 12)   # CHYBA! text + číslo nejde
>
> cislo = int(input("Zadaj cislo: "))
> print(cislo + 12)   # 62
> ```
>
> **Ako sa rozhodnúť:**
> ```
> Chcem s tym pocitat?  --> ano, cele cislo    --> int(input(...))
>                       --> ano, desatinne     --> float(input(...))
>                       --> nie (meno, mesto)  --> input(...)
> ```
>
> **Metafora:** `input()` je ako **poštová schránka**: čokoľvek do nej hodíme, program dostane len **obálku** (text), a ak to chceme použiť ako číslo, musíme ju sami "rozbaliť" (`int()`, `float()`).

# `input()`
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
>>> text = input("Kolko je hodin? ")
Kolko je hodin? 9
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

## Úlohy
1. Napíšte program, ktorý sa vás opýta na vaše meno. Keď zadáte svoje meno, opýta sa vás, koľko máte rokov, a potom vypíše súhrnnú vetu o tom, kto sedí pred počítačom `Ahoj [pocetRokov] rocny [meno], vidim, ze ty sedis pred pocitacom`
1. Napíšte program, ktorý zo zadaných údajov (meno, bydlisko a kontakt) vypíše na obrazovku vizitku.

    ```
    Meno: [meno]
    Bydlisko: [bydlisko]
    Kontakt: [kontakt]
    ```
1. Vypýtajte od používateľa tri prirodzené čísla, ktoré postupne znamenajú počet 5, 2 a 1 eur. Určte a vypíšte celkovú sumu.
príklad:
    ```
    Pocet 5 eur: 2
    Pocet 2 eur: 3
    Pocet 1 eur: 1
    To je celkovo 17 eur.
    ```
1. Vypíšte malú násobilku pre zadané číslo (od 1 do 10). Zatiaľ stačí 10 samostatných príkazov `print`.
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
    
    1. Napíšte program, ktorý vám povie, koľko peňazí si máte vziať so sebou, ak kúpite 1 kg jabĺk, 1.5 kg citrónov a 2 kg pomarančov.
    Skúste aj iné hodnoty.
    Napr. kúpite 3 kily každého ovocia, 5 kíl, atď.
    > Pozor: počet kíl môže byť aj desatinné číslo, preto tu treba `float(input(...))`!
    1. Spýtajte sa používateľa, koľko peňazí má u seba a z toho koľko **celých** kilogramov jabĺk, citrónov alebo pomarančov vie kúpiť.

> # 💥 Pokazte to!
> Napíšte také riadky s `input()`, ktoré Python odmietne s chybou. Nápady:
>
> - `cislo = input("Zadaj cislo: ")` a potom `print(cislo + 12)`
> - `int(input("Kolko mas rokov? "))`, ale zadáte písmeno, nie číslo
> - `int(input("Cena: "))`, ale zadáte desatinné číslo, napr. `1.5`
> - chýba jedna zátvorka na konci `int(input(...))`
>
> Prečítajte si chybovú správu: ako sa chyba volá a čo prezrádza o tom, kde je problém?

> # ❓ Otázky
> 1. Napíšte kód, ktorý od používateľa získa jeho meno a vek, a potom na obrazovku vypíše, koľko bude mať rokov o 10 rokov. Príklad: `Ahoj [meno], teraz máš 16 rokov, o 10 rokov budeš mať 26 rokov.`
> 1. Aký dátový typ číta funkcia `input` z klávesnice?
> 1. Čo robí `int()` a čo `float()`? Kedy ktoré použijeme okolo `input()`?
