# base calass with Name property, that is already set in __init__ method
class Animal:
    Name:str

    def __init__(self, name:str) -> None:
        self.Name = name

class Dog(Animal):

    # dog does not have __init__ method, but it inherits from Animal, so it is needed when creating an instance of a class 
    def Bark(self):
        print(f"I'm a dog, my name is {self.Name} and i am barking")

class Cat(Animal):
    
    # dog does not have __init__ method, but it inherits from Animal, so it is needed when creating an instance of a class 
    def Purr(self):
        print(f"I'm a cat, my name is {self.Name} and i am purring")

dog = Dog("Daniel")
dog.Bark()

cat = Cat("Cecil")
cat.Purr()