> # ✏️ Lambda függvények (opcionális)
>
> A **lambda** egy rövid, névtelen, egysoros függvény.
>
> ```py
> negyzet = lambda x: x ** 2
> print(negyzet(4))   # 16
> ```
>
> Ugyanaz, mint:
> ```py
> def negyzet(x):
>     return x ** 2
> ```
>
> Leggyakrabban a `map()`, `filter()`, `sorted(key=...)` függvényekkel együtt használjuk, amikor egy egyszerű műveletet kell egy másik függvénynek átadni.
>
> **Metafora:** a lambda olyan, mint egy **post-it cetli**, amire gyorsan felírsz egy egysoros utasítást, és rögtön oda is adod valakinek — nem éri meg neki nevet adni, mint egy "rendes" függvénynek.
