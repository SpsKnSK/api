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

## Úlohy
1. Napíšte program, ktorý vás opýta na vaše meno. Keď zadáte svoje meno, opýta sa vás, koľko máte rokov, a potom vypíše súhrnnú vetu o tom, kto sedí pred počítačom `Ahoj [pocetRokov] rocny [meno], vidim, ze ty sedis pred pocitacom`
1. Napíšte program, ktorý zo zadaných údajov (meno, bydlisko a kontakt) vypíše na obrazovku vizitku.
```
Meno: [meno]
Bydlisko: [bydlisko]
Kontakt: [kontakt]
```
1. Vypýtajte od používateľa tri prirodzené čísla, ktoré postupne znamenajú počet 5, 2 a 1 eur. Určte a vypíšte celkovú sumu.
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
> `/` delenie na desatinné čisla: `18/7=2.571428571428571`
 
> `//` celočíselné delenie: `18//7=2`
 
> `%` zvyšok po delení: `18 % 7=4`
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
    
    1. Napíšte program, ktorý vám povie, koľko peňazí si máte vziať so sebou, ak kúpite 1 kg jabĺk, 1,5 kg citrónov a 2 kg pomarančov.
    Skúste aj iné hodnoty.
    Napr. kúpite 3 kily každého ovocia, 5 kíl, atď.
    1. Spýtajte sa používateľa, koľko peňazí má u seba a z toho koľko **celých** kilogramov jabĺk, citrónov alebo pomarančov vie kúpiť.
## Otázky
1. Na čo slúži funkcia `round`, uveďte príklad.
2. Napíšte kód, ktorý od používateľa získa jeho meno a vek, a potom na obrazovku vypíše, koľko bude mať rokov o 10 rokov. Príklad: `"Ahoj [meno], teraz máš 16 rokov, o 10 rokov budeš mať 26 rokov."`
3. Aký dátový typ číta funkcia `input` zo klávesnice?