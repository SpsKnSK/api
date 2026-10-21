## ✏️ Do zošita – Vetvenie (if)

**Na čo slúži?** Pomocou `if` sa program rozhoduje podľa podmienky. Ak je podmienka pravdivá (`True`), vykonajú sa príkazy vo vetve `if`; inak sa môže vykonať vetva `else`.

~~~python
vek = 17

if vek >= 18:
    print("Môžeš vstúpiť.")
else:
    print("Ešte nemôžeš vstúpiť.")
~~~

**Porovnávacie operátory:**

| Operátor | Význam |
|---|---|
| `<` | menší |
| `<=` | menší alebo rovný |
| `==` | rovný |
| `>` | väčší |
| `>=` | väčší alebo rovný |
| `!=` | nerovný |

**Logické operátory:**
- `and` – a: všetky podmienky musia byť pravdivé.
- `or` – alebo: pravdivá musí byť aspoň jedna podmienka.
- `not` – negácia: obráti pravdivostnú hodnotu.

**Dôležité pravidlá:**
- Riadok s `if`, `elif` alebo `else` sa končí dvojbodkou (`:`).
- Príkazy patriace do vetvy musia byť odsadené.
- `==` porovnáva hodnoty; `=` priraďuje hodnotu premennej.
- V jednej konštrukcii `if/elif/else` sa vykoná najviac jedna vetva.
