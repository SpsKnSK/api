# Práca so súbormi – základy

Pomocou súborov môžeme uchovávať údaje aj po skončení programu.

## Najdôležitejšie veci

- `open(názov_súboru, mód)` – otvorí súbor.
- `r` – čítanie, `w` – zápis (prepíše predchádzajúci obsah), `a` – pridanie na koniec.
- `read()` – načíta celý obsah; `readline()` – jeden riadok; `readlines()` – zoznam riadkov.
- `write()` – zapisuje text do súboru; iný dátový typ treba najprv previesť pomocou `str()`.
- `with open(...) as f:` – na konci bloku automaticky zatvorí súbor.
- `os.path.dirname(__file__)` – vráti cestu k adresáru, v ktorom sa nachádza spustený Python súbor.

## Krátky príklad

```py
with open("pracovnysubor.txt", "w") as f:
    f.write("Ahoj!")

with open("pracovnysubor.txt", "r") as f:
    print(f.read())
```

Výstup:
```text
Ahoj!
```

Mód `w` prepíše existujúci obsah súboru, preto ho používaj opatrne.
