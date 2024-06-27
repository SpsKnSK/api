# Properties

The idea is to create private members, that should not be changed from outside the class only through methods, that are allowed to manipulate the members (getters/setters). More can be read [here](https://stackoverflow.com/questions/17330160/how-does-the-property-decorator-work-in-python)

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

## _Single Leading Underscores -> private members

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

## Getters
Accessing the members should be through *properties*, those are methods that have the name of the member, in this case `def Name(self)->str:`
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

When we want to get the value of `_name_` we call the method on the object `print(p.Name())`.

## Properties

If you add a decorator `@property` you can get rid of the parenthesis: `print(p.Name)`. It is a so called *syntactic sugar*, which means, that it is fancier to use.

```py
class Person:
    def __init__(self, name: str, surname: str, age: int) -> None:
        self._name, self._surname, self._age = name, surname, age

    @property
    def Name(self) -> str:
        return self._name

    def __str__(self) -> str:
        return f"{self._name} {self._surname} is {self._age} years old"


p = Person("John", "Doe", 10)
print(p.Name)
```

## Setters
Setters are a way to handle value association. Private members of a class should **not** be changed outside of the class, hence it can have some *rules*. These rules can be applied in the getter/setter methods (mostly the other one).

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

We can have a guarding clausule in the setter method that does not allow empty strings to be set: it raises exception:
```py
class Person:
    def __init__(self, name: str, surname: str, age: int) -> None:
        self._name, self._surname, self._age = name, surname, age

    @property
    def Name(self) -> str:
        return self._name

    @Name.setter
    def Name(self, name) -> None:
        if not name:
            raise Exception("Name cannot be empty")
        self._name = name

    def __str__(self) -> str:
        return f"{self._name} {self._surname} is {self._age} years old"


p = Person("John", "Doe", 10)
print(p.Name)
try:
    p.Name = ""
    print(p.Name)
except Exception as ex:
    print(ex)
```