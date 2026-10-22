🗺️ [Vissza a tananyag térképéhez](../../Lessons_hu/00_Terkep_hu.md) · [Részletes tananyag](02_main.md)

# 09 – Listák: alapok

## Mit kell tudni a listákról?

A lista több értéket tárol egyetlen változóban. Az elemek sorrendben állnak, és **indexszel** érhetők el. Az indexelés 0-tól indul.

```python
gyumolcsok = ["alma", "körte", "szilva"]
print(gyumolcsok[0])  # alma
print(gyumolcsok[2])  # szilva
print(len(gyumolcsok))  # 3
```

A listát bejárhatjuk `for` ciklussal, és új elemeket adhatunk hozzá.

```python
pontszamok = [12, 8, 15]
pontszamok.append(10)

for pont in pontszamok:
    print(pont)
```

## Kétféle hívási forma

Egyelőre nem kell ismerned az osztályokat. Elég megkülönböztetni ezt a két, gyakran használt formát:

- **Ponttal hívott lista-metódus:** a listán keresztül hívjuk, például `lista.append(érték)`. A metódus a lista művelete.
- **Pont nélkül hívott függvény:** a függvény neve után zárójelben adjuk meg a listát, például `len(lista)`, `min(lista)` vagy `sorted(lista)`.

```python
szamok = [7, 2, 9]

szamok.append(4)       # metódus: módosítja a listát
print(len(szamok))     # függvény: visszaadja a lista hosszát
print(min(szamok))     # függvény: visszaadja a legkisebb értéket
print(sorted(szamok))  # függvény: rendezett új listát ad
```

Ne próbálj minden különbséget most megtanulni az objektumokról és osztályokról. Egyelőre a hívás alakját és a működését figyeld meg.

## Ezt gyakorold először!

1. Készíts egy három elemből álló listát, és írasd ki a második elemét.
2. Cseréld le az egyik elem értékét.
3. Adj hozzá egy új elemet az `.append()` segítségével.
4. Írasd ki az elemszámot a `len()` segítségével.
5. Járd be a listát `for` ciklussal, és minden elemet külön sorban írj ki.

További példák: [részletes tananyag](02_main.md) és [listás algoritmusok](02a_algorithms.md).
