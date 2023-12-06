# Zoznamy

Zoznam je dátový typ, ktorý slúži na uchovávanie viacerých hodnôt v jednej premennej.

Môže obsahovať:
- Celé čísla
- Reťazce
- Desatinné čísla
- Iný zoznam
- Atď., rôzne typy údajov.

## Prvky v zozname

V zozname zaberá každý prvok určitú pozíciu, ktorá sa nazýva **index**. Index začína od 0 až po pozíciu posledného prvku.
```py
moj_zoznam = ["jablko", "hruška", "čerešňa"]
print(moj_zoznam)

print(moj_zoznam[0])
print(moj_zoznam[1])
print(moj_zoznam[2])
```

Hodnota premennej `moj_zoznam` je `list`.

## Príklad
```py
udaje = ['pondelok', 'utorok', 'streda', 1800]
print(udaje[2])
```

## Zmena hodnoty prvku v zozname
```py
udaje = ['pondelok', 'utorok', 'streda', 1800]
print(udaje)
udaje[3] = udaje[3] + 47
print(udaje)
```
Iný príklad:
```py
udaje = ['pondelok', 'utorok', 'streda', 1800]
print(udaje)
udaje[3] = 'júl'
print(udaje)
```
## `len()`
```py
moj_zoznam = ["jablko", "hruška", "čerešňa"]
print(len(moj_zoznam))
```

## Odstránenie prvku
```py
moj_zoznam = ["jablko", "hruška", "čerešňa"]
del(moj_zoznam[1])
print(moj_zoznam)
```
alebo
```py
moj_zoznam = ["jablko", "hruška", "čerešňa"]
moj_zoznam.remove("jablko")
print(moj_zoznam)
```
## Vyňatie prvku pomocou `.pop()`
Vyberie posledný prvok, a môže sa uložiť do premennej, zároveň ho odstráni zo zoznamu.
```py
moj_zoznam = ["jablko", "hruška", "čerešňa"]
hodnota = moj_zoznam.pop()
print(moj_zoznam)
print(hodnota)
```

## Úplné vymazanie zoznamu `.clear()`
```py
moj_zoznam = ["jablko", "hruška", "čerešňa"]
moj_zoznam.clear()
print(moj_zoznam)
```
## Pridanie nového prvku
### `.append(value)` nový prvok na koniec zoznamu
```py
moj_zoznam = ["jablko", "hruška", "čerešňa"]
moj_zoznam.append('kiwi')
print(moj_zoznam)
```
### `.insert(index, value)` nový prvok na danú pozíciu
```py
moj_zoznam = ["jablko", "hruška", "čerešňa"]
moj_zoznam.insert(1, 'kiwi')
print(moj_zoznam)
```
### `.index(element)`
Vráti index zadaného prvku, ak ho nájde, inak vráti `-1`.

```py
from random import sample

moj_zoznam = sample(range(1, 50), 7)
index_najmensieho = moj_zoznam.index(min(moj_zoznam))
print(f"Najmenší prvok v {moj_zoznam} je na indexe {index_najmensieho}, jeho hodnota je {moj_zoznam[index_najmensieho]}")
```
### `.count(searchedElement)`
Spočíta počet výskytov daných prvkov v zozname.
```py
moj_zoznam = [1, 1, 2, 3, 4, 5, 5, 1, 1]
print(moj_zoznam.count(1))
```
### `.extend(anotherList)`
Zlúči dva zoznamy.
```py
from random import sample

moj_zoznam = sample(range(1, 50), 3)
tvoj_zoznam = sample(range(100, 500), 2)
print(moj_zoznam)
print(tvoj_zoznam)
moj_zoznam.extend(tvoj_zoznam)
print(moj_zoznam)
```
### `.reverse()`
Otočí poradie prvkov v zozname.
```py
from random import sample

moj_zoznam = sample(range(1, 50), 5)
print(moj_zoznam)
moj_zoznam.reverse()
print(moj_zoznam)
```

## Výmena dvoch prvkov v zozname
```py
moj_zoznam = ["jablko", "hruška", "čerešňa"]
jablkoIndex, hruškaIndex = moj_zoznam.index("jablko"), moj_zoznam.index("hruška")

print(moj_zoznam)

moj_zoznam[hruškaIndex], moj_zoznam[jablkoIndex] = moj_zoznam[jablkoIndex], moj_zoznam[hruškaIndex]

print(moj_zoznam)
```

## Úlohy
[e01_fillList.md](https://github.com/SpsKnSK/api/blob/main/Exercies/10_lists/e01_fillList.md)

[e02_fillListWithinInterval.md](https://github.com/SpsKnSK/api/blob/main/Exercies/10_lists/e02_fillListWithinInterval.md)

[e03_maxMin.md](https://github.com/SpsKnSK/api/blob/main/Exercies/10_lists/e03_maxMin.md)

[e04_maxMinIndexAverage.md](https://github.com/SpsKnSK/api/blob/main/Exercies/10_lists/e04_maxMinIndexAverage.md)


## Naplnenie zoznamu náhodnými číslami
### Variant 1
```py
from random import randint

moj_zoznam = []
while index < dlzka_zoznamu:
    moj_zoznam.append(randint(minimum_intervalu, maximum_intervalu))
    index += 1
print(moj_zoznam)
```
### Variant 2
```py
from random import sample
moj_zoznam = sample(range(minimum, maximum), pocet_prvkov)
print(moj_zoznam)
```

## Úlohy
> [e05_randomEvenOdd.md](https://github.com/SpsKnSK/api/blob/main/Exercies/10_lists/e05_randomEvenOdd.md)

## Úlohy
> [e06_switchNumbers.md](https://github.com/SpsKnSK/api/blob/main/Exercies/10_lists/e06_switchNumbers.md)

## Úlohy
> [e07_separateTextNumbers.md](https://github.com/SpsKnSK/api/blob/main/Exercies/10_lists/e07_separateTextNumbers.md)

# Otázky
1. Načo slúžia zoznamy?
1. Vytvorte prázdny zoznam a vypíšte ho na obrazovku.
1. Načo slúži index?
1. Vypíšte prvý a posledný prvok ľubovoľného zoznamu.
1. Odstráňte všetky prvky v ľubovoľnom zozname pomocou príkazu `del`.
1. Pridajte do zoznamu s 4 prvkami ľubovoľný nový prvok pomocou príkazu `.insert()`.
1. Pridajte do zoznamu s ľubovoľným počtom prvkov ľubovoľný nový prvok pomocou príkazu `.insert()`.
1. V zozname čísel vypíšte najmenšiu a najväčšiu hodnotu, a ich indexy.
