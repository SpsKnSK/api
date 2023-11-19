# HU
Kérjétek be a felhasználótól a lista elemeinek a számát, és készítsetek egy annyi véletlen egész számból álló listát. 

- Egy `paros` és `paratlan` listába mentsétek el a páros és páratlan számokat külön
- Írjátok ki a legkisebbet és a legnagyobb értéket a két listábólküket!


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