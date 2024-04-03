from os import path

class Cat:
    def __init__(self, name) -> None:
        self.Name = name

fileName = "cats.txt"
print(__file__)
full_path = f"{path.dirname(__file__)}\\{fileName}"

cat = Cat("Mr. Wisker")

with open(full_path, "w") as f:
    # cannot do:
    # f.write(cat)
    f.write(str(cat)) # writes: <__main__.Cat object at 0x000002539F9B77D0>

class Dog:
    def __init__(self, name) -> None:
        self.Name = name

    def __str__(self) -> str:
        return f"Dog: {self.Name}"

fileName = "dogs.txt"
print(__file__)
full_path = f"{path.dirname(__file__)}\\{fileName}"

dog = Dog("BullDog")

with open(full_path, "w") as f:
    # cannot do:
    # f.write(cat)
    f.write(str(dog)) # because of the __str__ it writes: Dog: BullDog