# HU
Egy műkorcsolyaversenyen 20 versenyző vetélkedik. Minden egyes műsor után a 8 bíró ad pontszámot 1-10ig, ezekből a legjobbat és a legrosszabbat figyelmen kívül hagyják. A versenyzők rangsorát az így megmaradt pontszámok átlaga alapján határozzák meg.

Feladatok:
1. készítsetek egy listát 20 műkorcsolyázóval (a műkorcsolyázó meghatározására használhattok listát, szótárat, osztályt)
2. amint a műkorcsolyázó bemutatta a számát, 8 véletlen tizedes számú értékelést kap, amiből a két szélsőt (a legjobbat és a legrosszabbat) figyelmen kívül hagyjátok, úgy határozzátok meg az átlagpontszámot
3. állítsátok sorrendbe a legmagasabb pontszámtól a legalacsonyabb pontszámig a versenyzőket
4. Az első 3 helyezett nevét, és elért pontszámát írjátok ki
5. Az utolsó 3 helyezett nevét, és elért pontszámát írjátok ki

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