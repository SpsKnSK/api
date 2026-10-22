🗺️ [Späť na mapu učiva](../../Lessons_sk/00_Mapa_sk.md) · [Späť na prehľad témy](README.md)

# Funkcia `input()`

Načítanie údajov, textu (reťazca), ktorý potom môžeme uložiť do premennej.

```py
>>> text = input()
jablko
>>> print(text)
jablko
```

Python umožňuje pomocou príkazu `input()` poslať používateľovi správu o tom, aký údaj potrebujeme.

Správu zapíšeme do zátvoriek príkazu `input` medzi jednoduché alebo dvojité úvodzovky. Program pri spustení zobrazí správu a potom čaká na zadané údaje. Ušetríme tak jeden príkaz `print`!

## Príklad

```py
>>> text = input("Kolko je hodin? ")
Kolko je hodin? 9
>>> print(text)
9
```

## `input()` – čísla (celé čísla)

`cislo = input("Zadaj číslo!")`

Hodnota premennej `cislo` po zadaní: `"50"`.

Prečo to nestačí, ak chceme počítať? Skúsime k premennej `cislo` pridať `12`.

### Opravený kód

```py
cislo = int(input("Zadaj číslo!"))
print(cislo + 12)
```

Ak používateľ zadá `50`, výstup bude `62`. Funkcia `int()` prevedie hodnotu na celé číslo.

Na načítanie desatinného čísla použijeme `float()`:

```py
cena = float(input("Zadaj cenu: "))
print(cena * 2)
```

Ak používateľ zadá `1.5`, výstup bude `3.0`.

**Dôležité:** `int(input(...))` očakáva celé číslo. Ak zadáme písmeno alebo `1.5`, prevod vyvolá chybu. Pre desatinné číslo použijeme `float(input(...))`.

Otázky, hľadanie chýb a úlohy sú v samostatných súboroch: [otázky](04_questions.md), [pokazte to](03_break_it.md), [precvičovacie úlohy](05_exercises.md).
