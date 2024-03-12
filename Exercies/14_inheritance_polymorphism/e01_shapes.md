# HU
- Hozzatok létre két származott osztályt a `Síkidom` osztályból
  - `Kör`, inicializálásnál állítsátok be a sugarat
  - `Téglalap`, inicializálásnál állítsátok be a két oldal hosszúságát

A következő kódot egészítsétek ki, a `Main` függvényt és a `Shape` osztályt ne változtassátok!
# Fill

```py
class Shape:
    def CalculateArea(self) -> float:
        pass

    def CalulatePerimeter(self) -> float:
        pass

    def GetName(self)->str:
        return self.__class__.__name__


class Circle:
    pass

class Rectangle:
    pass
    
def Main()->None:
    c = Circle(10)
    r = Rectangle(10,20)
    shapes : list[Shape] = [c, r]    
    for s in shapes:
        print(f"The perimeter of {s.GetName()} is {s.CalulatePerimeter()} cm")
        print(f"The area of {s.GetName()} is {s.CalculateArea()} cm^2")
Main()

```