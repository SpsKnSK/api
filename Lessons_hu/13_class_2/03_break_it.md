[Vissza a térképhez](../00_Terkep_hu.md)

> # 💥 Rontsátok el!
>
> Mi a hiba ebben a programban?
>
> ```py
> class Konyv:
>     def __init__(self, cim, ar):
>         self.cim = cim
>         self.ar = ar
>
> konyv = Konyv("1984", 3500)
> print(konyv)
> ```
>
> A kiírás valami ilyesmi lesz: `<__main__.Konyv object at 0x...>`. Mi hiányzik az osztályból ahhoz, hogy a `print(konyv)` szépen, olvashatóan írja ki az adatokat?
