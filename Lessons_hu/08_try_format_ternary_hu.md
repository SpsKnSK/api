# try-except-finally
A hibák kezelésére szolgál. Hiba merülhet fel a következő esetekben:
- 0-val osztunk `print(10/0)`
- rossz konvertálás `int("alma")`
- szöveg egész számmal való összeadása: `print("alma"+10)`

Ilyen esetekben használhatjuk a `try-except-finally` parancsokat:
```py
try:
    int('alma')
except Exception as e:
    print(f"Hiba tortent: {e}")
finally:
    print("Finally branch will be always executed")
```

## Saját hiba generálása `Exception` segítségeével
```py
try:
    raise Exception("Ez egy saját hiba")
except Exception as e:
    print(f"Hiba tortent: {e}")
```

# format
[Itt találtok hozzá több leírást](https://www.w3schools.com/python/python_string_formatting.asp)
## format parancs

A `str`-t elkészítitek a következőképpen: `"valami szoveg {valtozo_indexe} meg valami szoveg {valtozo_indexe}"`. Az index 0-tól indul, és a `format` parancs bemenő paramétereiként használjátok

```py
speedLimit = 130
speed = 110
formattedString = "You are going {0} in a {1} area"

stringToDisplay = formattedString.format(speedLimit, speed)

print(stringToDisplay)
```

## f-format
A formátozás nagyon hasznos tud lenni a pythonban, ami szükséges hozzá:
- `f""`- `str` elején az `f` azt jelenti, hogy a `str` formátozott lesz
- `{}` kapcsos zárójelbe teszed a változót, értéket, amit ki szeretnél íratni
```py
speedLimit = 130
speed = 110
print("You are going", speed, "in a", speedLimit, "area")

# can be rewritten to:
print(f"You are going {speed} in a {speedLimit} area")
```
persze, nem csak `print`nél lehet használni:
```py
speedLimit = 130
speed = 110

toBePrintedOut = f"You are going {speed} in a {speedLimit} area"
print(toBePrintedOut)
```

# ternary operator
Amikor értéket akartok megadni valamilyen feltétel alapján, vagy egy soros if-ként is lehet rá utalni

```py
valtozo = ertek_ha_igaz if feltetel else ertek_ha_hamis
```

```py
a = 0

if 10 > 20:
    a = 20
else:
    a = 10

print(a)

# can be rewritten as
a = 20 if 10 > 20 else 10
print(a)
```
