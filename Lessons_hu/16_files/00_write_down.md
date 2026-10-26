🗺️ [Vissza a térképhez](../00_Terkep_hu.md)

> # ✏️ Fájlkezelés
>
> ```py
> with open("munkafajl.txt", "w") as f:
>     f.write("Ez egy tesztsor 12345")
>
> with open("munkafajl.txt", "r") as f:
>     tartalom = f.read()
>     print(tartalom)
> ```
>
> | Mód | Jelentés |
> |---|---|
> | `r` | csak olvasás |
> | `w` | csak írás (felülírja a fájlt!) |
> | `a` | hozzáfűzés a fájl végéhez |
> | `r+` | írás és olvasás egyszerre |
>
> - `f.read()` — teljes tartalom
> - `f.readline()` — egy sor
> - `f.readlines()` — lista, minden sor egy elem
> - `f.write(szoveg)` — csak `str`-t fogad el! (`str(szam)`-mal alakítsd át)
> - `with open(...) as f:` — a fájl **automatikusan bezárul** a blokk végén, nem kell `f.close()`
>
> **Metafora:** a fájl olyan, mint egy **közös jegyzetfüzet**: ha kinyitod (`open`), írhatsz vagy olvashatsz belőle, de ha elfelejted becsukni (`close`), más program esetleg nem tud hozzáférni. A `with` olyan, mint egy **automata ajtó**: magától becsukódik, amikor kilépsz.
