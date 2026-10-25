> # ✏️ Lista, halmaz, szótár, tuple
>
> Négyféle **gyűjtemény** típus, mindegyiknek más a "személyisége":
>
> | Típus | Jel | Sorrend? | Ismétlődhet? | Módosítható? |
> |---|---|---|---|---|
> | `list` | `[]` | igen (index) | igen | igen |
> | `set` | `{}` | nem | **nem** | igen |
> | `dict` | `{kulcs: érték}` | igen (kulcs) | kulcs nem, érték igen | igen |
> | `tuple` | `()` | igen (index) | igen | **nem** |
>
> ```py
> lista = ['alma', 'körte']       # sorrend van, indexelhető, módosítható
> halmaz = {'alma', 'körte'}      # nincs sorrend, nincs duplikátum
> szotar = {'nev': 'Anna'}        # kulcs -> érték
> tuple_ = (10, 20)               # mint a lista, de nem módosítható
> ```
>
> **Metafora:**
> - **Lista** = **sorszámozott polc**: bármikor kivehetsz, betehetsz, átrendezheted.
> - **Halmaz** = **zsák egyedi golyókkal**: nem számít a sorrend, és két egyforma golyó nem fér bele.
> - **Szótár** = **telefonkönyv**: nem sorszám alapján keresel, hanem **név alapján** (kulcs → érték).
> - **Tuple** = **lepecsételt doboz**: amit egyszer beletettél, azt már nem cserélheted ki.
