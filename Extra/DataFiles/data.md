# Working with data

## Reading values from file
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

### Write them out

```py
import os
directory = os.path.dirname(__file__)
file_path = os.path.join(directory, '01_students.txt')
with open(file_path, 'r') as file:
    lines = file.readlines()
    for l in lines:
        print(l.strip())
```

### Write out just the names and sex

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

## Use `class`
For more complex operations, use class `Student` as in `03_writeOut_withClass.py`

Let's write a program, that will sort the students by height and write out their name
