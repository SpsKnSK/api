# 06 – Cyklus while: precvičovacie úlohy

Rieš úlohy postupne. Najprv si premysli, čo treba opakovať a čo spôsobí ukončenie cyklu.

## 🟢 Základné úlohy

1. Vypíš čísla od 1 do 10.
2. Vypíš párne čísla od 2 do 20.
3. Odpočítavaj od 10 do 1 a potom vypíš: `Štart!`
4. Päťkrát vypíš `Python`.
5. Začni od 0 a zvyšuj číslo o 3, kým nebude väčšie ako 15.

## 🟡 Precvičovanie

6. Načítaj číslo a vypíš všetky čísla od 1 po zadané číslo.
7. Pýtaj si heslo, kým používateľ nezadá správne slovo `tajomstvo`.
8. Postupne načítavaj čísla a sčítavaj ich. Zadanie čísla 0 ukončí načítavanie. Na konci vypíš súčet.
9. Vytvor hru na hádanie čísla, ktorá pýta ďalší tip, kým tip nebude 7.

## ⭐ Dobrovoľné výzvy

10. Načítaj kladné celé číslo. Ak používateľ zadá 0 alebo záporné číslo, pýtaj si ho znova, kým nezadá správnu hodnotu.
11. Vytvor jednoduché menu, ktoré vypíše: `1 – Pozdrav`, `2 – Rozlúčka`, `0 – Koniec`. Menu sa má zobrazovať opakovane, kým používateľ nevyberie 0.

## 🔵 Precvičovanie: `break` a `continue`

12. Napíš cyklus, ktorý počíta od 1 nahor, ale pomocou `break` sa zastaví pri čísle 4. Riadok za cyklom má vypísať: `Koniec!`.
13. Vypíš čísla od 1 do 10, ale pomocou `continue` vynechaj číslo 5.
14. **Nájdi chybu!** Prečo sa tento program nezastaví? Oprav ho tak, aby sa hodnota `i` zvyšovala aj pri použití `continue`.
    ```python
    i = 1
    while i <= 5:
        if i == 3:
            continue
        print(i)
        i = i + 1
    ```


## Kontrola

Pri každom riešení skontroluj:
- Je podmienka cyklu správna?
- Mení sa v cykle niečo, vďaka čomu sa raz skončí?
- Sú riadky jadra cyklu odsadené na rovnakej úrovni?
