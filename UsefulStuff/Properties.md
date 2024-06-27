# Properties
Creating properties using `init`
```py
class Person:
    def __init__(self, name: str, surname: str, age: int) -> None:
        self.Name, self.Surname, self.Age = name, surname, age


p = Person("John", "Doe", 10)
print(p.Name)
```

Creating class properties before `init`
```py
class Person:
    Name: str
    Surname: str
    Age: int
    def __init__(self, name: str, surname: str, age: int) -> None:
        self.Name, self.Surname, self.Age = name, surname, age


p = Person("John", "Doe", 10)
print(p.Name)
```

Creating extra 