# Try-except-finally
Slúži na spracovanie chýb. Chyba môže nastať v týchto prípadoch:
- Delenie nulou `print(10/0)`
- Nesprávna konverzia `int("jablko")`
- Sčítanie reťazca so celým číslom: `print("jablko"+10)`

V týchto prípadoch môžeme použiť príkazy `try-except-finally`:
```py
try:
    int('jablko')
except Exception as e:
    print(f"Nastala chyba: {e}")
finally:
    print("Vždy sa vykoná vetva finally")
```
## Generovanie vlastnej chyby pomocou `Exception` 
```py
try:
    raise Exception("Toto je vlastna chyba")
except Exception as e:
    print(f"Nastala chyba: {e}")
```

# Format
[Tu nájdete viac informácií na github.com/SpsKnSK/api](https://github.com/SpsKnSK/api/tree/main/UsefulStuff/08_format.md)

[Tu nájdete viac informácií na w3schools](https://www.w3schools.com/python/python_string_formatting.asp)
## format príkaz

Reťazec vytvoríte takto: `"nejaky text {index_premennej} este nejaky text{index_premennej}"`. Index sa začína od 0, hodnoty zadávame, ako vstupné parametre príkazu `format`.

```py
speedLimit = 130
speed = 110
formatovanyRetazec = "Prekračujete rýchlosť {0} v oblasti s obmedzením na {1}"

retazecNaZobrazenie = formatovanyRetazec.format(speed, speedLimit)

print(retazecNaZobrazenie)
```

## F-formát
Formátovanie môže byť veľmi užitočné v jazyku Python. Na to budete potrebovať:
- `f""` na začiatku reťazca, čím definujete formátovaný reťazec
- `{}` závorky použijete pre premennú alebo hodnotu, ktorú chcete vypísať

```py
speedLimit = 130
speed = 110
print("Prekračujete rýchlosť", speed, "v oblasti s obmedzením na", speedLimit, "km/h")

# Môže sa prepísať na:
print(f"Prekračujete rýchlosť {speed} v oblasti s obmedzením na {speedLimit} km/h")
```

Samozrejme, nie len pri príkaze `print`:
```py
speedLimit = 130
speed = 110

textNaVypis = f"Prekračujete rýchlosť {speed} v oblasti s obmedzením na {speedLimit} km/h"
print(textNaVypis)
```

# ternary operator
Používa sa na priradenie hodnôt na základe podmienky alebo sa dá použiť ako skrátená forma `if`.

```py
premenná = hodnota_ak_pravda if podmienka else hodnota_ak_nepravda
```

```py
a = 0

if 10 > 20:
    a = 20
else:
    a = 10

print(a)

# Môže byť prepísané ako
a = 20 if 10 > 20 else 10
print(a)
```