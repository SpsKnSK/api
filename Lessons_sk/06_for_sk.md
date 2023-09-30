# Úvod do cyklov
V programovaní v jazyku Python rozlišujeme dva druhy cyklov:
- počítaný `for` - vopred vieme, koľkokrát sa vykoná, počet opakovaní je daný
- nepočítaný `while`- vopred nevieme určiť, koľkokrát sa vykoná, cyklus sa opakuje, kým je splnená podmienka

## Cyklus
Príkaz, ktorý umožňuje vykonať inštrukciu viackrát.
> Cykly menia smer behu programu, pretože sa vracajú na začiatok cyklu.
## Jadro cyklu
Súbor príkazov vykonávaných v cykle.
## Premenná cyklu (pre cyklus `for`)
Pomocná premenná cyklu, ktorá mení svoju hodnotu pri každom behu cyklu.
Rastie/klesá o jeden/dva/desať...

# Intervaly
Rozlišujeme dva druhy intervalov:
- otvorený (0; 5), kde hranice **ne**patria do intervalu: 1, 2, 3, 4
- uzavretý <0; 5>, kde hranice **patria** do intervalu: 0, 1, 2, 3, 4, 5

# `for` cyklus
Počítaný cyklus, vieme vopred, koľkokrát sa vykoná. Použitie:
- potrebujeme niečo vykonať `x`-krát
- potrebujeme prejsť prvky v zozname
## Syntax, sada pravidiel, popis
```py
for [premenna_cyklu] in range(x,y):
    if podmienka1:   # jadro cyklu
        continue     # jadro cyklu
    prikaz           # jadro cyklu
    prikaz           # jadro cyklu
    prikaz           # jadro cyklu
    if podmienka2:   # jadro cyklu
        break        # jadro cyklu
else:
    prikaz
```
## Interpretácia
- Jadro cyklu oddelíme od príkazu `for` tabulátorom alebo medzerami (odporúčam tab)
- Premenné `x` a `y` označujú začiatok a koniec rozsahu, intervalu, napr. <1;10)
- `remenna_cyklu`, ak je celé číslo, zvyčajne označujeme `i` a hodnotu získa v rozsahu určenom `range`
- Ako pri `if`, aj pri cykle `for` máme možnosť vytvoriť vetvu `else` (_špecifikum jazyka Python_), ktorá sa vykoná, ak sa cyklus **ne** preruší príkazom `break`
- Po `continue` sa ďalšie príkazy nevykonajä, cyklus pokračuje s ďalšou hodnotou, na ktorej sa má vykonať jadro cyklu (ale pozor, v príklade je tento prípad je podmienený)
- `break` ukončuje vykonávanie jadro cyklu a vykoná príkaz nasledujúci po cykle (ale pozor, v príklade je tento prípad je podmienený)

### Príklady
```py
for i in range(0,3):
    print(x)
```
```py
a = 10
for i in range(1, 5):
    print(a+i)
```
# Vlastnosti `for` cyklu
`for` cyklus vždy beží v určenom rozsahu, ktorý je jednoznačne definovaný. `range()` funkciu nie je vždy nutné použiť, pretože takýmto definovaným rozsahom môže byť aj reťazec `string`.

```py
text = "jablko"
for c in text: # c ako znak
    print(c)
```
## Úloha
Vytvorte program, ktorý vypíše všetky celé čísla od 1 do 15 a k nim druhú mocninu.
```
1 1
2 4
3 9
...
14 196
15 225
```
## Úloha
Napíšte program, ktorý v zadanom rozsahu vypíše všetky:
- čísla deliteľné 2 a 4 navzájom
- čísla deliteľné 5
- čísla väčšie ako 35
> Môžete to urobiť v jednom `for` cyklom alebo vytvoriť 3 samostatné cykly.
## Úloha 
Určte a vypíšte všetky prirodzené čísla menšie ako 1000, ktoré sú deliteľné tromi aj piatimi navzájom.
## Úloha
Požiadajte o **N** prirodzených čísel (najprv vypýtajte **N**). Po zadaní dát program vypíše:
- počet párnych čísel
- počet nepárnych čísel
- súčet nepárnych čísel!

# `range()`
```py
class range(
    __

start: SupportsIndex,
    __stop: SupportsIndex,
    __step: SupportsIndex = ...,
    /
)
```
- `__start` začiatok intervalu, uzavretý
- `__stop` koniec intervalu, otvorený
- `__step` krok

```py
for i in range(0,10,3):
    print(x)
```

- `range(5, 10)`: 5, 6, 7, 8, 9
- `range(0, 10, 3)`: 0, 3, 6, 9 
- `range(-10, -100, -30)`:  -10, -40, -70

## Úlohy
- Vypíšte čísla deliteľné 3 do 100.
- Vypíšte čísla deliteľné 7 v intervale od 50 do 99.
- Odpočítajte naspäť od 50 do 20 s krokom 4 a vypíšte jednotlivé čísla!

# Otázky
1. Čo je rozdiel medzi otvoreným a uzavretým intervalom?
1. Do ktorých hodnôt patria nasledujúce intervaly: <1; 6), <-2;1>, (6;3)?
1. Aké druhy cyklov poznáte? Nastriekajte rozdiely.
1. Koľko príkazov môže byť v telocvični?
1. Napíšte syntax `for` cyklu.
1. Pomocou cyklu `for` vypíšte násobkovú tabuľku, ktorú určuje používateľ.
1. Spočítajte späť od 20 do 0 s krokom 4 a vypíšte každé štvrté číslo.
1. Aký je rozdiel medzi príkazmi `break` a `continue`?
1. Koľko `else` vetiev môže mať `for` cyklus?
1. Je vždy potrebná vetva `else`?
1. Kedy sa vykoná vetva `else`?
1. Môže `for` cyklus fungovať bez `break`?
1. Môže `for` cyklus fungovať bez `continue`?
1. Načo slúži funkcia `range()`? Uveďte jej parametre.
1. Čo vypíše nasledujúci program?
    ```py
    for i in range(2, 10, 3):
        print(i, end=" ")
    ```
1. Čo vypíše nasledujúci program?
    ```py
    for i in range(0,10):
        break
        print(i)
    else:
        print("Else")
    print("Krásny deň!")
    ```
1. Čo vypíše nasledujúci program?
    ```py
    for i in range(0,10):
        continue
        print(i)
    else:
        print("Else")
    print("Krásny deň!")
    ```