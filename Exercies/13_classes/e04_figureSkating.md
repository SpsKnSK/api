# HU
Egy műkorcsolyaversenyen 20 versenyző vetélkedik. Minden egyes műsor után a 8 bíró ad pontszámot 1-10ig, ezekből a legjobbat és a legrosszabbat figyelmen kívül hagyják. A versenyzők rangsorát az így megmaradt pontszámok átlaga alapján határozzák meg.

Feladatok:
1. Készítsetek egy listát 20 műkorcsolyázóval, akik rendelkeznek névvel és pontszámokkal (a műkorcsolyázó meghatározására használhattok listát, szótárat, osztályt)
2. Amint a műkorcsolyázó bemutatta a számát, a 8 bíró értékeli a műsort zsűrizve azt. A bírók 1-10-ig adnak egy tizedes számú értékelést. Az átlagot úgy számolják ki, hogy a két szélső értéket (a legjobbat és a legrosszabbat) figyelmen kívül hagyják.
4. A versenyzőket állítsátok sorrendbe a legmagasabb pontszámtól a legalacsonyabb pontszámig 
5. Az első 3 helyezett nevét, és elért pontszámát írjátok ki
6. Az utolsó 3 helyezett nevét, és elért pontszámát írjátok ki

- Használhatjátok a `faker` könyvtárat nevek generálásához
- Vagy ki is találhattok neveket
  
# Code

```py
from random import randint
from faker import Faker  # from command line run `pip install faker`
# https://faker.readthedocs.io/en/master/providers/faker.providers.person.html

def Main() -> None:
    faker = Faker()
    skaters = [faker.name() for _ in range(20)]
    for s in skaters:
        print(s)

Main()

```