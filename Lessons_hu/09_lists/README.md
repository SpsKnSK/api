# Listák

A **lista** több érték egyben, egy változóban. A dobozokkal ellentétben ez egy egész **polc**, ahol minden helynek van sorszáma (**index**), 0-tól kezdve.

```python
mylist = ["alma", "banán", "cseresznye"]
print(mylist[0])  # alma
```

| Művelet | Jelentés |
|---|---|
| `mylist[i]` | az `i`. elem (0-tól számolva) |
| `.append(x)` | `x` hozzáadása a lista **végére** |
| `.insert(i, x)` | `x` beszúrása az `i`. helyre |
| `.remove(x)` | az első `x` értékű elem törlése |
| `.pop()` | az utolsó elem kiemelése és eltávolítása |
| `len(mylist)` | a lista hossza (elemszám) |
| `.sort()` | növekvő sorrendbe rendezi (helyben) |

**Metafora:** a lista olyan, mint egy **polc dobozokkal**, minden doboznak van egy száma (0, 1, 2...), és bármikor tehettek bele, vehettek ki, vagy átrendezhetitek a dobozokat.

## A lecke részei

A részletes tananyag bemutatja a lista műveleteit, az algoritmusos rész pedig a listák gyakorlati feldolgozását. A füzetbe másolandó külön rész ehhez a témához nem tartozik.

- [01 – Alapok](01_basic.md)
- [02 – Részletes tananyag](02_main.md)
- [02a – Algoritmusok listákkal](02a_algorithms.md)
- [03 – Rontsátok el!](03_break_it.md)
- [04 – Kérdések](04_questions.md)
- [05 – Gyakorlófeladatok](05_exercises.md)

[← Vissza a tananyag térképéhez](../00_Terkep_hu.md)
