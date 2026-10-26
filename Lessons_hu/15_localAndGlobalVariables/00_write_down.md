🗺️ [Vissza a térképhez](../../Lessons_hu/00_Terkep_hu.md)

> # ✏️ Globális és lokális változók
>
> - **Globális változó**: a függvényeken kívül létezik, mindenhonnan elérhető
> - **Lokális változó**: egy függvényen belül jön létre, csak ott létezik
> - Ha egy függvényen belül **ugyanazt a nevet** használjuk, az egy **új, lokális** változó lesz — nem nyúl a globálishoz!
> - `global x` — ezzel mondjuk meg, hogy a függvényen belül **ne** hozzon létre új lokális változót, hanem a globálist módosítsa
>
> ```py
> x = "awesome"
>
> def myfunc():
>     x = "fantastic"     # ez lokális, nem érinti a globálist
>     print(f"Python is {x}")
>
> myfunc()                # Python is fantastic
> print(f"Python is {x}") # Python is awesome (a globális változatlan)
> ```
>
> **Miért jobb paramétert használni globális változó helyett?** Mert így a függvény csak azzal dolgozik, amit **átadunk neki** — nem lehet meglepetés abból, hogy valahol máshol megváltozott egy érték a hátunk mögött.
>
> **Metafora:** a globális változó olyan, mint egy **közös iskolai tábla**: bárki írhat rá, bárki törölhet róla, és ha két diák egyszerre firkál rá, könnyen összezavarodik. A paraméterek olyanok, mint a **saját füzet**: csak azt írod bele, amire szükséged van, senki más nem piszkálja.
