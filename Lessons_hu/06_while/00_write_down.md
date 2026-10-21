# ✏️ Füzetbe – a `while` ciklus

**Ciklus:** utasítások egy blokkjának ismétlése.

**Képzeld el így:** egy poharat töltesz vízzel. Amíg a pohár nincs tele, töltesz még bele egy kicsit, majd újra megnézed, tele van-e. A `while` ciklus is így működik: ellenőrzi a feltételt, végrehajtja a feladatot, aztán újra ellenőriz. Amikor a feltétel már hamis (például a pohár tele van), megáll.

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
