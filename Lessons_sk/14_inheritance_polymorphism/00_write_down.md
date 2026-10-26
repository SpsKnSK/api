[Späť na mapu](../00_Mapa_sk.md)

> # ✏️ Dedenie a polymorfizmus
>
> **Dedenie**: nova trieda (dieta/podtrieda) ziska vsetky vlastnosti a funkcie uz existujucej triedy (rodica).
>
> ```py
> class Zviera:
>     def __init__(self, meno):
>         self.Meno = meno
>
> class Pes(Zviera):        # Pes dedi od triedy Zviera
>     def Haf(self):
>         print(f"{self.Meno}: Hav!")
>
> pes = Pes("Bodrik")
> pes.Haf()   # zdedil aj Meno, metodu Haf() si pridava sam
> ```
>
> - `class Dieta(Rodic):` — zapis dedenia
> - `super().__init__(...)` — zavola `__init__` rodica, aby sme ho nemuseli pisat znova
> - **Polymorfizmus**: rovnaky nazov funkcie (napr. `PohniSa()`) sa v roznych triedach sprava rozne
>
> **Metafora:** rodičovská trieda je ako **rodinný recept**: každé dieťa dostane základný postup receptu, ale môže pridať vlastné dochutenie (prepísať metódu).