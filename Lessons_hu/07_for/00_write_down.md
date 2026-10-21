## ✏️ Füzetbe – Ciklus: for

**Mire való?** A `for` ciklust akkor használjuk, ha előre tudjuk, milyen értékeken vagy hányszor ismétlünk.

**Metafora:** a `for` olyan, mint egy **névsorolvasás**: előre tudod, kik vannak a listán, és sorban végigmész rajtuk — nem kell magadnak számolgatnod, hogy hányszor lépj.

```python
for i in range(1, 6):
    print(i)
```

**Kimenet:** `1, 2, 3, 4, 5`

**A `range()` legfontosabb alakjai:**

| Kód | Értékek |
|---|---|
| `range(5)` | `0, 1, 2, 3, 4` |
| `range(2, 5)` | `2, 3, 4` |
| `range(1, 10, 2)` | `1, 3, 5, 7, 9` |

A felső határ **nem tartozik bele** a sorozatba. A ciklusmag behúzott blokk.

**Visszafelé számolás:**

```python
for i in range(10, 0, -2):
    print(i)
```

Kimenet: `10, 8, 6, 4, 2`
