# ✏️ Ciklusok - `while`

**Ciklus:** ugyanazokat az utasításokat ismételjük.

```py
while feltetel:
    utasitasok    # ez a ciklusmag (blokk)
    utasitasok    # ez a ciklusmag (blokk)
    utasitasok    # ez a ciklusmag (blokk)
    utasitasok    # ez a ciklusmag (blokk)
```

A `while` addig ismétli a ciklusmagot, **amíg a feltétel igaz**. Minden kör után újra megvizsgálja a feltételt.

**Ne feledd:**
1. a `while feltetel` sor végén kettőspont `:` áll;
2. a ciklusmag sorai beljebb kezdődnek;
3. a feltételnek egyszer hamissá kell válnia, különben a ciklus végtelen.

```py
i = 1
while i <= 3:
    print(i)
    i = i + 1
```
Kimenet: `1`, `2`, `3`

**Metafora:** a `while` olyan, mint egy **társasjáték szabálya**: "amíg van pénzed, lépj egy mezőt". Minden kör után újra megkérdezzük: igaz még a feltétel? Ha igen, jön a következő kör, ha nem, vége.