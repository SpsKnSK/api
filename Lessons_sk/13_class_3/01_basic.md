# Stručný prehľad

[Späť na mapu](../00_Mapa_sk.md)

Táto časť je určená pokročilým a je voliteľná.

> # ✏️ Triedy — hlbšie poznatky
>
> *Voliteľné, pokročilé učivo.*
>
> - `@property` — vlastnost mozeme citat alebo nastavovat, akoby to bol obycajny atribut, ale pritom mozeme vykonat kontrolu alebo vypocet
> - **Triedna premenna** — spolocna pre vsetky instancie (napr. `Pes.pocet_jedincov`)
> - **Instancna premenna** — kazda instancia ma vlastnu (napr. `self.meno`)
> - `@staticmethod` — nema `self` ani `cls`, je to len "pomocna" funkcia v triede
> - `@classmethod` — dostane parameter `cls`, casto ju pouzivame ako alternativny konstruktor
> - `__eq__`, `__add__`, `__lt__` atd. — "magic methods", nimi urcujeme, ako sa trieda sprava pri `==`, `+`, `<`
> - `with` + context manager (`__enter__`, `__exit__`) — automaticky "uprace" (napr. zatvori subor) aj pri chybe
> - `@dataclass` — kratsi sposob zapisu jednoduchych tried na uchovavanie udajov
>
> ```py
> class Teplomer:
>     def __init__(self):
>         self._celsius = 0
>
>     @property
>     def celsius(self):
>         return self._celsius
>
>     @celsius.setter
>     def celsius(self, hodnota):
>         if hodnota < -273.15:
>             raise ValueError("Prilis nizka teplota!")
>         self._celsius = hodnota
>
> t = Teplomer()
> t.celsius = 25      # navonok to vyzera ako obycajny atribut...
> print(t.celsius)    # ...ale v pozadi sa v skutocnosti vola funkcia
> ```
>
> **Metafora:** `@property` je ako **vratnik pri vytahu**: zvonka to vyzera, ze len stlacis tlacidlo (`objekt.celsius`), ale vratnik (setter/getter) medzitym skontroluje, ci tam mozes ist.
