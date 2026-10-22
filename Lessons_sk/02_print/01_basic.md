🗺️ [Späť na mapu učiva](../../Lessons_sk/00_Mapa_sk.md) · [Podrobná lekcia](02_main.md)

# 02 – Výpis: `print()`

## Čo sa naučím?

Naučím sa vypisovať na obrazovku text, číslo, premennú a výsledok operácie a meniť spôsob, akým sa výpis zobrazí.

## Krátky príklad

```python
meno = "Anna"
print("Ahoj", meno)
print(1 + 1)
print("Ahoj", "svet", sep="-")
```

**Výstup:**

```text
Ahoj Anna
2
Ahoj-svet
```

- Text píšeme do úvodzoviek, číslo bez nich.
- Namiesto názvu premennej sa vypíše jej hodnota.
- Čiarkou môžeme odovzdať viac hodnôt v jednom volaní `print()`; predvolene sa medzi ne vloží medzera.
- Parameter `sep` určuje oddeľovač medzi hodnotami a `end` text na konci riadka.
- `\n` označuje nový riadok, `\t` tabulátor. Časť za `#` je komentár.

Podrobné vysvetlenia a ďalšie príklady nájdeš v [podrobnej lekcii](02_main.md), úlohy v [zozname precvičovacích úloh](05_exercises.md).
