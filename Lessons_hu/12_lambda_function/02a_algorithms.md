# Lambda és a hozzá kapcsolódó függvények – gyors áttekintés

| Függvény | Mire való? | Példa a részletes leckében |
|---|---|---|
| `lambda` | Rövid, névtelen függvény létrehozása | [Egyszerű lambda](02_main.md#egyszerű-lambda-függvény) |
| `map()` | Függvény alkalmazása minden elemre | [map példa](02_main.md#lambda-függvény-a-map-függvénnyel) |
| `filter()` | Elemek kiválasztása feltétel alapján | [filter példa](02_main.md#lambda-függvény-a-filter-függvénnyel) |
| `sorted(..., key=...)` | Rendezés megadott szempont szerint | [sorted példa](02_main.md#lambda-függvény-a-sorted-függvénnyel) |
| `reduce()` | Elemek egy értékké összevonása | [reduce példa](02_main.md#lambda-függvény-a-reduce-függvénnyel) |
| `min()`, `max()`, `sum()`, `len()` | Beépített összesítő függvények | [Összesítő függvények](02_main.md#összesítő-függvények) |

## Fontos megjegyzés

A `map()`, `filter()` és `reduce()` eredménye nem ugyanaz a típus: a `map()` és `filter()` iterálható objektumot ad vissza, a `reduce()` pedig egyetlen értéket. A `map()` és `filter()` eredményét a példákban `list()` alakítja listává.
