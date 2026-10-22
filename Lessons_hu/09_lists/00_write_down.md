# ✏️ Listák

A **lista** több érték egyben, egy változóban. A bozokkal ellentétben ez egy egész **polc**, ahol nden helynek van sorszáma (**index**), 0-tól kezdve.

```py
mylist = ["alma", "banán", "cseresznye"]
print(mylist[0])   # "alma"
```

| Művelet | Jelentés |
|---|---|
| `mylist[i]` | az `i`. elem (0-tól számolva) |
| `.append(x)` | `x` hozzáadása a lista **végére** |
| `.insert(i, x)` | `x` beszúrása az `i`. helyre |
| `.remove(x)` | az első `x` értékű elem törlése |
| `.pop()` | az utolsó elem kiemelése és távolítása |
| `len(mylist)` | a lista hossza (elemszám) |
| `.sort()` | növekvő sorrendbe rendezi (helyben) |

**Metafora:** a lista olyan, mint egy **polc dobozokkal**, minden doboznak van egy száma (0, 1, 2...), és bármikor tehettek bele, vehettek ki, vagy átrendezhetitek a dobozokat.