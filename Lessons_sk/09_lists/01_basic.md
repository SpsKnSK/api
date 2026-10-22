🗺️ [Späť na mapu učiva](../../Lessons_sk/00_Mapa_sk.md) · [Podrobná lekcia](02_main.md)

# 09 – Zoznamy: základy

## Čo treba vedieť o zoznamoch?

Zoznam uchováva viac hodnôt v jednej premennej. Prvky majú svoje poradie a pristupujeme k nim pomocou **indexu**, ktorý začína od 0.

```python
ovocie = ["jablko", "hruška", "slivka"]
print(ovocie[0])  # jablko
print(ovocie[2])  # slivka
print(len(ovocie))  # 3
```

Zoznam môžeme prechádzať cyklom `for` a pridávať doň nové prvky.

```python
body = [12, 8, 15]
body.append(10)

for bod in body:
    print(bod)
```

## Dva spôsoby volania

Kým sa nebudeme podrobne učiť triedy, stačí rozlišovať tieto dva bežné zápisy:

- **Metóda zoznamu volaná s bodkou:** voláme ju cez zoznam, napríklad `zoznam.append(hodnota)`. Ide o operáciu zoznamu.
- **Funkcia volaná bez bodky:** za názov funkcie dáme do zátvoriek zoznam, napríklad `len(zoznam)`, `min(zoznam)` alebo `sorted(zoznam)`.

```python
cisla = [7, 2, 9]

cisla.append(4)       # metóda: zmení zoznam
print(len(cisla))     # funkcia: vráti dĺžku zoznamu
print(min(cisla))     # funkcia: vráti najmenšiu hodnotu
print(sorted(cisla))  # funkcia: vráti nový zoradený zoznam
```

Zatiaľ sa nemusíš učiť všetky podrobnosti o objektoch a triedach. Všímaj si tvar volania a to, čo daný príkaz robí.

## Najprv si precvič!

1. Vytvor zoznam s tromi prvkami a vypíš jeho druhý prvok.
2. Zmeň hodnotu jedného prvku.
3. Pridaj nový prvok pomocou `.append()`.
4. Vypíš počet prvkov pomocou `len()`.
5. Prejdi zoznam cyklom `for` a vypíš každý prvok na samostatný riadok.

Ďalšie príklady: [podrobná lekcia](02_main.md) a [algoritmy so zoznamami](02a_algorithms.md).
