> # ✏️ Lambda funkcie (voliteľné)
>
> **Lambda** je krátka, anonymná, jednoradová funkcia.
>
> ~~~py
> stvorec = lambda x: x ** 2
> print(stvorec(4))   # 16
> ~~~
>
> To isté ako:
> ~~~py
> def stvorec(x):
>     return x ** 2
> ~~~
>
> Najčastejšie ju používame spolu s `map()`, `filter()` a `sorted(key=...)`, keď treba inej funkcii odovzdať jednoduchú operáciu.
>
> **Metafora:** lambda je ako **post-it lístok**, na ktorý si rýchlo napíšete jednoradový pokyn a hneď ho niekomu odovzdáte — neoplatí sa mu dávať meno ako "riadnej" funkcii.
