# ✏️ `print()`

**Na čo slúži?** Vypíše na obrazovku to, čo napíšeme do zátvoriek: text, číslo, premennú, výsledok operácie.

**Tvar:** `print(hodnota1, hodnota2, sep=" ", end="\n")` – `sep` a `end` nie sú povinné

| Čo napíšem | Čo to znamená |
|---|---|
| `print("Ahoj")` | text (v úvodzovkách!) |
| `print(12)` | číslo (bez úvodzoviek) |
| `print(cislo)` | **obsah** premennej |
| `print(a+b)` | najprv počíta, potom vypíše |
| `print(a, b)` | čiarka = medzera vo výstupe |
| `sep="."` | čo má byť **medzi** hodnotami (predvolene: medzera) |
| `end=" "` | čo má byť na **konci** riadku (predvolene: nový riadok `\n`) |
| `""` | prázdny reťazec |
| `\n` | znak nového riadku |
| `\t` | tabulátor |

**Číslo vs. text:**
```py
print(1+1)      # 2   -> sčítanie
print("1"+"1")  # 11  -> zlepenie
```

**Príklad:**
```py
print(192, 168, 100, 1, sep=".")
print("Ahoj", end=" ")
print("Peter!")
```
na obrazovke
```
192.168.100.1
Ahoj Peter!
```

**Metafora:** `print()` je ako **výklad obchodu**: čo tam vystavíš (napíšeš do zátvoriek), to uvidí zákazník (uvidí sa na obrazovke).
