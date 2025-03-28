# Reading values from file
There is the following file of students (name, surname, age, sex, average grade, height (cm) and weight (kg))
```
Emily,Wilson,12,F,1.95,160,35
Oliver,Gray,11,M,3.62,165,40
Ava,Taylor,13,F,2.02,155,32
Ethan,Brown,14,M,1.99,170,45
Lily,White,12,F,4.03,158,36
Noah,Miller,13,M,2.91,162,38
Sophia,Patel,14,F,1.51,165,42
Mason,Harris,15,M,3.22,168,48
Isabella,Rodriguez,13,F,2.78,160,35
Logan,Walker,14,M,4.30,165,40
Charlotte,Davis,15,F,1.27,170,45
Alexander,Thomas,12,M,3.65,162,38
Mia,Robinson,13,F,2.12,155,32
Benjamin,King,14,M,4.58,165,40
Harper,Williams,15,F,1.14,168,48
```

## Write them out

```py
import os
directory = os.path.dirname(__file__)
file_path = os.path.join(directory, '01_students.txt')
with open(file_path, 'r') as file:
    lines = file.readlines()
    for l in lines:
        print(l.strip())
```

## Write out just the names and sex

```py
import os
directory = os.path.dirname(__file__)
file_path = os.path.join(directory, '01_students.txt')
with open(file_path, 'r') as file:
    lines = file.readlines()
    for l in lines:
        columns = l.split(',')
        print(columns[0], "Girl" if columns[3]== 'F' else "Boy")
```

# Use `class`
For more complex operations, use class `Student` as in:
- `03_writeOut_withClass.py`
- `04_writeOut_withClass.py`
- `05_writeOut_withClass.py`

With the class it is easier to get the correct value, as the value is named as a property of the class. Instead of `line[5]` where we have no context, what that value contains, we use `student.HeightInCm` and we already have the context.

> Have a note that in `05_writeOut_withClass.py` `Student` class has a method without `self`: `FromLine` that returns a `Student` instance, this is called **on class** not on instance as: `student = Student.FromLine(l)` 

## Sorting
Sorting data can be tricky on a dataset, that is without context and wirking with indexes can lead to messy code. Our next task is to read the students' file and sort them by height and write out their names. `06_sortByheight.py`

```py
students : list[Student] = []

with open(file_path, 'r') as file:
    [students.append(Student.FromLine(l)) for l in file.readlines()]

students.sort(key=lambda x: x.HeightInCm, reverse=True)
header:str = f"{'Name':<10}HeightInCm"
print(header)
print("-"*len(header))
for s in students:
    print(f"{s.Name:<10}{s.HeightInCm}")
```
Here we fill the `students` list with a student then sort them by height and finally we write out their name and height

## Groups
Lets' make a program, that will print out how many students do we have by gender.

> With **pandas** it is just as followinig: 
> ```py
> import pandas as pd
> df = pd.DataFrame(data)
> grouped_Data = df.groupby('sex')
> for name, group in grouped_df:
>    print(f"**{name.upper()}**")
>    print(group)
>    print()
> ```