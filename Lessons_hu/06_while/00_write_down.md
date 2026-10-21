# ✏️ Füzetbe – a `while` ciklus

**Ciklus:** utasítások egy blokkjának ismétlése.

```python
while feltetel:
    utasitasok  # ciklusmag
```

A `while` addig ismétli a ciklusmagot, **amíg a feltétel igaz**. Minden kör után újra ellenőrzi a feltételt.

```python
i = 1
while i <= 3:
    print(i)
    i = i + 1
```

Kimenet: `1, 2, 3`

**Ne feledd:**
1. A `while` sor végén kettőspont (`:`) áll.
2. A ciklusmag sorai behúzással kezdődnek.
3. A ciklusban általában változtatni kell valamin, hogy a feltétel egyszer hamissá váljon.
4. Ha a feltétel sosem lesz hamis, végtelen ciklus keletkezhet.

**Metafora:** a `while` olyan, mint egy **társasjáték szabálya**: "amíg van pénzed, lépj egy mezőt:. Minden kör után újra megkérdezzük: igaz még a feltétel? Ha igen, jön a következő kör, ha nem, vége.