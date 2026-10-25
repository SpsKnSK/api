[Späť na mapu](../00_Mapa_sk.md)

> # 💥 Pokazte to!
>
> Aka je chyba v tomto programe?
>
> ```py
> class Teplomer:
>     def __init__(self):
>         self.celsius = 0
>
> t = Teplomer()
> t.celsius = -500
> print(t.celsius)
> ```
>
> Program sa spusti, ale dovoli fyzikalne nemoznu hodnotu (-500 C neexistuje, absolutna nula je -273.15 C). Ako by sa dala trieda ochranit pomocou `@property`?
