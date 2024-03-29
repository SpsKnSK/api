class Animal:
    Name: str

    def __init__(self, name: str) -> None:
        self.Name = name

    # this method is not implemented in Animal class, every child class has to implement it
    def MakeNoise(self) -> None:
        # this raises an exception only when the child class is not implementing this method
        raise Exception("Implement in child class")
        # or you can use pass


class Dog(Animal):
    def MakeNoise(self):
        print(f"I'm a dog, my name is {self.Name} and i am barking")


class Cat(Animal):
    def MakeNoise(self):
        print(f"I'm a cat, my name is {self.Name} and i am purring")

# by purpose this does not override MakeNoise method, it will throw an exception
class Bird(Animal):
    pass

# when setting the type list[Aninaml], python will give you suggestions what methods/properties they have
animals : list[Animal] = [Dog("Daniel"), Cat("Cecil"), Bird("Barbara")]

for a in animals:
    try:
        a.MakeNoise()
    except Exception as ex:
        print(ex)
