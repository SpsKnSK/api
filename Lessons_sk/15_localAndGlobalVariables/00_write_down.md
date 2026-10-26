🗺️ [Späť na mapu](../../Lessons_sk/00_Mapa_sk.md)

> # ✏️ Globálne a lokálne premenné
>
> - **Globalna premenna**: existuje mimo funkcii, je dostupna odkialkolvek
> - **Lokalna premenna**: vznika vo vnutri funkcie, existuje len tam
> - Ak vo vnutri funkcie pouzijeme **rovnaky nazov**, vznikne **nova lokalna** premenna — globalnej sa to nedotkne!
> - `global x` — tym povieme, ze vo funkcii sa nema vytvorit nova lokalna premenna, ale ma sa menit globalna
>
> ```py
> x = "uzasny"
>
> def mojafunkcia():
>     x = "fantasticky"   # toto je lokalna premenna, globalnu nemeni
>     print(f"Python je {x}")
>
> mojafunkcia()               # Python je fantasticky
> print(f"Python je {x}")     # Python je uzasny (globalna sa nezmenila)
> ```
>
> **Preco je lepsie pouzivat parametre namiesto globalnych premennych?** Pretoze funkcia potom pracuje iba s tym, co jej **odovzdame** — neprekvapi nas, ze sa niekde inde na pozadi zmenila nejaka hodnota.
>
> **Metafora:** globalna premenna je ako **spolocna skolska tabula**: ktokolvek na nu moze pisat, ktokolvek ju moze zmazat, a ked na nu pisu dvaja naraz, lahko vznikne zmatok. Parametre su ako **vlastny zosit**: zapisujes si len to, co potrebujes, a nikto iny ti donho nezasahuje.
