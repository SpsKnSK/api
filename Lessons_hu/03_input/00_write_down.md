🗺️ [Vissza a térképhez](../00_Terkep_hu.md)

> # ✏️ `input()`
>
> **Mire jó?** Szöveget olvas be a billentyűzetről, amit elmentünk egy változóba.
>
> **Alak:** `valtozo = input("kérdés a felhasználónak")`
>
> | Amit írok | Mit csinál |
> |---|---|
> | `input()` | vár, amíg beírunk valamit + Enter |
> | `input("Hany eves vagy? ")` | előbb kiírja a kérdést, aztán vár (megspórolunk egy `print`-et) |
> | `nev = input(...)` | a beírt adat a `nev` változóba kerül |
>
> **⚠️ A legfontosabb:** az `input()` **mindig szöveget (string)** ad vissza, akkor is, ha számot írunk be!
>
> | Amit írok | Eredmény |
> |---|---|
> | `szam = input(...)` | `"50"` – szöveg, nem lehet vele számolni |
> | `szam = int(input(...))` | `50` – egész szám |
> | `magassag = float(input(...))` | `1.5` – tizedes szám |
>
> ```py
> szam = input("Adj meg egy szamot: ")   # beírjuk: 50
> print(szam + 12)   # HIBA! szoveg + szam nem megy
>
> szam = int(input("Adj meg egy szamot: "))
> print(szam + 12)   # 62
> ```
>
> **Így dönts:**
> ```
> Szamolni akarok vele?  --> igen, egesz szam  --> int(input(...))
>                        --> igen, tizedes     --> float(input(...))
>                        --> nem (nev, varos)  --> input(...)
> ```
>
> **Metafora:** az `input()` olyan, mint egy **postaláda**: bármit dobnak bele, a program csak egy **borítékot** (szöveget) kap, amit ha számként akarunk használni, nekünk kell "kibontani" (`int()`, `float()`).
