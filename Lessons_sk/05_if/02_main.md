🗺️ [Späť na mapu učiva](../../Lessons_sk/00_Mapa_sk.md)

# If – Elif – Else

## Ako program mení smer?

Program zvyčajne vykonáva príkazy postupne, jeden po druhom. Pomocou podmienok však môže vybrať, ktoré príkazy sa vykonajú. Na opakovanie slúžia cykly `while` a `for`.

## Čo je blok?

**Blok** je skupina príkazov, ktoré patria k sebe a vykonávajú sa spolu. Python rozpoznáva blok podľa **odsadenia**.

~~~python
if znamka == 1:
    print("Gratulujem!")
    print("Si šikovný!")
print("Koniec programu")
~~~

Prvé dva príkazy `print` patria do bloku `if`. Posledný príkaz sa vykoná vždy.

- Riadok otvárajúci blok sa končí dvojbodkou `:`.
- Všetky príkazy v bloku majú rovnaké odsadenie (zvyčajne 4 medzery).
- Blok končí, keď sa odsadenie vráti späť.
- Blok môže obsahovať aj ďalší blok.

## Syntax vetvenia

~~~python
if podmienka_1:
    prikazy_1
elif podmienka_2:
    prikazy_2
else:
    ine_prikazy
~~~

- `if` je povinné.
- `elif` znamená „inak, ak“ a môže sa použiť aj viackrát.
- `else` je nepovinné a vykoná sa, ak nebola pravdivá žiadna predchádzajúca podmienka.
- Ak chýba `else` a žiadna podmienka nie je pravdivá, nevykoná sa žiadna vetva.

Python kontroluje podmienky **zhora nadol**. Vykoná sa iba prvá pravdivá vetva; ostatné preskočí.

## Príklad so známkami

~~~python
znamka = int(input("Akú známku si dostal? "))

if znamka == 1:
    print("Gratulujem, výborný výsledok!")
elif znamka == 2:
    print("Veľmi pekne.")
elif znamka == 3:
    print("Dá sa to ešte zlepšiť.")
elif znamka == 4:
    print("Nabudúce sa priprav lepšie.")
else:
    print("Skús sa učivu venovať viac.")
~~~

Viac príkazov v jednej vetve stačí napísať pod seba s rovnakým odsadením.

## Vnorené podmienky

Do bloku `if` možno vložiť ďalší `if`. Vnútorná podmienka sa kontroluje iba vtedy, ak je vonkajšia podmienka pravdivá.

~~~python
cislo = 55

if cislo > 30:
    print("Číslo je väčšie ako 30.")
    if cislo > 40:
        print("Číslo je väčšie ako 40.")
        if cislo > 50:
            print("Číslo je väčšie ako 50.")
        else:
            print("Číslo je najviac 50.")
    else:
        print("Číslo je najviac 40.")
else:
    print("Číslo je najviac 30.")
~~~

Vyskúšaj hodnotu `cislo = 35`. Ktoré správy sa vypíšu a prečo?

## Logické operátory

### `and` – logické A

Výraz je pravdivý, iba ak sú pravdivé **všetky** podmienky.

| a | b | `a and b` |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | **1** |

### `or` – logické ALEBO

Výraz je pravdivý, ak je pravdivá **aspoň jedna** podmienka.

| a | b | `a or b` |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | **1** |
| 1 | 0 | **1** |
| 1 | 1 | **1** |

### `not` – logická negácia

Obráti pravdivostnú hodnotu: pravda sa zmení na nepravdu a naopak.

| a | `not a` |
|---|---|
| 0 | **1** |
| 1 | **0** |

~~~python
cislo = int(input("Zadaj číslo: "))

if cislo > 3 and cislo < 10:
    print("Číslo je väčšie ako 3 a menšie ako 10.")

if cislo == 3 or cislo == 5:
    print("Číslo je 3 alebo 5.")
~~~

Pozor: `cislo == 3 or 5` nie je správny spôsob porovnania. Napíš celú podmienku na oboch stranách: `cislo == 3 or cislo == 5`. Zátvorky nie sú vždy potrebné, ale pomáhajú sprehľadniť zložitejšie podmienky.

## Úlohy

1. Napíš program, ktorý podľa hodnoty pH určí, či je prostredie kyslé (menej ako 7), neutrálne (7) alebo zásadité (viac ako 7).
2. Vytvor mini kalkulačku: načítaj dve čísla a operáciu (+, -, * alebo /), potom vypíš výsledok. Ošetri delenie nulou.
3. Načítaj tri čísla a vypíš najväčšie. Potom program uprav tak, aby vypísal aj najmenšie a prostredné číslo.
4. Načítaj dĺžky troch strán trojuholníka. Over, či sa dá zostrojiť; ak áno, vypočítaj jeho obvod.
5. Načítaj názov elektrickej jednotky (volt, ohm, ampér, farad alebo henry) a vypíš, akú veličinu meria. Pri neznámej jednotke informuj používateľa.

Ďalšie cvičenia nájdeš v [súbore s úlohami](05_exercises.md).
