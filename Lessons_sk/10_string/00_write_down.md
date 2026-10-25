🗺️ [Späť na mapu](00_Mapa_sk.md)

> # ✏️ Reťazce (texty)
>
> **Reťazec** je postupnosť znakov. Každý znak má svoj **index** (poradové číslo), ktoré začína od **0**.
>
> ```text
> s  l  o  v  o
> 0  1  2  3  4
> ```
>
> | Operácia | Význam | Príklad (`text = "slovo"`) |
> |---|---|---|
> | `text[i]` | `i`-ty znak | `text[3]` → `"v"` |
> | `text[a:b]` | od `a` po `b` (`b` sa nepočíta) | `text[1:4]` → `"lov"` |
> | `.lower()` / `.upper()` | zmení na malé/veľké písmená | |
> | `.replace(x, y)` | nahradí `x` za `y` | |
> | `.split()` | rozdelí podľa medzier | |
> | `len(text)` | dĺžka reťazca | |
>
> **Metafora:** reťazec je ako **retiazka z korálikov** — každý korálik je jeden znak a každý má svoju menovku: 0, 1, 2, 3... Výraz `[a:b]` vystrihne kus tejto retiazky.
