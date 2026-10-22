# 📋 Precvičovacie úlohy

Úlohy sú zoradené od jednoduchších po náročnejšie. Téma je voliteľná; ak je niečo nové, najprv si prečítaj [podrobné učivo](02_main.md).

## 1. Základy f-stringu

Vytvor premenné `meno` a `vek` a pomocou f-stringu vypíš napríklad: `Anna má 16 rokov.`

## 2. Vlož do textu výsledok výpočtu

Ulož súčet dvoch čísel do premennej a vypíš ho pomocou f-stringu v tvare `12 + 8 = 20`. Zmeň čísla a over, či výstup zodpovedá novým hodnotám.

## 3. Formátované čísla

Ulož desatinné číslo do premennej a vypíš ho s dvoma desatinnými miestami. Potom zobraz pomer medzi 0 a 1 ako percento s jedným desatinným miestom.

## 4. Ternary: párne alebo nepárne

Priraď hodnotu premennej `cislo`. Pomocou ternary výrazu vyber text `"párne"` alebo `"nepárne"` a vypíš ho. Vyskúšaj párne aj nepárne číslo.

## 5. Spracovanie nesprávneho čísla

Načítaj text a skús ho previesť na celé číslo. Ak používateľ nezadá číslo, program sa nemá ukončiť chybovým hlásením; vypíš zrozumiteľnú informáciu. Použi konkrétne ošetrenie chyby.

## 6. Vlastná chyba

Ak je počet bodov mimo rozsahu 0 až 100, vyvolaj chybu pomocou `raise ValueError("Počet bodov musí byť od 0 do 100!")`. Ošetri ju pomocou `try-except`.

## 7. Načítanie dvoch celých čísel – kombinovaná úloha

Pýtaj si od používateľa dve celé čísla a opakuj načítanie, kým nezadá dve platné celé čísla. Potom ich porovnaj a vypíš, ktoré je väčšie. Použi všetky tri nástroje:

- blok `try-except`;
- formátovanie (f-string);
- ternary výraz.

Premysli si aj to, čo sa má stať, ak sú obe čísla rovnaké.

## ⭐ 8. Dobrovoľná výzva

Načítaj sumu a zobraz ju s dvoma desatinnými miestami. Ak sa vstup nedá previesť na číslo, ošetri chybu. Pri úspešnom vstupe použi ternary výraz na vypísanie, či je suma aspoň 100.
