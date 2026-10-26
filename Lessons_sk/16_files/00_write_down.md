🗺️ [Späť na mapu](../00_Mapa_sk.md)

> # ✏️ Práca so súbormi
>
> ```py
> with open("pracovnysubor.txt", "w") as f:
>     f.write("Toto je testovací riadok 12345")
>
> with open("pracovnysubor.txt", "r") as f:
>     obsah = f.read()
>     print(obsah)
> ```
>
> | Mód | Význam |
> |---|---|
> | `r` | iba čítanie |
> | `w` | iba zápis (prepíše súbor!) |
> | `a` | pridanie na koniec súboru |
> | `r+` | zápis aj čítanie naraz |
>
> - `f.read()` — celý obsah
> - `f.readline()` — jeden riadok
> - `f.readlines()` — zoznam, každý riadok je jeden prvok
> - `f.write(text)` — prijíma iba `str`! (preveď pomocou `str(cislo)`)
> - `with open(...) as f:` — súbor sa na konci bloku **automaticky zatvorí**, netreba volať `f.close()`
>
> **Metafora:** súbor je ako **spoločný zošit**: keď ho otvoríš (`open`), môžeš doň písať alebo z neho čítať, ale ak ho zabudneš zavrieť (`close`), iný program sa k nemu nemusí dostať. `with` je ako **automatické dvere**: samy sa zatvoria, keď odídeš.
