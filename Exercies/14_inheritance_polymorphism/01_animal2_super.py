# base calass with Name property, that is already set in __init__ method
class Animal:
    Name:str

    def __init__(self, name:str) -> None:
        self.Name = name

class Dog(Animal):
    
    # we add a new property to Dog numberOfBittenPostmen and reuse the init from Animal
    def __init__(self, name:str, numberOfBittenPostmen:int) -> None:
        super().__init__(name)
        self.NumberOfBittenPostmen = numberOfBittenPostmen
    
    def Bark(self):
        print(f"I'm a dog, my name is {self.Name} and i am barking. I bit {self.NumberOfBittenPostmen} postmen.")

class Cat(Animal):
    
    # we add a new property to Cat color and reuse the init from Animal
    def __init__(self, name:str, color:str) -> None:
        super().__init__(name)
        self.Color = color
    
    def Purr(self):
        print(f"I'm a cat, my name is {self.Name} and i am purring. I have {self.Color} fur.")

# The following won't work, hence the Dog and Cat classes need an extra input parameter for the constructor
# dog = Dog("Daniel")
# dog.Bark()

# cat = Cat("Cecil")
# cat.Purr()

dog = Dog("Daniel", 14)
dog.Bark()

cat = Cat("Cecil", "black")
cat.Purr()