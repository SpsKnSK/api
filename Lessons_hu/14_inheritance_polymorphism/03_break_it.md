[Vissza a térképhez](../00_Terkep_hu.md)

# 💥 Rontsátok el!

Mi a hiba ebben a programban?

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

Miért dob a Python `AttributeError`-t? Figyeljetek a kis- és nagybetűkre — Python **kis- és nagybetű érzékeny** (case sensitive), tehát a `move()` és a `Move()` két különböző név!