# SK
V nasledujúcom kóde zmente `CalculateAverage` tak, aby vám vrátil priemer, v iných prípadoch vnechvráti `0`. Funkciu `Main` nemente!

# HU
A következő kódban változtassátok meg a `CalculateAverage`-t, hogy helyes átlagot számoljon, bármi egyéb lehetőségnél `0`-t adjon vissza. A `Main` függvényt ne változtassátok!

```py
def CalculateAverage(l: list[int]) -> float:
    pass


def PrintListsAverage(l: list) -> float:
    print(f"The average of the following list: {l} is {CalculateAverage(l):0.2f}")


def Main() -> None:
    myList = None
    PrintListsAverage(myList)
    myList = []
    PrintListsAverage(myList)
    myList = [1, 2, 3]
    PrintListsAverage(myList)


Main()

```