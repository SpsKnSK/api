import os
directory = os.path.dirname(__file__)
file_path = os.path.join(directory, '01_students.txt')

class Student:

    def __init__(self, name:str, surname:str, age:int, sex:str, averageGrade:float, heightInCm:int, weightInKg:int):
        self.Name, self.Surname, self.Age, self.Sex, self.AverageGrade, self.HeightInCm, self.WeightInKg = name, surname, age, sex, averageGrade, heightInCm, weightInKg

    def FromLine(line:str, separator:str = ',')->"Student":
        columns = line.split(separator)
        return Student(columns[0], columns[1], int(columns[2]), columns[3], float(columns[4]), int(columns[5]), int(columns[6]))
    def __str__(self):
        return f"{self.Name}, {self.Surname} {self.Age}"

students : list[Student] = []

with open(file_path, 'r') as file:
    [students.append(Student.FromLine(l)) for l in file.readlines()]

students.sort(key=lambda x: x.HeightInCm, reverse=True)
header:str = f"{'Name':<10}HeightInCm"
print(header)
print("-"*len(header))
for s in students:
    print(f"{s.Name:<10}{s.HeightInCm}")