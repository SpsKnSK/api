# Sorting

## `sorted()` function
Sorting a `list` can be done in many ways. First start with the `sorted` function. This functions returns a `list`, that is sorted (by default from the smallest to the largest):
```py
from random import sample

l = sample(range(10, 20), 10)
print(l)
l = sorted(l)
print(l)
```
### `sorted()` descending
Descending or from the biggest to the lowest
```py
from random import sample

l = sample(range(10, 20), 10)
print(l)
l = sorted(l, reverse=True)
print(l)
```

## `.sort()` instance function
This function returns `None`, what means, it changes the list itself:
```py
from random import sample

l = sample(range(10, 20), 10)
print(l)
l.sort()
print(l)
```

### `sort()` descending
```py
from random import sample

l = sample(range(10, 20), 10)
print(l)
l.sort(reverse=True)
print(l)
```

# Sorting own data types (e.g. `class`es)

```py
from random import randint
from faker import Faker  # from command line run `pip install faker`
# https://faker.readthedocs.io/en/master/providers/faker.providers.person.html


class Person:
    def __init__(self, name, surname, age) -> None:
        self.Name, self.Surname, self.Age = name, surname, age

    def __str__(self) -> str:
        return f"{self.Surname}, {self.Name} at age {self.Age}"


def PrintListOfPersons(persons: list[Person]) -> None:
    print("\n".join([str(p) for p in persons]))


Faker.seed(0)
fake = Faker()
persons = [Person(fake.first_name(), fake.last_name(), randint(18, 60)) for _ in range(50)]
print('# print first 10 persons')
PrintListOfPersons(persons[:10])

print('\n\n# sort them by first name')
personsSortedByFirstName = sorted(persons, key=lambda p: p.Name)
PrintListOfPersons(personsSortedByFirstName[:10])

print('\n\n# sort them by surname name')
personsSortedBSurname = sorted(persons, key=lambda p: p.Surname)
PrintListOfPersons(personsSortedBSurname[:10])

print('\n\n# sort them by age descending/reverse from the oldest -> the yougest')
persons.sort(key=lambda p: p.Age, reverse=True)
PrintListOfPersons(persons[:10])
```