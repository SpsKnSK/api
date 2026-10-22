🗺️ [Vissza a tananyag térképéhez](../../Lessons_hu/00_Terkep_hu.md) · [Részletesebb tananyag](02_main.md)

# 03 – Bemenet: `input()`

## Mit kell megjegyeznem?

- Az `input()` a billentyűzetről olvas be adatot, és az eredményt szövegként adja vissza.
- A zárójelbe írt kérdés megjelenik a képernyőn, majd a program megvárja a választ.
- Ha a beolvasott értékkel számolni szeretnénk, alakítsuk át:
  - `int(input(...))` – egész számhoz;
  - `float(input(...))` – tizedes számhoz.
- Ha nevet, várost vagy más szöveget kérünk be, elég az `input(...)`.

## Rövid példa

```python
nev = input("Hogy hívnak? ")
kor = int(input("Hány éves vagy? "))

print("Szia", nev)
print("10 év múlva", kor + 10, "éves leszel.")
```

Például, ha a felhasználó a `Dani` nevet és a `16` életkort adja meg, a program ezt írja ki:

```text
Szia Dani
10 év múlva 26 éves leszel.
```

További magyarázat: [részletes tananyag](02_main.md). Gyakorlás: [feladatok](05_exercises.md).
