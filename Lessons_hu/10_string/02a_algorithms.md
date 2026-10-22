# Stringműveletek – gyors áttekintés

| Művelet | Mit ad vissza / mire való? |
|---|---|
| `text[i]` | az adott indexű karakter |
| `text[a:b]` | részstring; a `b` index már nincs benne |
| `text.lower()` | kisbetűs változat |
| `text.upper()` | nagybetűs változat |
| `text.replace(old, new)` | cserével létrehozott új string |
| `text.split()` | szóközök mentén feldarabolt lista |
| `text.split(".")` | a megadott elválasztó mentén feldarabolt lista |
| `text.index(x)` | az első előfordulás indexe; hiányzó értéknél `ValueError` |
| `text.count(x)` | előfordulások száma |
| `len(text)` | karakterek száma |
| `separator.join(parts)` | stringek összefűzése elválasztóval |
| `x in text` | `True`, ha `x` megtalálható a stringben |
| `list(text)` | karakterek listája |

## Rövid példák

```python
szoveg = "Python nyelv"
print(szoveg.lower())           # python nyelv
print(szoveg.replace("nyelv", "programozás"))  # Python programozás
print(" ".join(["Jó", "napot"])) # Jó napot
```

A `join()` elválasztója az a string, amelyen a metódust meghívjuk. Számokat előbb `str()`-rel szöveggé kell alakítani. A részletes példákat a [02 – Részletes tananyag](02_main.md) tartalmazza.
