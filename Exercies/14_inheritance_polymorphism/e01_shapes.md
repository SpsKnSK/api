# SK
Podľa pravidiel dedenia a polymorfizmu dopíšte, doplňte nasledujúce dve triedy tak, aby kód fungoval a vypočítal správnu hodnotu obvodu a obsahu:
  - `Kružnica`, pri inicializácií nastavte **polomer**
  - `Obdĺžnik`, pri inicializácií nastavte **obe stray**

Zmeňte len **Circle** a **Rectangle**, `Main`,  `GetRandomLength` a `Shape` nechajte tak, ako sú

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

    def CalculatePerimeter(self) -> float:
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
        print(f"The perimeter of {s.GetName()} is {s.CalculatePerimeter():0.2f} cm")
        print(f"The area of {s.GetName()} is {s.CalculateArea():0.2f} cm^2")
Main()

```
# Output
```
The perimeter of Circle is 157.00 cm
The area of Circle is 1962.50 cm^2
The perimeter of Rectangle is 102.00 cm
The area of Rectangle is 644.00 cm^2
```