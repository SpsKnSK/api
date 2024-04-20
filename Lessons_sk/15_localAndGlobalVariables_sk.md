# Globálne premenné

Premenné vytvorené mimo funkcií sa nazývajú **globálne premenné**.

Globálne premenné môžu používať všetky časti kódu:
- Sú dostupné **vo vnútri** funkcií.
- Sú dostupné aj **mimo** funkcií.
```py
x = "úžasný"

def mojafunkcia():
  print(f"Python je {x}")

mojafunkcia()
```
Výstup:
```
Python je úžasný
```

## Rozdiel medzi globálnymi a lokálnymi premennými
Ak vytvoríte premennú s rovnakým názvom vo vnútri funkcie, táto premenná bude **lokálna** a bude dostupná iba **vnútri** funkcie. Premenná s rovnakým názvom mimo funkcie zostane globálna a bude mať pôvodnú hodnotu.

```py
x = "úžasný"

def mojafunkcia():
  x = "fantastický"
  print(f"Python je {x}")

mojafunkcia()

print(f"Python je {x}")
```
Výstup:
```
Python je fantastický
Python je úžasný
```

V tomto príklade sme **globálnu** premennú `x` nastavili na hodnotu `úžasný`, potom sme ju vo funkcii `mojafunkcia` zmenili na hodnotu `fantastický` a neskôr sme ju znova použili
