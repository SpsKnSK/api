[Späť na mapu](../00_Mapa_sk.md)

> # ✏️ Triedy (`class`)
>
> Trieda je **plán**, inštancia (objekt) je z nej vytvorené **konkrétna vec**.
>
> ```py
> class Macka:
>     def __init__(self, meno, farba) -> None:
>         self.Meno = meno
>         self.Farba = farba
>
>     def Predie(self):
>         print(f"{self.Meno} je {self.Farba} macka a pradie")
>
> cica = Macka("Cilka", "strieborná")   # vytvorenie inštancie - konkrétny objekt
> cica.Predie()
> ```
>
> - `class Nazov:` - vytvorenie triedy (plánu)
> - `__init__(self, ...)` - spustí sa pri každom vytvorené inštancie, nastaví počiatočné vlastnosti
> - `self` - "táto konkrétna inštancia", cez nu pristupujeme k vlastným vlastnostiam a funkciám
> - `self.Vlastnost = hodnota` - nastavenie vlastnosti
> - `__str__(self)` - urcuje, ako bude objekt vyzerat po prevedení na text (`str`) alebo pri výpise
>
> **Metafora:** trieda je ako **forma na sušienky**: samotná forma nie je sušienka, ale každý sušienka z nej dostane rovnaké základné tvar (a pritom ju môžeme ozdobit inak).
