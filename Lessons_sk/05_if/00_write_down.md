# ✏️ If, vetvenie

**Na čo slúži?** Program sa **rozvetví**: časť kódu sa vykoná iba vtedy, ak je podmienka pravdivá.

```py
if podmienka1:
    prikazy1
elif podmienka2:
    prikazy2
else:
    ine_prikazy
```

| Časť | Povinná? | Kedy sa vykoná |
|---|---|---|
| `if` | **vždy** | ak je jeho podmienka pravdivá |
| `elif` | nie | ak sú predošlé nepravdivé, ale táto je pravdivá (môže ich byť viac) |
| `else` | nie | ak **žiadna** podmienka nebola pravdivá |

**⚠️ 3 veci, na ktoré nesmieš zabudnúť:**
1. na konci riadku **dvojbodka** `:`
2. riadky pod ním **odsadené** (odsadenie, Tab)
3. `==` je porovnanie, `=` je iba priradenie

**Blok:** skupina príkazov odsadených pod `if`. Vykonajú sa spolu, alebo spolu vypadnú. **Odsadenie** určuje, kiaľ blok siaha.
```py
if znamka == 1:
    print("Gratulujem!")   # \_ blok: patrí k if
    print("Si šikovný!")   # /
print("Koniec")            # toto sa vykoná vždy
```

**Vykoná sa iba prvá pravdivá vetva!** Ak `znamka = 2`, vykoná sa vetva pre 2, ostatné sa ani nepozrú.

**Podmienky:**

| | | | |
|-|-|-|-|
| `==` rovné | `!=` nerovné | `<` menšie | `>` väčšie |
| `<=` menšie-rovné | `>=` väčšie-rovné | | |

**Spojenie:** `and` = obe pravdivé · `or` = aspoň jedna pravdivá · `not` = obráti
```py
if (vek > 12) and (vek < 20):
    print("tínedžer")
```

**Metafora:** `if` je ako **rázcestie**: program tam dorazí, pozrie sa na tabuľu (podmienku) a podľa nej pôjde ďalej jednou alebo druhou cestou — vydať sa môže iba **jednou**.