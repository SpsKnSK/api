> ## ✏️ Füzetbe – Változók
>
> **Mi az?** Névvel ellátott doboz a memóriában, amiben egy értéket tárolunk. A neve alapján bármikor előszedhetjük.
>
> **Értékadás:** `nev = ertek` – a `=` **nem** egyenlőség, hanem: "tedd bele!"
> ```py
> kor = 16          # a kor dobozba bekerül a 16
> kor = kor + 1     # kivesszük, hozzáadunk 1-et, visszatesszük -> 17
> ```
>
> | Típus | Jele | Példa |
> |---|---|---|
> | egész szám | `int` | `10`, `-9`, `0` |
> | tizedes szám | `float` | `3.14`, `95.78` |
> | szöveg | `str` | `"alma"`, `'3gomb'`, `'11'`, `"-38"` |
> | logikai | `bool` | `True`, `False` |
>
> **Névadás:** csak betű, szám és `_`; **nem** kezdődhet számmal; nincs benne szóköz és kötőjel; nem lehet foglalt szó (`print`, `input`).
>
> **Fontos műveletek:**
>
> | | | | |
> |-|-|-|-|
> | `+` összeadás | `-` kivonás | `*` szorzás | `/` osztás |
> | `//` egész osztás | `%` maradék | `**` hatvány | `round(a, x)` kerekítés |
>
> **⚠️ A leggyakoribb hiba:** `=` értékadás, `==` összehasonlítás!
> ```py
> x = 5      # betettem az 5-öt
> x == 5     # kérdés: x "dobozban" 5 van? -> True
> ```
>
> **Metafora:** a változó olyan, mint egy **felcímkézett doboz**: a címke a neve, a tartalma az értéke. Ha újat teszünk bele, a régi kiesik — egyszerre csak egy dolog van a dobozban.
>
