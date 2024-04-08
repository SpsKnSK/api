# SK

V krasokorčuliarskej súťaži súťaží 20 pretekárov. Po každom vystúpení 8 rozhodcov udeľuje skóre od 1 do 10, z ktorých najlepšie a najhoršie skóre sú ignorované. Poradie súťažiacich sa určuje na základe priemeru zostávajúcich bodov.

Úlohy:

- Vytvorte zoznam 20 krasokorčuliarov, ktorí majú meno a skóre (na definovanie krasokorčuliara môžete použiť zoznam, slovník, triedu)
- Hneď ako krasokorčuliar predloží svoje číslo, 8 rozhodcov vyhodnotí vystúpenie. Porotcovia dávajú desatinné hodnotenie od 1 do 10. Priemer sa vypočíta tak, že sa ignorujú dve krajné hodnoty (najlepšia a najhoršia).
- Usporiadajte súťažiacich v poradí podľa priemeru
- Vypíšte mená prvých 3 krasokorčuliarov a ich skóre
- Vypíšte mená posledných 3 krasokorčuliarov a ich skóre

# HU
Egy műkorcsolyaversenyen 20 versenyző vetélkedik. Minden egyes műsor után a 8 bíró ad pontszámot 1-10ig, ezekből a legjobbat és a legrosszabbat figyelmen kívül hagyják. A versenyzők rangsorát az így megmaradt pontszámok átlaga alapján határozzák meg.

Feladatok:
1. Készítsetek egy listát 20 műkorcsolyázóval, akik rendelkeznek névvel és pontszámokkal (a műkorcsolyázó meghatározására használhattok listát, szótárat, osztályt)
2. Amint a műkorcsolyázó bemutatta a számát, a 8 bíró értékeli a műsort zsűrizve azt. A bírók 1-10-ig adnak egy tizedes számú értékelést. Az átlagot úgy számolják ki, hogy a két szélső értéket (a legjobbat és a legrosszabbat) figyelmen kívül hagyják.
4. A versenyzőket állítsátok sorrendbe a legmagasabb pontszámtól a legalacsonyabb pontszámig 
5. Az első 3 helyezett nevét, és elért pontszámát írjátok ki
6. Az utolsó 3 helyezett nevét, és elért pontszámát írjátok ki

> Használhatjátok a `faker` könyvtárat a nevek generálásához, vagy ki is találhattok neveket
  
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
