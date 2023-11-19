# HU
Kérjétek be a felhasználótól a lista elemeinek a számát, és készítsetek egy annyi véletlen egész számból álló listát. 

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