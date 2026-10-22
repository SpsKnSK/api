# Függvények – röviden

A **függvény** egy névvel ellátott kódrészlet, amelyet akkor futtatunk le, amikor meghívjuk. Akkor hasznos, ha egy műveletet többször is el kell végezni, vagy ha a programot kisebb, könnyebben érthető részekre szeretnénk bontani.

```python
def osszead(a, b):
    return a + b

eredmeny = osszead(3, 5)
print(eredmeny)  # 8
```

- `def`: létrehozza, azaz **definiálja** a függvényt.
- `a`, `b`: **paraméterek**, a függvény bemenetei.
- `osszead(3, 5)`: a függvény **meghívása**; a 3 és az 5 az átadott **argumentumok**.
- `return`: visszaad egy értéket a hívás helyére.
- A függvény törzsét behúzással jelöljük.

Fontos: a függvény definíciója önmagában még nem futtatja le a benne lévő műveleteket. Ehhez meg kell hívni.

[Részletes magyarázat és példák →](02_main.md)
