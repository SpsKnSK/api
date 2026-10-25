# Rövid áttekintés

[Vissza a térképhez](../00_Terkep_hu.md)

Ez a rész haladóknak szól, és opcionális.

> # ✏️ Osztályok — mélyebb ismeretek
>
> *Opcionális, haladó tananyag.*
>
> - `@property` — úgy nézhetjük meg/állíthatjuk be egy tulajdonságot, mintha sima attribútum lenne, de közben ellenőrzést, számítást is végezhetünk
> - **Osztályváltozó** — minden példány között közös (pl. `Kutya.egyedek_szama`)
> - **Példányváltozó** — minden objektumnak saját (pl. `self.nev`)
> - `@staticmethod` — nincs `self`/`cls`, csak "kényelmi" függvény az osztályon belül
> - `@classmethod` — `cls` paramétert kap, gyakran alternatív konstruktorként használjuk
> - `__eq__`, `__add__`, `__lt__` stb. — "magic method"-ok, ezekkel definiáljuk, hogyan viselkedjen az osztály `==`, `+`, `<` esetén
> - `with` + context manager (`__enter__`, `__exit__`) — automatikusan "takarít" (pl. fájlt zár be) hiba esetén is
> - `@dataclass` — rövidebb módja az egyszerű, adatokat tároló osztályok írásának
>
> ```py
> class Homero:
>     def __init__(self):
>         self._celsius = 0
>
>     @property
>     def celsius(self):
>         return self._celsius
>
>     @celsius.setter
>     def celsius(self, ertek):
>         if ertek < -273.15:
>             raise ValueError("Túl alacsony!")
>         self._celsius = ertek
>
> h = Homero()
> h.celsius = 25       # úgy nézhet ki, mint egy sima attribútum...
> print(h.celsius)      # ...pedig valójában egy függvény fut le mögötte
> ```
>
> **Metafora:** a `@property` olyan, mint egy **portás egy liftnél**: kívülről úgy tűnik, csak megnyomod a gombot (`objektum.celsius`), de a portás (a setter/getter függvény) közben ellenőrzi, hogy szabad-e odamenned.
