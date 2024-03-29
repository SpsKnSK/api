# SK
V nasledujúcom kóde zmente `CalculateAverage` tak, aby vám vrátil priemer, v iných prípadoch vnechvráti `0`. Funkciu `Main` nemente!

# HU
A következő kódban változtassátok meg
- a `CalculateAverage`-t, hogy helyes átlagot számoljon, bármi egyéb lehetőségnél `0`-t adjon vissza
- `PrintListsAverage`, hogy kiirja "The average of the following list: (l) is (average)". 

A `Main` függvényt ne változtassátok!

```py
def CalculateAverage(l: list[int]) -> float:
    pass


def PrintListsAverage(l: list) -> None:
    pass


def Main() -> None:
    myList = None
    PrintListsAverage(myList)
    myList = "Test"
    PrintListsAverage(myList)
    myList = 1
    PrintListsAverage(myList)
    myList = []
    PrintListsAverage(myList)
    myList = [1, 2, 3]
    PrintListsAverage(myList)


Main()

```

# Output
```
The average of the following list: None is 0.00
The average of the following list: Test is 0.00
The average of the following list: 1 is 0.00
The average of the following list: \[\] is 0.00
The average of the following list: \[1, 2, 3\] is 2.00
```