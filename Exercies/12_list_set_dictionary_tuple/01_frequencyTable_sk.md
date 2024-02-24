# SK
# Príklad frekvenčnej tabuľky
V nasledujúcom príklade vyriešime úlohu, kde zobrazíme používateľovi frekvenciu jednotlivých písmen v jednom výroku. Každý krok bude okomentovaný, čo robíme a prečo, na konci dôjdeme k jednému možnému riešeniu, kde využijeme aj to, čo sme doteraz naučili (funkcie, slovníky, zoznamy, množiny...).

# SK

Máme jednu vetu: `"Pista siel pre 2 litre mlieka, ale kupil chlieb. Pisti si so sebou nevzal vela penazi."`, zistime, koľkokrát sa v nej vyskytuje každé písmeno.

## 1. krok
**Vypíšme** znaky vety jeden po druhom:
```py
veta = "Pista siel pre 2 litre mlieka, ale kupil chlieb. Pisti si so sebou nevzal vela penazi."
for pismeno in veta:
    print(pismeno)
```

## 2. krok
Nájdime **unikátne** znaky vo vete:
```py
veta = "Pista siel pre 2 litre mlieka, ale kupil chlieb. Pisti si so sebou nevzal vela penazi."
for pismeno in set(veta):
    print(pismeno)
```

## 3. krok
Stanovte, **koľkokrát sa** daný znak vyskytuje v vete:
```py
veta = "Pista siel pre 2 litre mlieka, ale kupil chlieb. Pisti si so sebou nevzal vela penazi."
for znak in set(veta):
    print(f"{znak}\t{veta.count(znak)}")
```

## 4. krok
Stanovte, **koľko percent** predstavuje toto číslo voči všetkým znakom:
```py
veta = "Pista siel pre 2 litre mlieka, ale kupil chlieb. Pisti si so sebou nevzal vela penazi."
for pismeno in set(veta):
    print(f"{pismeno}\t{veta.count(pismeno)}\t{100*veta.count(pismeno)/len(veta):0.2f}%")
```

## 5. krok
Zobrazte **len písmená**:
```py
veta = "Pista siel pre 2 litre mlieka, ale kupil chlieb. Pisti si so sebou nevzal vela penazi."

for pismeno in set(veta):
    if pismeno.isalpha():
        print(f"{pismeno}\t{veta.count(pismeno)}\t{100*veta.count(pismeno)/len(veta):0.2f}%")
```
# SK

## 6. krok
Zobrazte **len malé písmená**:
```py
veta = "Pista siel pre 2 litre mlieka, ale kupil chlieb. Pisti si so sebou nevzal vela penazi."
novaVeta = ""
for pismeno in veta.lower():
    if pismeno.isalpha():
        novaVeta += pismeno
veta = novaVeta
for pismeno in set(veta):
    print(f"{pismeno}\t{veta.count(pismeno)}\t{100*veta.count(pismeno)/len(veta):0.2f}%")
```
Toto môžeme zapísať pomocou **list comprehension** nasledovne:
```py
veta = "Pista siel pre 2 litre mlieka, ale kupil chlieb. Pisti si so sebou nevzal vela penazi."
veta = "".join([znak for znak in veta.lower() if znak.isalpha() ])

for znak in set(veta):
    print(f"{znak}\t{veta.count(znak)}\t{100*veta.count(znak)/len(veta):0.2f}%")
```

## 7. krok
Keďže nie je isté, či chceme vždy len vypísať, vytvorme slovník, kde kľúčom je znak a hodnotou je zoznam obsahujúci počet výskytov a pomer voči dĺžke celého textu.
```py
veta = "Pista siel pre 2 litre mlieka, ale kupil chlieb. Pisti si so sebou nevzal vela penazi."
veta = "".join([znak for znak in veta.lower() if znak.isalpha()])

slovnik = {}

for pismeno in set(veta):
    slovnik.update({pismeno: [veta.count(pismeno), 100 * veta.count(pismeno) / len(veta)]})
print(slovnik)

# Výpis kľúča a hodnoty
for pismeno, hodnoty in slovnik.items():
    print(pismeno, hodnoty)

# V kontexte
for pismeno, hodnoty in slovnik.items():
    print(f"Znak {pismeno} sa v texte vyskytuje {hodnoty[0]}-krát, čo je {hodnoty[1]:0.2f}% ")
```
```py
# trochu extra :)
class farby:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def VypisModrou(menovka: str) -> None:
    print(f"{farby.OKBLUE}{menovka}{farby.ENDC}")


def VytvorFrekvencnuTabulku(veta: str) -> dict[str, list[int, float]]:
    veta = "".join([pismeno for pismeno in veta.lower() if pismeno.isalpha()])
    slovnik = {pismeno: [veta.count(pismeno), 100 * veta.count(pismeno) / len(veta)] for pismeno in veta}
    return slovnik


def VypisFrekvencnuTabulku(frekvencna_tabulka: dict[str, list[int, float]]) -> None:
    print(f"{farby.BOLD}{farby.OKCYAN}znak\tpocet\tpomer{farby.ENDC}")
    for kluc, hodnota in frekvencna_tabulka.items():
        print(f"{kluc}\t{hodnota[0]}\t{hodnota[1]:0.2f}%")


mojaVeta ="Pista siel pre 2 litre mlieka, ale kupil chlieb. Pisti si so sebou nevzal vela penazi."
frekvencna_tabulka = VytvorFrekvencnuTabulku(mojaVeta)

VypisModrou("Nahodne prvky v mnozine")
VypisFrekvencnuTabulku(frekvencna_tabulka)

VypisModrou("Prvky zoradene podla abecedy")
frekvencna_tabulka = dict(sorted(frekvencna_tabulka.items()))
VypisFrekvencnuTabulku(frekvencna_tabulka)

VypisModrou("Prvky zoradene podla poctu vyskytov")
frekvencna_tabulka = dict(sorted(frekvencna_tabulka.items(), key=lambda item: item[1][0], reverse=True))
VypisFrekvencnuTabulku(frekvencna_tabulka)
```