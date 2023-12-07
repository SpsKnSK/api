# Listák

A lista egy olyan adattípus, amely több érték tárolására szolgál egy változóban. 

Tartalmazhat:
- Integer
- String
- Float
- Másik lista
- Stb. típusú adatot.

## Elemek a listában

A listában minden elem egy meghatározott helyet foglal el. Ezt **index**nek nevezzük. Az index sorszám, amelyik 0-tól kezdődik az utolsó elem sorszámáig
```py
mylist = ["apple", "banana", "cherry"]
print(mylist)

print(mylist[0])
print(mylist[1])
print(mylist[2])
```
A `mylist` változó értéke `list`

## Példa
```py
adatok = ['hétfő', 'kedd', 'szerda', 1800]
print(adatok[2])
```
## Listaelem értékének megváltoztatása
```py
adatok = ['hétfő', 'kedd', 'szerda', 1800]
print(adatok)
adatok[3] = adatok[3] + 47
print(adatok)
```
másik példa: 
```py
adatok = ['hétfő', 'kedd', 'szerda', 1800]
print(adatok)
adatok[3] = 'Július'
print(adatok)
```
## `len()`
```py
mylist = ["apple", "banana", "cherry"]
print(len(mylist))
```

## Elem törlése
```py
mylist = ["apple", "banana", "cherry"]
del(mylist[1])
print(mylist)
```
vagy
```py
mylist = ["apple", "banana", "cherry"]
mylist.remove("apple")
print(mylist)
```
## Elem kiemelése `.pop()`
Kiemeli az utolsó elemet, és elmenthetjük egy változóba, a listából kitörli
```py
mylist = ["apple", "banana", "cherry"]
value = mylist.pop()
print(mylist)
print(value)
```

## Teljes lista törlése `.clear()`
```py
mylist = ["apple", "banana", "cherry"]
mylist.clear()
print(mylist)
```
## Új elem hozzáadása 
### `.append(erték)` új elem a lista végére
```py
mylist = ["apple", "banana", "cherry"]
mylist.append('kiwi')
print(mylist)
```
### `.insert(index, erték)` új elem az index helyére
```py
mylist = ["apple", "banana", "cherry"]
mylist.insert(1, 'kiwi')
print(mylist)
```
### `.index(elem)`
Visszaadja egy adott elem indexét, ha nem találja meg, akkor `-1`et ad vissza.

```py
from random import sample

mylist = sample(range(1, 50), 7)
legkisebbIndex = mylist.index(min(mylist))
print(f"A {mylist} legkisebb eleme a {legkisebbIndex}. indexen van, értéke pedig {mylist[legkisebbIndex]}")
```
### `.count(keresettElem)`
Megszámolja a megadott elemek darabszámát a listában. 
```py
mylist = [1, 1, 2, 3, 4, 5, 5, 1, 1]
print(mylist.count(1))
```
### `.extend(masikLista)`
Egyesít két listát
```py
from random import sample

mylist = sample(range(1, 50), 3)
yourList = sample(range(100, 500), 2)
print(mylist)
print(yourList)
mylist.extend(yourList)
print(mylist)
```
### `.reverse()`
Lista elemeinek sorrendjét megfordítja
```py
from random import sample

mylist = sample(range(1, 50), 5)
print(mylist)
mylist.reverse()
print(mylist)
```

## Lista két elemének cseréje
```py
myList = ["apple", "banana", "cherry"]
appleIndex, bananaIndex = myList.index("apple"), myList.index("banana")

print(myList)

myList[bananaIndex], myList[appleIndex] = myList[appleIndex], myList[bananaIndex]

print(myList)
```

## Feladatok
[e01_fillList.md](https://github.com/SpsKnSK/api/blob/main/Exercies/10_lists/e01_fillList.md)

[e02_fillListWithinInterval.md](https://github.com/SpsKnSK/api/blob/main/Exercies/10_lists/e02_fillListWithinInterval.md)

[e03_maxMin.md](https://github.com/SpsKnSK/api/blob/main/Exercies/10_lists/e03_maxMin.md)

[e04_maxMinIndexAverage.md](https://github.com/SpsKnSK/api/blob/main/Exercies/10_lists/e04_maxMinIndexAverage.md)

## Véletlen számokkal való feltöltés
### variant 1
```py
from random import randint

myList = []
while index < listLenght:
    myList.append(randint(rangeMinimum, rangeMaximum))
    index += 1
print(myList)
```
### variant 2
```py
from random import sample
mylist = sample(range(lowest, highest), numberOfElements)
print(myList)
```

## Feladat
> [e05_randomEvenOdd.md](https://github.com/SpsKnSK/api/blob/main/Exercies/10_lists/e05_randomEvenOdd.md)

## Feladat
> [e06_switchNumbers.md](https://github.com/SpsKnSK/api/blob/main/Exercies/10_lists/e06_switchNumbers.md)

## Feladat
> [e07_separateTextNumbers.md](https://github.com/SpsKnSK/api/blob/main/Exercies/10_lists/e07_separateTextNumbers.md)

# Kérdések
1. Mire szolgálnak a listák?
1. Készítsetek egy üres listát, és írassátok ki a képernyőre.
1. Mire szolgál az index?
1. Írjátok ki  egy tetszőleges lista első és utolsó elemét.
1. Töröljétek egy tetszőleges lista összes elemét a `del` paranccsal.
1. Egy 4 elemű listához adjatok hozzá egy tetszőleges új elemet az `.insert()` paranccsal.
1. Egy tetszőleges elemű listához adjatok hozzá egy tetszőleges új elemet az `.insert()` paranccsal.
1. Egy számokból álló listában írjátok ki a legkisebb és legnagyobb értéket, és azoknak az indexét.