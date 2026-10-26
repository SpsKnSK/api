# Práca so súbormi – funkcie a metódy

Táto stránka stručne zhŕňa funkcie a metódy použité v podrobnom učive.

| Názov | Na čo slúži? |
|---|---|
| `open(názov_súboru, mód)` | Otvorenie súboru. |
| `f.read(size)` | Načítanie obsahu súboru; bez `size` vráti celý obsah. |
| `f.readline()` | Načítanie jedného riadka. |
| `f.readlines()` | Načítanie všetkých riadkov do zoznamu. |
| `f.write(text)` | Zápis textu do súboru; parameter musí byť typu `str`. |
| `f.seek(offset, odkiaľ)` | Posunutie kurzora v súbore. |
| `f.close()` | Zatvorenie súboru. |
| `with open(...) as f:` | Automaticky zatvorí súbor na konci bloku. |
| `path.dirname(__file__)` | Určenie cesty k adresáru, v ktorom sa nachádza spustený Python súbor. |

## Režimy otvorenia

- `r` – čítanie
- `w` – zápis; prepíše existujúci obsah
- `a` – pridanie na koniec
- `r+` – čítanie aj zápis
- `t` – textový režim (predvolený)
- `b` – binárny režim
