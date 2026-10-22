🗺️ [Späť na mapu](../00_Mapa_sk.md)

> # ✏️ `input()`
>
> **Na čo slúži?** Načíta text z klávesnice, ktorý uložíme do premennej.
>
> **Tvar:** `premenna = input("otázka pre používateľa")`
>
> | Čo napíšem | Čo to robí |
> |---|---|
> | `input()` | čaká, kým niečo napíšeme + Enter |
> | `input("Kolko mas rokov? ")` | najprv vypíše otázku, potom čaká (ušetríme `print`) |
> | `meno = input(...)` | zadaný údaj sa uloží do premennej `meno` |
>
> **⚠️ Najdôležitejšie:** `input()` vracia **vždy text (string)**, aj keď zadáme číslo!
>
> | Čo napíšem | Výsledok |
> |---|---|
> | `cislo = input(...)` | `"50"` – text, nedá sa s ním počítať |
> | `cislo = int(input(...))` | `50` – celé číslo |
> | `cena = float(input(...))` | `1.5` – desatinné číslo |
>
> ```py
> cislo = input("Zadaj cislo: ")   # zadáme: 50
> print(cislo + 12)   # CHYBA! text + číslo nejde
>
> cislo = int(input("Zadaj cislo: "))
> print(cislo + 12)   # 62
> ```
>
> **Ako sa rozhodnúť:**
> ```
> Chcem s tym pocitat?  --> ano, cele cislo    --> int(input(...))
>                       --> ano, desatinne     --> float(input(...))
>                       --> nie (meno, mesto)  --> input(...)
> ```
>
> **Metafora:** `input()` je ako **poštová schránka**: čokoľvek do nej hodíme, program dostane len **obálku** (text), a ak to chceme použiť ako číslo, musíme ju sami "rozbaliť" (`int()`, `float()`).
