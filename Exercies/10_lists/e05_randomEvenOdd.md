# SK
Od používateľas si vypýtajte počet prvkov `<1;20>` v zozname a vytvorte z neho zoznam náhodných celých čísel `(100,1000)`.

- Uložte párne a nepárne čísla do samostatných zoznamov `parneCisla` a `neparneCisla`.
- Vypíšte najmenšiu a najväčšiu hodnotu z oboch zoznamov!

# HU
Kérjétek be a felhasználótól a lista elemeinek a számát `<1;20>` , és készítsetek egy annyi véletlen egész számból álló listát a `(100,1000)` intervallumból. 

- Egy `paros` és `paratlan` listába mentsétek el a páros és páratlan számokat külön
- Írjátok ki a legkisebbet és a legnagyobb értéket a két listából!


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
Give me the count of random numbers <1;20>: asd
There was an error to convert the input to a number, please try again
Give me the count of random numbers <1;20>: 12321as
There was an error to convert the input to a number, please try again
Give me the count of random numbers <1;20>: 25
The count has to be between <1;20>
Give me the count of random numbers <1;20>: 15
The whole list: [368, 872, 241, 795, 483, 116, 611, 859, 594, 301, 437, 698, 160, 602, 949]
The even numbers are: [368, 872, 116, 594, 698, 160, 602]
The smallest even numer is: 116
The biggest even number is: 872
The odd numbers are: [241, 795, 483, 611, 859, 301, 437, 949]
The smallest odd numer is: 241
The biggest odd number is: 949
```