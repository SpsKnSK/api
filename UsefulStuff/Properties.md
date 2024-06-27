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

Creating extra methods to change value
```py
class Person:
    Name: str
    Surname: str
    Age: int
    def __init__(self, name: str, surname: str, age: int) -> None:
        self.Name, self.Surname, self.Age = name, surname, age

    def ChangeSurname(self, newSurname:str)->None:
        self.Surname = newSurname


p = Person("John", "Doe", 10)
print(p.Surname)
p.ChangeSurname("Smith")
print(p.Surname)
```

## _Single Leading Underscores

One underline at the beginning of a method, function, or data member means you shouldn’t access this method because it’s not part of the API. Let’s look at this snippet of code: 

```py
class Person:
    def __init__(self, name: str, surname: str, age: int) -> None:
        self._name, self._surname, self._age = name, surname, age
    
    def __str__(self) -> str:
        return f"{self._name} {self._surname} is {self._age} years old"

p = Person("John", "Doe", 10)
print(p)
```

Accessing the members should be through *properties*
```py
class Person:
    def __init__(self, name: str, surname: str, age: int) -> None:
        self._name, self._surname, self._age = name, surname, age
    
    def Name(self)->str:
        return self._name

    def __str__(self) -> str:
        return f"{self._name} {self._surname} is {self._age} years old"

p = Person("John", "Doe", 10)
print(p.Name())
```

If you want to set the value of the member through a setter method, you should use `NameOfTheProperty.setter`:
```py
class Person:
    def __init__(self, name: str, surname: str, age: int) -> None:
        self._name, self._surname, self._age = name, surname, age

    @property
    def Name(self) -> str:
        return self._name

    @Name.setter
    def Name(self, name) -> None:
        self._name = name

    def __str__(self) -> str:
        return f"{self._name} {self._surname} is {self._age} years old"


p = Person("John", "Doe", 10)
print(p.Name)
p.Name = "new name"
print(p.Name)
```