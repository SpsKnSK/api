🗺️ [Späť na mapu učiva](../../Lessons_sk/00_Mapa_sk.md) · [Podrobnejšia lekcia: If–Elif–Else](02_main.md)

# 05 – Vetvenie: if

## Čo sa naučím?

Pomocou `if` vyberiem medzi možnosťami. Program podľa podmienky vykoná rôzne príkazy.

## Prečo to potrebujem?

Predstav si kontrolu lístka: ak má návštevník aspoň 18 rokov, môže vstúpiť na film s vekovým obmedzením; inak vstúpiť nemôže.

## Krátky príklad

~~~python
vek = 17

if vek >= 18:
    print("Môžeš vstúpiť.")
else:
    print("Ešte nemôžeš vstúpiť.")
~~~

**Výstup:**

~~~text
Ešte nemôžeš vstúpiť.
~~~

### Čo sa deje po riadkoch?

- `vek = 17`: uložíme vek do premennej.
- `if vek >= 18:`: program overí, či je vek aspoň 18.
- Prvý `print` sa vykoná iba vtedy, ak je podmienka pravdivá.
- `else` označuje druhú možnosť, keď je podmienka nepravdivá.

**Všimni si:**
- Za riadkom `if` a `else` je dvojbodka.
- Príkazy vo vetve sú odsadené.
- `>=` porovnáva, `=` priraďuje hodnotu.

## Najprv tipuj!

Ešte nespúšťaj program. Zapíš si, čo vypíše.

~~~python
cislo = 8

if cislo > 10:
    print("A")
else:
    print("B")

print("C")
~~~

1. Čo program vypíše a v akom poradí?
2. Prečo?
3. Čo sa zmení, keď nastavíš `cislo = 12`?

Potom program spusti a porovnaj výsledok so svojím tipom.

## Vyskúšaj samostatne

### 1. Vedená úloha
Doplň podmienku tak, aby program vypísal „kladné“, ak je číslo väčšie ako nula, inak vypísal „nie je kladné“.

~~~python
cislo = 5

if __________________:
    print("kladné")
else:
    print("nie je kladné")
~~~

Vyskúšaj hodnoty 5, 0 a -3.

### 2. Samostatná úloha
Načítaj celé číslo a vypíš, či je **párne** alebo **nepárne**. Číslo je párne, ak je zvyšok po delení dvoma rovný nule.

### 3. Samostatná úloha
Načítaj vek používateľa. Ak má aspoň 18 rokov, vypíš „Dospelý“, inak „Ešte nie je dospelý“.

### ⭐ Dobrovoľná výzva
Načítaj teplotu a vypíš „mrzne“, ak je nižšia ako 0, inak „nemrzne“. Uprav program tak, aby pri presnej hodnote 0 vypísal osobitnú správu.

Ďalšie úlohy: [If – precvičovacie úlohy](05_exercises.md).
