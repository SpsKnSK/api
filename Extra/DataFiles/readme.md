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
Lets' make a program, that will print the students by gender. `07_groupByGender.py`
```py
sexDictionary : dict[str, list[Student]] = {"Boys" if s == 'M' else 'Girls':[student for student in students if student.Sex == s] for s in set([s.Sex for s in students])}
```

1. We create a set of sexes: `set([s.Sex for s in students])` this will give us the exact number of groups
2. we rename the key in the dictionary by `"Boys" if s == 'M' else 'Girls'` -> if `sex == 'M'` then we write Boys, else Girls
3. To create the value (list of students), we take only the ones that have the same sex, as we requested: `[student for student in students if student.Sex == s]`
4. The dictionary comprehension is created by the `{k:v for k in list}` then defining the key, in this case the gender and defining all the students that have this gender

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

# Reading CSV file
CSV (comma separated value) files can contain header rows, where each column is named. `08_readCsv.py`
The header of the csv file is `name,surname,age,sex,average score,height in cm,weight in kg`

```py
import pandas as pd
df = pd.read_csv(file_path)
students : list[Student] = [Student(row['name'], row['surname'], row['age'], row['sex'], row['average score'], row['height in cm'], row['weight in kg'])for _, row in df.iterrows()]
```

> Note, that panda reads each row and the column is the header's name as it is in the file 

# JSON (JavaScript Object Notation)

**JSON** is a lightweight, human-readable data interchange format that is widely used for exchanging data between web servers, web applications, and mobile apps. It is a text-based format that represents data as a collection of key-value pairs, arrays, and objects.

## Key Features:

- Lightweight and easy to read/write
- Platform-independent and language-agnostic
- Human-readable and easily parseable by machines
- Supports data types such as strings, numbers, booleans, arrays, and objects

## Example JSON Data:
```json
{
  "name": "John Doe",
  "age": 30,
  "address": {
    "street": "123 Main St",
    "city": "Anytown",
    "state": "CA",
    "zip": "12345"
  },
  "hobbies": ["reading", "hiking", "coding"]
}
```

### JSON is commonly used for:

- Data exchange between web servers and web - applications
- Mobile app data storage and retrieval
- Configuration files and settings
- API responses and requests

In our example `09_ReadAndWriteJson.py` we used JSON as following
- `import json`
- In `Student` class created 2 methods `to_dict` and `from_dict`
- Writing to file is done as:
    ```py
    def save_students_to_json(students, file_path):
        data = [student.to_dict() for student in students]
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    ```
    First we create a dictionary of all students (data) and then using the `json.dump` method we save the json formatted string to the file
- Reading from the file is done as: 
    ```py
    def read_students_from_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        students = [Student.from_dict(student_data) for student_data in data]
    return students
    ```
    The raw data is read from the file using `json.load` and then we go through all the student's dictionary representation and creating our `Student` intance as `Student.from_dict(student_data)`

