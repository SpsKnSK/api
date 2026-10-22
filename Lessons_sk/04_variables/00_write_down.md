> # ✏️ Premenné
>
> **Čo to je?** Menom označená krabica v pamäti, do ktorej uložíme jednu hodnotu. Podľa mena ju vieme kedykoľvek vybrať.
>
> **Priradenie:** `meno = hodnota` – `=` **nie je** rovnosť, ale: "vlož do toho!"
> ```py
> vek = 16          # do krabice vek sa vloží 16
> vek = vek + 1     # vyberieme, pripočítame 1, vložíme späť -> 17
> ```
>
> | Typ | Značka | Príklad |
> |---|---|---|
> | celé číslo | `int` | `10`, `-9`, `0` |
> | desatinné číslo | `float` | `3.14`, `95.78` |
> | text | `str` | `"jablko"`, `'3tlacitko'` |
> | logická hodnota | `bool` | `True`, `False` |
>
> **Názvy:** iba písmená, číslice a `_`; **nesmie** začínať číslom; bez medzier a spojovníkov; nesmie to byť rezervované slovo (`print`, `input`).
>
> **Dôležité operácie:**
>
> | | | | |
> |-|-|-|-|
> | `+` súčet | `-` rozdiel | `*` súčin | `/` delenie |
> | `//` celočíselné delenie | `%` zvyšok | `**` umocňovanie | `round(a, x)` zaokrúhlenie |
>
> **⚠️ Najčastejšia chyba:** `=` je priradenie, `==` je porovnanie!
> ```py
> x = 5      # vložil som 5
> x == 5     # otázka: je vnútri 5? -> True
> ```
>
> **Metafora:** premenná je ako **krabica s nálepkou**: nálepka je jej meno, obsah je jej hodnota. Ak do nej vložíme niečo nové, staré vypadne — v krabici je naraz iba jedna vec.
