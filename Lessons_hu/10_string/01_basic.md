# Stringek – rövid áttekintés

A **string** (szöveg) karakterek sorozata. A karakterek indexe 0-tól indul.

```python
szoveg = "szöveg"
print(szoveg[0])    # s
print(szoveg[3])    # v
print(szoveg[1:4])  # zöv
```

A szeletelésnél a kezdő index benne van, a záró index már nincs benne.

| Művelet | Mire való? |
|---|---|
| `szoveg[i]` | egy karakter elérése |
| `szoveg[a:b]` | részstring kivágása |
| `.lower()` / `.upper()` | kis-/nagybetűs változat |
| `.replace(x, y)` | szövegrész cseréje |
| `.split()` | szöveg feldarabolása listára |
| `.index(x)` / `.count(x)` | keresés / előfordulások száma |
| `len(szoveg)` | karakterek száma |
| `elvalaszto.join(lista)` | szövegek összefűzése elválasztóval |
| `x in szoveg` | tartalmazás vizsgálata |

A stringen `for` ciklussal karakterenként végig lehet menni. Részletek: [02 – Részletes tananyag](02_main.md).
