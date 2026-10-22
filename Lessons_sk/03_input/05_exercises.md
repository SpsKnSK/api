🗺️ [Späť na mapu učiva](../../Lessons_sk/00_Mapa_sk.md)

# `input()` – precvičovacie úlohy

Úlohy sú zoradené od jednoduchších po náročnejšie.

## 🟢 Základné úlohy

### 1. Pozdrav

Napíšte program, ktorý sa opýta na meno. Potom sa opýta, koľko máte rokov, a vypíše súhrnnú vetu:

```text
Ahoj [pocetRokov] rocny [meno], vidim, ze ty sedis pred pocitacom
```

### 2. Vizitka

Napíšte program, ktorý zo zadaných údajov vypíše na obrazovku vizitku. Údaje: meno, bydlisko, kontakt.

```text
Meno: [meno]
Bydlisko: [bydlisko]
Kontakt: [kontakt]
```

### 3. Súčet mincí

Vypýtajte od používateľa tri prirodzené čísla, ktoré znamenajú počet 5-, 2- a 1-eurových mincí. Určte a vypíšte celkovú sumu.

Príklad:

```text
Pocet 5 eur: 2
Pocet 2 eur: 3
Pocet 1 eur: 1
To je celkovo 17 eur.
```

## 🟡 Náročnejšie úlohy

### 4. Malá násobilka

Vypíšte malú násobilku pre zadané číslo od 1 do 10. Zatiaľ stačí 10 samostatných príkazov `print`.

```text
Ktorú násobilku vypíšem? 11
1*11=11
2*11=22
3*11=33
...
10*11=110
```

### 5. Nákup ovocia

Cena za kilogram:
- jablká: 0.65 €;
- citróny: 1.2 €;
- pomaranče: 1.5 €.

1. Napíšte program, ktorý vypočíta, koľko peňazí si treba vziať, ak kúpite 1 kg jabĺk, 1.5 kg citrónov a 2 kg pomarančov. Vyskúšajte aj iné množstvá.
2. Opýtajte sa používateľa, koľko peňazí má, a vypočítajte, koľko **celých** kilogramov jabĺk, citrónov a pomarančov si za ne môže kúpiť.

**Pozor:** hmotnosť môže byť desatinné číslo, preto treba použiť `float(input(...))`. Premyslite si aj to, ako budete pracovať s cenami a celkovou sumou.

Hľadanie chýb je v samostatnom súbore: [Pokazte to!](03_break_it.md).
