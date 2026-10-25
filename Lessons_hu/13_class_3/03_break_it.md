[Vissza a térképhez](../00_Terkep_hu.md)

> # 💥 Rontsátok el!
>
> Mi a hiba ebben a programban?
>
> ```py
> class Hőmérő:
>     def __init__(self):
>         self.celsius = 0
>
> h = Hőmérő()
> h.celsius = -500
> print(h.celsius)
> ```
>
> A program lefut, de fizikailag lehetetlen értéket enged be (-500°C nem létezik, az abszolút nulla -273.15°C). Hogyan lehetne `@property`-vel megvédeni az osztályt ettől?
