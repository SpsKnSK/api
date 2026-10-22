# ✏️ `print()`

**Mire jó?** Kiírja a képernyőre azt, amit a zárójelbe írunk: szöveget, számot, változót vagy egy művelet eredményét.

**Alak:** `print(érték1, érték2, sep=" ", end="\n")` – a `sep` és az `end` nem kötelező

| Amit írok | Mit jelent |
|---|---|
| `print("Szia")` | szöveg (idézőjelben!) |
| `print(12)` | szám (idézőjel nélkül) |
| `print(szam)` | a változó **tartalma** |
| `print(a+b)` | előbb számol, aztán kiír |
| `print(a, b)` | a vessző = szóköz a kimenetben |
| `sep="."` | mi kerüljön az értékek **közé** (alapértelmezetten: szóköz) |
| `end=" "` | mi kerüljön a sor **végére** (alapértelmezetten: új sor `\n`) |
| `""` | üres szöveg |
| `\n` | új sor jele |
| `\t` | tabulátor |

**Szám vagy szöveg:**
```py
print(1+1)      # 2   -> összeadás
print("1"+"1")  # 11  -> összeragasztás
```

**Példa:**
```py
print(192, 168, 100, 1, sep=".")
print("Szia", end=" ")
print("Peter!")
```
a képernyőn
```
192.168.100.1
Szia Peter!
```

**Metafora:** a `print()` olyan, mint egy **kirakat**: amit kiállítasz benne (a zárójelbe írsz), azt a vásárló is látja (a képernyőn jelenik meg).
