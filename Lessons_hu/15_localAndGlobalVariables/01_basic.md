🗺️ [Vissza a térképhez](../../Lessons_hu/00_Terkep_hu.md) · [Részletes tananyag](02_main.md)

# Globális és lokális változók – alapok

- **Globális változó:** függvényen kívül jön létre, és a függvényből is olvasható.
- **Lokális változó:** függvényen belül jön létre, és csak ott használható.
- Ha egy függvényben egy globális változóval azonos nevű változót értékadással hozunk létre, az a függvény saját lokális változója lesz.
- A `global` kulcsszóval jelezhetjük, hogy a függvény a globális változót módosítsa.
- A paraméterekkel és visszatérési értékkel dolgozó függvények általában könnyebben követhetők, mint azok, amelyek a globális állapotot módosítják.

```python
x = "awesome"

def myfunc():
    x = "fantastic"
    print(x)

myfunc()
print(x)
```

**Kimenet:**
```text
fantastic
awesome
```

A függvényen belüli `x` nem változtatja meg a függvényen kívüli `x` értékét.

[Részletes magyarázat és példák →](02_main.md)
