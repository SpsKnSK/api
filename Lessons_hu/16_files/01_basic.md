# Fájlkezelés – alapok

A fájlok segítségével a program futásának befejezése után is megőrizhetjük az adatokat.

## A legfontosabbak

- `open(fájlnév, mód)` – megnyit egy fájlt.
- `r` – olvasás, `w` – írás (a korábbi tartalmat felülírja), `a` – hozzáfűzés.
- `read()` – a teljes tartalom beolvasása; `readline()` – egy sor; `readlines()` – a sorok listája.
- `write()` – szöveget ír a fájlba; más adattípust előbb `str()`-ré kell alakítani.
- `with open(...) as f:` – a blokk végén automatikusan bezárja a fájlt.
- `os.path.dirname(__file__)` – annak a könyvtárnak az elérési útját adja meg, amelyben a futtatott Python-fájl található.

## Rövid példa

```py
with open("munkafajl.txt", "w") as f:
    f.write("Szia!")

with open("munkafajl.txt", "r") as f:
    print(f.read())
```

Kimenet:
```text
Szia!
```

A `w` mód felülírja a fájl meglévő tartalmát, ezért óvatosan használd.
