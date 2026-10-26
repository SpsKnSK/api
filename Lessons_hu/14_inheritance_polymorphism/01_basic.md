# Öröklődés és polimorfizmus – alapok

## Mit érdemes megjegyezni?

- **Öröklődés:** egy új osztály átveheti egy meglévő osztály tulajdonságait és metódusait.
- **Szülőosztály és alosztály:** a szülőben közös tulajdonságokat és működést helyezünk el; az alosztály további tulajdonságokat adhat hozzá, vagy felülírhat egy metódust.
- **`super()`:** segítségével elérhetjük a szülőosztály metódusait, például meghívhatjuk a szülő `__init__` metódusát.
- **Polimorfizmus:** ugyanaz a metódushívás különböző objektumoknál eltérő viselkedést eredményezhet.

## Rövid példa

```python
class Jarmu:
    def mozog(self):
        print("Mozog")

class Hajo(Jarmu):
    def mozog(self):
        print("Úszik")

jarmu = Jarmu()
hajo = Hajo()

jarmu.mozog()
hajo.mozog()
```

Kimenet:

```text
Mozog
Úszik
```

A részletes magyarázatokat, ábrákat és további példákat a [02 – Részletes tananyag](02_main.md) tartalmazza.
