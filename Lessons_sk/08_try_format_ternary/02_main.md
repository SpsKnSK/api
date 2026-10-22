🗺️ [Späť na mapu](../../Lessons_sk/00_Mapa_sk.md) · [Základy](01_basic.md) · [Precvičovacie úlohy](05_exercises.md)

# ✏️ Extra – try, format, ternary

Táto lekcia **nie je povinné učivo**, ale zbierka užitočných doplnkových trikov. Nevadí, ak ju teraz preskočíte — môžete sa k nej kedykoľvek vrátiť.

## try-except-finally

Slúži na spracovanie chýb. Chyba môže nastať napríklad v týchto prípadoch:

- delíme nulou: `10 / 0`;
- nesprávna konverzia: `int("jablko")`;
- pokúsime sa sčítať reťazec s celým číslom: `"jablko" + 10`.

V takýchto prípadoch môžeme chybu spracovať pomocou `try-except`:

```python
try:
    int("jablko")
except Exception as e:
    print(f"Nastala chyba: {e}")
```

V bloku `try` je operácia, ktorú skúšame vykonať; `except` sa vykoná, ak nastane zodpovedajúci typ chyby. Ak je to možné, zachytávaj konkrétny typ chyby, napríklad `ValueError` pri prevode na číslo. Všeobecné `Exception` môže zachytiť aj chyby, ktoré sme nechceli spracovať.

Blok `finally` sa vykoná bez ohľadu na to, či chyba nastala:

```python
try:
    cislo = int("12")
    print(cislo)
except ValueError:
    print("Neplatné číslo!")
finally:
    print("Operácia sa skončila.")
```

Výstup:
```text
12
Operácia sa skončila.
```

Ak zmeníš `int("12")` na `int("jablko")`, zobrazí sa správa z `except` a potom aj správa z `finally`.

### Vytvorenie vlastnej chyby pomocou `raise`

```python
try:
    raise Exception("Toto je vlastná chyba")
except Exception as e:
    print(f"Nastala chyba: {e}")
```

Výstup:
```text
Nastala chyba: Toto je vlastná chyba
```

## format a f-string

Ďalšie informácie: [poznámky o formátovaní v projekte](../../UsefulStuff/08_format.md) a [W3Schools – Python String Formatting](https://www.w3schools.com/python/python_string_formatting.asp).

### Metóda `format()`

Označenia `{0}`, `{1}` v texte odkazujú na index argumentov metódy `format()`. Indexovanie sa začína od 0.

```python
rychlostny_limit = 130
rychlost = 110
sablona = "Ideš rýchlosťou {0} km/h, limit je {1} km/h."
print(sablona.format(rychlost, rychlostny_limit))
```

Výstup: `Ideš rýchlosťou 110 km/h, limit je 130 km/h.`

### f-string

Písmeno `f` sa píše pred úvodzovky a premenná alebo výraz, ktorý chceme vložiť do textu, sa píše do zložených zátvoriek.

```python
rychlostny_limit = 130
rychlost = 110
print("Ideš rýchlosťou", rychlost, "km/h, limit je", rychlostny_limit, "km/h.")
print(f"Ideš rýchlosťou {rychlost} km/h, limit je {rychlostny_limit} km/h.")
```

Výstup:
```text
Ideš rýchlosťou 110 km/h, limit je 130 km/h.
Ideš rýchlosťou 110 km/h, limit je 130 km/h.
```

F-string nemusíme použiť iba v `print()`; vytvorený text môžeme uložiť aj do premennej.

```python
meno = "Anna"
sprava = f"Ahoj, {meno}!"
print(sprava)
```

Výstup: `Ahoj, Anna!`

### Formátovanie čísel

Zápis `:.2f` určuje dve desatinné miesta.

```python
cena = 12.5
pomer = 0.387481
print(f"Cena: {cena:.2f}")
print(f"Pomer: {pomer:.1%}")
```

Výstup:
```text
Cena: 12.50
Pomer: 38.7%
```

## Ternary operator – podmienený výraz

Ternary (jednoriadkový if) vyberá jednu z dvoch hodnôt podľa podmienky. Má tvar:

```python
premenná = hodnota_ak_pravda if podmienka else hodnota_ak_nepravda
```

Rovnaký príklad s bežným vetvením:

```python
a = 0
if 10 > 20:
    a = 20
else:
    a = 10
print(a)
```

Výstup: `10`.

Skrátený zápis:

```python
a = 20 if 10 > 20 else 10
print(a)
```

Výstup: `10`.

Príklad:

```python
cislo = 7
parne_alebo_neparne = "párne" if cislo % 2 == 0 else "nepárne"
print(parne_alebo_neparne)
```

Výstup: `nepárne`.

Ternary je vhodný na jednoduchý výber medzi dvoma možnosťami. Pri viacerých vetvách alebo zložitej logike je lepšie použiť klasickú štruktúru `if-elif-else`.
