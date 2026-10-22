# Stringműveletek – gyors áttekintés

A táblázat utolsó oszlopában kattintható hivatkozás vezet a részletes magyarázathoz és példához a [02_main.md](02_main.md) fájlban.

| Művelet | Mit ad vissza / mire való? | Részletes magyarázat a 02_main.md fájlban |
|---|---|---|
| `text[i]` | az adott indexű karakter | [Indexelés és szeletelés](02_main.md#mi-az-a-string) |
| `text[a:b]` | részstring; a `b` index már nincs benne | [Indexelés és szeletelés](02_main.md#mi-az-a-string) |
| `for karakter in text` | végigjárja a string összes karakterét | [Karakterenkénti bejárás](02_main.md#karakterenkenti-bejaras-for-ciklussal) |
| `text.lower()` | kisbetűs változat | [`.lower()`](02_main.md#lower) |
| `text.upper()` | nagybetűs változat | [`.upper()`](02_main.md#upper) |
| `text.replace(old, new)` | cserével létrehozott új string | [`.replace()`](02_main.md#replace-from-to) |
| `text.split()` | szóközök mentén feldarabolt lista | [`.split()`](02_main.md#split) |
| `text.split(".")` | a megadott elválasztó mentén feldarabolt lista | [Darabolás adott karakter mentén](02_main.md#split---darabolas-adott-karakter-menten) |
| `text.index(x)` | az első előfordulás indexe; hiányzó értéknél `ValueError` | [`.index()`](02_main.md#indexsubstring) |
| `text.count(x)` | előfordulások száma | [`.count()`](02_main.md#count-substring) |
| `len(text)` | karakterek száma | [`len()`](02_main.md#lentext) |
| `separator.join(parts)` | stringek összefűzése elválasztóval | [`join()` és számok összefűzése](02_main.md#elvalasztojoinstringcollection) |
| `x in text` | `True`, ha `x` megtalálható a stringben | [Tartalmazás vizsgálata](02_main.md#in--tartalmazas-vizsgalata) |
| `list(text)` | karakterek listája | [String mint kollekció](02_main.md#str-mint-kollekcio) |

## Rövid példák

```python
szoveg = "Python nyelv"
print(szoveg.lower())           # python nyelv
print(szoveg.replace("nyelv", "programozás"))  # Python programozás
print(" ".join(["Jó", "napot"])) # Jó napot
```

A `join()` elválasztója az a string, amelyen a metódust meghívjuk. Számokat előbb `str()`-rel szöveggé kell alakítani. A [részletes tananyagban](02_main.md) további példákat találsz.
