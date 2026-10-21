# ✏️ Do zošita – cyklus `while`

**Cyklus:** opakovanie bloku príkazov.

**Predstav si to takto:** napĺňaš pohár vodou. Kým pohár nie je plný, prileješ trochu vody a potom znova skontroluješ, či je už plný. Tak funguje aj cyklus `while`: skontroluje podmienku, vykoná úlohu a potom ju skontroluje znova. Keď podmienka prestane platiť (napríklad pohár je plný), cyklus sa zastaví.

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
