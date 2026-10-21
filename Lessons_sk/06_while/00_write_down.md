# ✏️ Do zošita – cyklus `while`

**Cyklus:** opakovanie bloku príkazov.

```python
while podmienka:
    prikazy  # jadro cyklu
```

Cyklus `while` opakuje jadro cyklu **dovtedy, kým je podmienka pravdivá**. Po každom kole podmienku znova skontroluje.

```python
i = 1
while i <= 3:
    print(i)
    i = i + 1
```

Výstup: `1, 2, 3`

**Nezabudni:**
1. Riadok `while` sa končí dvojbodkou (`:`).
2. Príkazy jadra cyklu sú odsadené.
3. V cykle treba často meniť premennú, aby sa podmienka raz stala nepravdivou.
4. Ak podmienka nikdy nebude nepravdivá, vznikne nekonečný cyklus.
