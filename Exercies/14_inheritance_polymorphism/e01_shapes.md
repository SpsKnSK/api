# HU
Az öröklés és polimorfizmus alapján bővítsétek ki a két osztályt úgy, hogy működjön a kód, és helyes értékeket adjon vissza a terület és kerület számításánál:
  - `Kör`, inicializálásnál állítsátok be a sugarat
  - `Téglalap`, inicializálásnál állítsátok be a két oldal hosszúságát

A következő kódot egészítsétek ki, a `Main` és `GetRandomLength` függvényeket és a `Shape` osztályt ne változtassátok!
# Fill

```py
class Shape:
    def CalculateArea(self) -> float:
        raise("Implement in child class")

    def CalulatePerimeter(self) -> float:
        raise("Implement in child class")

    def GetName(self) -> str:
        return self.__class__.__name__

class Circle:
    pass

class Rectangle:
    pass
    
def GetRandomLength() -> int:
    from random import randint
    return randint(10, 30)

def Main() -> None:
    c = Circle(GetRandomLength())
    r = Rectangle(GetRandomLength(), GetRandomLength())
    shapes: list[Shape] = [c, r]
    for s in shapes:
        print(f"The perimeter of {s.GetName()} is {s.CalulatePerimeter():0.2f} cm")
        print(f"The area of {s.GetName()} is {s.CalculateArea():0.2f} cm^2")
Main()

```