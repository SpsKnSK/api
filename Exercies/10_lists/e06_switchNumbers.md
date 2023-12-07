# SK
Od používateľas si vypýtajte počet prvkov v zozname a vytvorte z neho zoznam náhodných celých čísel `(-100,1000)`.

- Nájdite najmenšie a najväčšie číslo v zozname.
- Vložte najmenšie číslo na začiatok zoznamu a najväčšie na koniec.
- 
# HU
Kérjétek be a felhasználótól a lista elemeinek a számát, és készítsetek egy annyi véletlen egész számból álló listát a `(-100,1000)` intervallumból.

- Keressétek meg a legkisebb és legnagyobb számokat
- A lista elejére tegyétek a legkisebbet, a lista végére a legnagyobbat


## Hint
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

# Example
```
Give me the count of random numbers <1;20>: 0
The count has to be between <1;20>
Give me the count of random numbers <1;20>: 234er
There was an error to convert the input to a number, please try again
Give me the count of random numbers <1;20>: dfs
There was an error to convert the input to a number, please try again
Give me the count of random numbers <1;20>: 90
The count has to be between <1;20>
Give me the count of random numbers <1;20>: 15
[28, 348, 762, 81, 494, 713, 187, 209, 222, 5, 530, 979, 633, 48, -2]
After switch
[-2, 348, 762, 81, 494, 713, 187, 209, 222, 5, 530, 28, 633, 48, 979]
```