[Vissza a térképhez](../00_Terkep_hu.md)

> # ✏️ Öröklődés és polimorfizmus
>
> **Öröklődés**: egy új osztály (gyerek/alosztály) megkapja egy már létező osztály (szülő) minden tulajdonságát és függvényét.
>
> ```py
> class Allat:
>     def __init__(self, nev):
>         self.Nev = nev
>
> class Kutya(Allat):        # Kutya örököl Allat-tól
>     def Ugat(self):
>         print(f"{self.Nev}: Vau!")
>
> kutya = Kutya("Bodri")
> kutya.Ugat()   # a Nev-et is örökölte, az Ugat()-ot maga adja hozzá
> ```
>
> - `class Gyerek(Szulo):` — öröklés jelölése
> - `super().__init__(...)` — meghívja a szülő `__init__`-jét, hogy ne kelljen újraírni
> - **Polimorfizmus**: ugyanaz a függvénynév (pl. `Mozdulj()`) más-más osztályokon más-más módon viselkedik
>
> **Metafora:** a szülő osztály olyan, mint egy **családi recept**: minden gyerek megkapja az alaprecept lépéseit, de bármelyikük hozzáadhat saját ízesítést (felülírhatja a függvényt).