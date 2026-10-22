# ✏️ If, elágazás

**Mire jó?** A program **elágazik**: csak akkor fut le egy kódrészlet, ha egy feltétel igaz.

```py
if feltetel1:
    utasitasok1
elif feltetel2:
    utasitasok2
else:
    utasitasok_else
```

| Rész | Kell? | Mikor fut le |
|---|---|---|
| `if` | **mindig** | ha a feltétele igaz |
| `elif` | nem | ha a fentiek hamisak, de ez igaz (akárhány lehet) |
| `else` | nem | ha **egyik** feltétel sem volt igaz |

**⚠️ 3 dolog, amit el ne felejts:**
1. a sor végén **kettőspont** `:`
2. az alatta lévő sorok **beljebb** (behúzás, Tab)
3. `==` az összehasonlítás, `=` csak értékadás

**Blokk:** az `if` alatt beljebb írt utasítások csoportja. Együtt futnak le, vagy együtt maradnak ki. A behúzás** jelöli ki, meddig tart.
```py
if jegy == 1:
    print("Gratulalok!")   # \_ blokk: az if-hez tartozik
    print("Ugyes vagy!")   # /
print("Vege")              # ez mindig lefut
```

**Csak az első igaz ág fut le!** Ha `jegy = 2`, a 2-es ág lefut, a többit meg se nézi.

**Feltételek:**

| | | | |
|-|-|-|-|
| `==` egyenlő | `!=` nem egyenlő | `<` kisebb | `>` nagyobb |
| `<=` kisebb-egyenlő | `>=` nagyobb-egyenlő | | |

**Összekapcsolás:** `and` = mindkettő igaz · `or` = legalább az egyik igaz · `not` = megfordítja
```py
if (kor > 12) and (kor < 20):
    print("tini")
```

**Metafora:** az `if` olyan, mint egy **útelágazás**: a program odaér, megnézi a táblát (feltétel), és aszerint megy tovább az egyik vagy a másik úton — csak **egy** ágon indulhat el.