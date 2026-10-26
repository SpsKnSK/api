# Fájlkezelés – függvények és metódusok

Ez a lap a részletes tananyagban használt függvények és metódusok gyors áttekintése.

| Név | Mire használjuk? |
|---|---|
| `open(fájlnév, mód)` | Fájl megnyitása. |
| `f.read(size)` | A fájl tartalmának beolvasása; `size` nélkül a teljes tartalmat adja vissza. |
| `f.readline()` | Egy sor beolvasása. |
| `f.readlines()` | Az összes sor beolvasása listába. |
| `f.write(szöveg)` | Szöveg írása a fájlba; a paraméternek `str`-nek kell lennie. |
| `f.seek(offset, honnan)` | A fájlon belüli pozíció (kurzor) mozgatása. |
| `f.close()` | A fájl bezárása. |
| `with open(...) as f:` | A blokk végén automatikusan bezárja a fájlt. |
| `path.dirname(__file__)` | A futtatott Python-fájlt tartalmazó könyvtár útvonalának meghatározása. |

## Megnyitási módok

- `r` – olvasás
- `w` – írás; a meglévő tartalmat felülírja
- `a` – hozzáfűzés
- `r+` – olvasás és írás
- `t` – szöveges mód (alapértelmezett)
- `b` – bináris mód
