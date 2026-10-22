🗺️ [Späť na mapu učiva](../../Lessons_sk/00_Mapa_sk.md) · [Podrobnejšia lekcia](02_main.md)

# 03 – Vstup: `input()`

## Čo si mám zapamätať?

- `input()` načíta údaj z klávesnice a vráti ho ako text.
- Otázka v zátvorkách sa zobrazí na obrazovke a program potom čaká na odpoveď.
- Ak chceme so zadanou hodnotou počítať, prevedieme ju:
  - `int(input(...))` – na celé číslo;
  - `float(input(...))` – na desatinné číslo.
- Ak načítavame meno, mesto alebo iný text, stačí `input(...)`.

## Krátky príklad

```python
meno = input("Ako sa voláš? ")
vek = int(input("Koľko máš rokov? "))

print("Ahoj", meno)
print("O 10 rokov budeš mať", vek + 10, "rokov.")
```

Ak používateľ zadá meno `Dani` a vek `16`, program vypíše:

```text
Ahoj Dani
O 10 rokov budeš mať 26 rokov.
```

Viac vysvetlení: [podrobná lekcia](02_main.md). Precvičovanie: [úlohy](05_exercises.md).
