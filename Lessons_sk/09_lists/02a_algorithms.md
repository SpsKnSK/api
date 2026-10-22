🗺️ [Späť na mapu učiva](../../Lessons_sk/00_Mapa_sk.md) · [Podrobná lekcia o zoznamoch](02_main.md)

# Algoritmy so zoznamami

V tejto časti sa neučíme len jednotlivé metódy zoznamu, ale riešime úlohy pomocou zoznamov. Príklady vychádzajú z premenných, podmienok a cyklov, ktoré už poznáš.

## Naplnenie zoznamu náhodnými číslami

### 1. variant: cyklus a `randint()`

Funkcia `randint(dolna, horna)` sa volá bez bodky a vráti náhodné celé číslo vrátane dolnej aj hornej hranice.

```python
from random import randint

dlzka_zoznamu = 5
dolna_hranica = 10
horna_hranica = 20

cisla = []
index = 0

while index < dlzka_zoznamu:
    cisla.append(randint(dolna_hranica, horna_hranica))
    index += 1

print(cisla)
```

Názvy premenných treba písať vždy rovnako: Python rozlišuje malé a veľké písmená. Zvyšovanie premennej `index` zabezpečí, že sa cyklus `while` raz skončí.

### 2. variant: `sample()` a `range()`

Funkcia `sample()` vyberá náhodnú vzorku bez opakovania z danej postupnosti. Funkcia `range(dolna, horna)` nezahŕňa hornú hranicu.

```python
from random import sample

dolna_hranica = 1
horna_hranica = 50
pocet_prvkov = 7

cisla = sample(range(dolna_hranica, horna_hranica + 1), pocet_prvkov)
print(cisla)
```

Pripočítame `+ 1`, pretože v tomto príklade chceme povoliť aj číslo 50. Funkcia `sample()` nie je vhodná, ak chceme vybrať viac prvkov, než koľko rôznych hodnôt je v rozsahu.

Ak sa čísla môžu opakovať, použi cyklus s `randint()`.

## Najmenší a najväčší prvok, priemer

### Pomocou vstavaných funkcií

```python
cisla = [5, 6, 19, 1, 954]

print("Zoznam:", cisla)
print("Najmenšie:", min(cisla))
print("Najväčšie:", max(cisla))
print("Priemer:", sum(cisla) / len(cisla))
```

Výstup:

```text
Zoznam: [5, 6, 19, 1, 954]
Najmenšie: 1
Najväčšie: 954
Priemer: 197.0
```

Funkcie `min()`, `max()`, `sum()` a `len()` sa volajú bez bodky: zoznam im odovzdávame ako parameter.

### Index minima a maxima

Funkcie `min()` a `max()` vracajú hodnotu, nie index. Index hodnoty zistíme pomocou metódy zoznamu `.index()`.

```python
cisla = [5, 6, 19, 1, 954]

najmensie = min(cisla)
najvacsie = max(cisla)

print("Index najmenšieho:", cisla.index(najmensie))  # 3
print("Index najväčšieho:", cisla.index(najvacsie))  # 4
```

Ak sa najmenšia alebo najväčšia hodnota vyskytuje viackrát, `.index()` vráti index prvého výskytu.

## Výmena dvoch prvkov

V Pythone môžeme hodnoty dvoch premenných alebo dvoch prvkov zoznamu vymeniť jediným priradením.

```python
ovocie = ["jablko", "hruška", "slivka"]
print(ovocie)

ovocie[0], ovocie[1] = ovocie[1], ovocie[0]
print(ovocie)  # ['hruška', 'jablko', 'slivka']
```

Ak zadanie vyžaduje výmenu podľa hodnôt, najprv môžeme nájsť indexy pomocou `.index()`. Pred výmenou sa uisti, že hľadané prvky sú v zozname.

## Rozdelenie párnych a nepárnych čísel do dvoch zoznamov

Pomocou zvyšku po delení (`%`) zistíme, či je číslo párne.

```python
cisla = [12, 7, 4, 9, 16, 3]
parne = []
neparne = []

for cislo in cisla:
    if cislo % 2 == 0:
        parne.append(cislo)
    else:
        neparne.append(cislo)

print("Párne:", parne)      # [12, 4, 16]
print("Nepárne:", neparne)  # [7, 9, 3]
```

Cyklus skontroluje každý prvok a podmienka `if` rozhodne, do ktorého zoznamu patrí.

## Oddelenie písmen a číslic z textu

Cez reťazec môžeme prechádzať cyklom `for` znak po znaku. Metóda `.isdigit()` zisťuje, či je znak číslicou.

```python
text = "Az678em12b87er"
pismena = []
cislice = []

for znak in text:
    if znak.isdigit():
        cislice.append(znak)
    else:
        pismena.append(znak)

print(pismena)  # ['A', 'z', 'e', 'm', 'b', 'e', 'r']
print(cislice)  # ['6', '7', '8', '1', '2', '8', '7']
```

V tomto príklade ukladáme číslice ako znaky reťazca. Ak potrebujeme celé čísla, môžeme použiť aj prevod `int(znak)`.

## Kroky algoritmu

Ak má program nájsť minimum a maximum z čísel zadaných používateľom, všeobecný plán je:

1. Vytvor prázdny zoznam.
2. Načítaj čísla a platné hodnoty pridávaj metódou `.append()`.
3. Skontroluj, či zoznam nie je prázdny.
4. Použi funkcie `min(zoznam)` a `max(zoznam)`.
5. Ak potrebuješ aj indexy, zisti ich pomocou `zoznam.index(hodnota)`.

Načítanie vstupu a ošetrenie nesprávne zadaných údajov sa dajú precvičovať samostatne; náročnejšie úlohy so zoznamami na to nadväzujú.
