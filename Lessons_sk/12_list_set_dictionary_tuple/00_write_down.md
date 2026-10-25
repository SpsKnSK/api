> # ✏️ Zoznam, množina, slovník, n-tica
>
> štyri typy **kolekcií**, každý má inú "osobnost":
>
> | Typ | Znak | Poradie? | Môžu sa opakovat? | Dá sa menit? |
> |---|---|---|---|---|
> | `list` | `[]` | áno (index) | áno | áno |
> | `set` | `{}` | nie | **nie** | áno |
> | `dict` | `{kľúč: hodnota}` | áno (kľúč) | kľúč nie, hodnota áno | áno |
> | `tuple` | `()` | áno (index) | áno | **nie** |
>
> ```py
> zoznam = ['jablko', 'hruška']      # má poradie, dá sa indexovat aj menit
> mnozina = {'jablko', 'hruška'}     # nemá poradie, nemá duplicity
> slovnik = {'meno': 'Anna'}         # kľúč -> hodnota
> ntica = (10, 20)                   # ako zoznam, ale nedá sa menit
> ```
>
> **Metafora:**
> - **Zoznam** = **očíslované polica**: môžeš z nej brat, pridávať aj presúvať veci.
> - **Množina** = **vrece s jedinečnými guľôčkami**: poradie nie je dôležité a dve rovnaké tam nezostanú.
> - **Slovník** = **telefónny zoznam**: nehľadá podla poradia, ale podla **mena** (kľúč -> hodnota).
> - **N-tica** = **zapečatená škatula**: co do nej raz vloží, to už nevymení.
