# SK
Zmeňte nasledujúci kód tak, aby funkcia `CountDistinctElements` namiesto `pass` vrátila slovník, kde kľúčom je **číslo**, a hodnotou je **počet výskytov v zozname**.

# HU
A következő kódot változtassátok meg úgy, hogy a `pass` helyett egy olyan szótárat adjon vissza a `CountDistinctElements` függvény, amelyik kulcsa a **szám**, értéke pedig a listában az **előbukkanása**.
> _The pass statement: How to Do Nothing in Python_
```py
from random import randint

def CountDistinctElements(l:list[int])->dict[int, int]:
    pass

myList = [randint(0,10) for _ in range(20)]

distincElementCount = CountDistinctElements(myList)
print(distincElementCount)
```