class Animal:
    Name:str

    def __init__(self, name:str) -> None:
        self.Name = name

class Dog(Animal):

    def Bark(self):
        print(f"I'm a dog, my name is {self.Name} and i am barking")

class Cat(Animal):

    def Purr(self):
        print(f"I'm a cat, my name is {self.Name} and i am purring")

dog = Dog("Daniel")
dog.Bark()

cat = Cat("Cecil")
cat.Purr()