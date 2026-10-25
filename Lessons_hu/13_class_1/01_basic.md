# Rövid áttekintés

[Vissza a térképhez](../00_Terkep_hu.md)

Ez a rész bemutatja az osztályok és objektumok alapjait.

> # ✏️ Osztályok (`class`)
>
> Az osztály egy **tervrajz**, a példány (objektum) az abból elkészített **konkrét dolog**.
>
> ```py
> class Macska:
>     def __init__(self, nev, szin) -> None:
>         self.Nev = nev
>         self.Szin = szin
>
>     def Dorombol(self):
>         print(f"{self.Nev} a {self.Szin} macska dorombol")
>
> cirmi = Macska("Cirmi", "ezüst")   # példányosítás - konkrét objektum
> cirmi.Dorombol()
> ```
>
> - `class Nev:` — osztály (tervrajz) létrehozása
> - `__init__(self, ...)` — lefut minden példányosításkor, ez állítja be a kezdő tulajdonságokat
> - `self` — "ez a konkrét példány", ezen keresztül érjük el a saját tulajdonságokat/függvényeket
> - `self.Tulajdonsag = ertek` — tulajdonság beállítása
> - `__str__(self)` — meghatározza, hogyan nézzen ki az objektum, ha szöveggé (`str`) alakítjuk / kiírjuk
>
> **Metafora:** az osztály olyan, mint a **kekszsütő forma**: maga a forma nem ehető keksz, de minden vele kisütött keksz ugyanazt az alapformát kapja (viszont ízesíthetjük külön-külön).
