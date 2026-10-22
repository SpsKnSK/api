# ✏️ Cykly - `while`

**Cyklus:** opakujeme tie isté príkazy.

```py
while podmienka:
    prikazy    # toto je jadro cyklu (blok)
    prikazy    # toto je jadro cyklu (blok)
    prikazy    # toto je jadro cyklu (blok)
    prikazy    # toto je jadro cyklu (blok)
```

`while` opakuje jadro cyklu **dovtedy, kým je podmienka pravdivá**. Po každom kole znovu preverí podmienku.

**Nezabudni:**
1. na konci riadka `while podmienka` je dvojbodka `:`;
2. riadky jadra cyklu sú odsadené;
3. podmienka sa musí raz stať nepravdivou, inak je cyklus nekonečný.

```py
i = 1
while i <= 3:
    print(i)
    i = i + 1
```
Výstup: `1`, `2`, `3`

**Metafora:** `while` je ako **pravidlo spoločenskej hry**: "kým máš peniaze, posuň sa o jedno políčko". Po každom kole sa znova pýtame: platí ešte podmienka? Ak áno, nasleduje ďalšie kolo, ak nie, je koniec.