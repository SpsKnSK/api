[Vissza a térképhez](../00_Terkep_hu.md)

> # ✏️ Osztályok — haladó (`__repr__`, `__dict__`, JSON)
>
> *Opcionális, haladó tananyag.*
>
> - `__str__(self)` — felhasználóbarát kiírás (`print(objektum)`)
> - `__repr__(self)` — fejlesztőbarát, részletes kiírás (listákban ez jelenik meg)
> - `objektum.__dict__` — az objektum tulajdonságai szótárként
> - `json.dump(adat, fajl)` / `json.load(fajl)` — mentés/betöltés JSON fájlba
> - `Osztaly(**szotar)` — szótárból objektumot csinál ("szétcsomagolás")
>
> ```py
> class Konyv:
>     def __init__(self, cim, ar):
>         self.cim = cim
>         self.ar = ar
>     def __repr__(self):
>         return f"Konyv(cim='{self.cim}', ar={self.ar})"
>
> konyv = Konyv("1984", 3500)
> print(konyv.__dict__)          # {'cim': '1984', 'ar': 3500}
> ujKonyv = Konyv(**konyv.__dict__)  # visszaalakítás objektummá
> print(ujKonyv)
> ```
>
> **Metafora:** a `__dict__` olyan, mintha az objektumot **kicsomagolnánk egy dobozból**: minden tulajdonsága egy címkézett rekeszben van, amit könnyen elmenthetünk (JSON-be), majd később ugyanúgy vissza is csomagolhatunk.
