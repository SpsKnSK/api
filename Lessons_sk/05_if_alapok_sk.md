🗺️ [Späť na mapu učiva](00_Mapa_sk.md) · [Podrobnejšia lekcia: If–Elif–Else](05_if_sk.md)

# 05 – Vetvenie: if – základy

## Čo sa naučím?

Na konci lekcie budem vedieť pomocou `if` vybrať jednu z dvoch možností. Program podľa podmienky vykoná rôzne príkazy.

## Prečo to potrebujem?

Predstav si kontrolu lístkov do kina: ak má návštevník aspoň 18 rokov, môže vojsť na film označený 18+. Ak je mladší, nemôže.

Programy robia podobné rozhodnutia často: napríklad zisťujú, či je číslo kladné alebo či má používateľ dostatočný vek.

## Pozrime sa na krátky príklad!

```python
vek = 17

if vek >= 18:
    print("Môžeš vstúpiť.")
else:
    print("Ešte nemôžeš vstúpiť.")
```

**Výstup:**

```text
Ešte nemôžeš vstúpiť.
```

### Riadok po riadku

- **`vek = 17`**: uložíme vek osoby do premennej.
- **`if vek >= 18:`**: program overí, či je vek aspoň 18. Operátor `>=` znamená „väčší alebo rovný“.
- **`print("Môžeš vstúpiť.")`**: tento riadok sa vykoná iba vtedy, keď je podmienka pravdivá.
- **`else:`**: označuje druhú možnosť — čo sa má stať, keď podmienka nie je pravdivá.
- **`print("Ešte nemôžeš vstúpiť.")`**: tento riadok sa vykoná, keď je vek menší ako 18.

**Všimni si:**
- Za riadkom `if` aj `else` je dvojbodka (`:`).
- Príkazy patriace do vetvy sú odsadené. Tomu hovoríme **odsadenie**.
- `>=` porovnáva hodnoty, zatiaľ čo `=` priraďuje hodnotu premennej.

## Najprv hádaj, potom spusti!

Zatiaľ program nespúšťaj. Napíš, čo podľa teba vypíše.

```python
cislo = 8

if cislo > 10:
    print("A")
else:
    print("B")

print("C")
```

1. Čo program vypíše a v akom poradí?
2. Prečo vypíše práve tieto znaky?
3. Čo sa zmení, ak nastavíš `cislo = 12`?

Teraz program spusti a porovnaj výsledok so svojím odhadom.

## Vyskúšaj si to samostatne!

### 1. Úloha s pomocou

Doplň program tak, aby vypísal `kladné`, ak je číslo väčšie ako nula, a inak vypísal `nie je kladné`.

```python
cislo = 5

if __________________:
    print("kladné")
else:
    print("nie je kladné")
```

Vyskúšaj hodnoty 5, 0 a -3.

### 2. Samostatná úloha

Načítaj celé číslo a vypíš, či je **párne** alebo **nepárne**. Pomôcka: číslo je párne, ak je zvyšok po delení dvoma rovný nule.

### 3. Samostatná úloha

Načítaj vek používateľa. Ak má aspoň 18 rokov, vypíš `Dospelý`; inak vypíš `Ešte nie je dospelý`.

### ⭐ Dobrovoľná výzva

Načítaj teplotu a vypíš:
- `mrzne`, ak je menšia ako 0;
- `nemrzne`, ak je 0 alebo vyššia.

Potom uprav program tak, aby pri teplote presne 0 vypísal samostatnú správu.

Ďalšie úlohy nájdeš v [podrobnejšej lekcii If – úlohy](../Exercies/05_if/feladatok_hu.md).

## Over si, či tomu rozumieš!

Skús odpovedať bez pozerania na príklad.

1. Čo znamená podmienka za slovom `if`?
2. Čo sa vykoná vo vetve `else`?
3. Prečo musia byť príkazy vo vetvách odsadené?

**Miniúloha:** Čo vypíše tento program?

```python
body = 10

if body >= 10:
    print("Podarilo sa")
else:
    print("Skús znova")
```

## 💥 Pokazte to!

### Východiskový kód: kontrola lístka do kina

Skopírujte tento program, spustite ho a potom v ňom zámerne niečo pokašlite. Najprv skúste odhadnúť, čo sa stane!

```python
vek = 17

if vek >= 18:
    print("Môžeš vstúpiť.")
else:
    print("Ešte nemôžeš vstúpiť.")
```

Nápady:
- Odstráňte dvojbodku: `if vek >= 18`
- Odstráňte odsadenie pred riadkom v bloku `if`.
- Použite v bloku rôzne odsadenie.
- Nahraďte porovnanie `==` priradením `=`: `if vek = 18:`
- Pridajte podmienku za `else`: `else vek < 18:`

Prečítajte si chybové hlásenie:
- Ako sa chyba volá a na ktorý riadok ukazuje?
- Ktorú chybu Python oznámi okamžite?
- Kedy sa program spustí, ale výsledok bude nesprávny?
