[Späť na mapu](../00_Mapa_sk.md)

# 💥 Pokazte to!

Aka je chyba v tomto programe?

```py
class Car:
  def __init__(self, brand, model):
    self.Brand = brand
    self.Model = model
  def Move(self):
    print("Drive!")

car1 = Car("Ford", "Mustang")
car1.move()
```

Preco Python vyhodi `AttributeError`? Davajte pozor na male a velke pismena - Python je **case sensitive**, takze `move()` a `Move()` su dve rozne mena!