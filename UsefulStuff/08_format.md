# Formatting in python
[Here](https://www.youtube.com/watch?v=9saytqA0J9A&ab_channel=Indently) is a link to watch the whole video

## Print values with different type
```py
name: str = "John"
age: int = 25
print("Name:", name, ", age:", age)
```
> Output `Name: John , age: 25`

Or joining the whole string:
```py
name: str = "John"
age: int = 25
print("Name: " + name + ", age: " + str(age))
```
> Output `Name: John , age: 25`

### Simplifying process
```py
name: str = "John"
age: int = 25
print(f"Name: {name}, age: {age}")
```
> Output `Name: John , age: 25`
### Write out a result of an operation
```py
print(f"2+2 = {2+2}")
```
> Output `2+2 = 4`

## Working with variables
Write out the variable's name and value
```py
var: int = 100
print(f"var={var}")
```
Instead of this you can use the `var=` to write out the name and the value
```py
var: int = 100
print(f"{var=}")
```
> Output `var=100`
To check if a variable is an instance of `int` type:
```py
var: int = 100
print(f"{isinstance(var, int)=}")
```
> Output `isinstance(var, int)=True`
Adding spacing will be shown in the result:
```py
var: int = 100
print(f"{isinstance(var, int) = }")
```
> Output: `isinstance(var, int) = True`

## Working with decimals
```py
print(f"{decimal:.2f}")  # after the decimal point round to 2 decimal numbers
print(f"{decimal:0.2f}")  # after the decimal point round to 2 decimal numbers, minimum 0 characters
print(f"{decimal:.3f}")  # after the decimal point round to 3 decimal numbers
print(f"{decimal:06.1f}")  # after the decimal point round to 1 decimal numbers, leading char is 0 and make the whole number's lenght to 6 -> len('0001.7') == 6
```
Output: 
```
1.68
1.68
1.679
0001.7
```
Formatting explained:
```py
              {:6.1f}
                ↑ ↑ 
                | |
# digits to pad | | # of decimal places to display
```

## Working with percents
```py
percent: float = 0.387481
print(f"{percent:.2%}")
print(f"{percent:.1%}")
print(f"{percent:.0%}")
```
Output:
```
38.75%
38.7%
39%
```

## Working with datetime library
```py
from datetime import datetime

now: datetime = datetime.now()
print(now) # Current date and time: 
print(f"{now:%x}") # Locale’s appropriate date representation. 
print(f"{now:%c}") # Locale’s appropriate date and time representation. 
print(f"{now:%H:%M:%S}") # hours:minutes:seconds
```
Output:
```
2024-12-08 11:23:30.997903
12/08/24
Sun Dec  8 11:23:30 2024
11:23:30
```

## Alignment

### Text
```py
text: str = "MyText"

print(f"{text:_>20}")  # right align
print(f"{text:_^20}")  # center align
print(f"{text:_<20}")  # left align
print()
print(f"{text:*>20}")  # right align with '*'
print(f"{text:*^20}")  # center align with '*'
print(f"{text:*<20}")  # left align with '*'

```
Output:
```
______________MyText
_______MyText_______
MyText______________

**************MyText
*******MyText*******
MyText**************
```
### Using indent to display text
```py
names: list[str] = ["Bob", "Alice", "Montgomery", "Ubul", "John", "Frederik"]
print("Show names in a column")
for n in names:
  print(f"Hi {n:>12}, how are you?")

print("\nShow names in a column with the comma right behind the name")
for n in names:
  print(f"Hi {n+',':<12}how are you?")

print("\nShow names in a column with calculated indent")
maxLength: int = max([len(n) for n in names]) + 1
for n in names:
  print(f"Hi {n+',':<{maxLength}} how are you?")
```
Output:
```
Show names in a column
Hi          Bob, how are you?
Hi        Alice, how are you?
Hi   Montgomery, how are you?
Hi         Ubul, how are you?
Hi         John, how are you?
Hi     Frederik, how are you?

Show names in a column with the comma right behind the name
Hi Bob,        how are you?
Hi Alice,      how are you?
Hi Montgomery, how are you?
Hi Ubul,       how are you?
Hi John,       how are you?
Hi Frederik,   how are you?

Show names in a column with calculated indent
Hi Bob,        how are you?
Hi Alice,      how are you?
Hi Montgomery, how are you?
Hi Ubul,       how are you?
Hi John,       how are you?
Hi Frederik,   how are you?
```

### Display numbers
```py
numbers: list[int] = [10.75, 200, 300.8, 0.921]
print("Align numbers in a column:")
for n in numbers:
    print(f"{n:>8}")
```
Output:
```
Align numbers in a column:
   10.75
     200
   300.8
   0.921
```