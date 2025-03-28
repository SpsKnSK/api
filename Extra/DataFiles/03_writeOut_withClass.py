import os
directory = os.path.dirname(__file__)
file_path = os.path.join(directory, '01_students.txt')

class Student:
    Name:str
    Surname:str
    Age:int
    Sex:str
    AverageGrade:float
    HeightInCm:int
    WeightInKg:int


with open(file_path, 'r') as file:
    lines = file.readlines()
    for l in lines:
        columns = l.split(',')
        student = Student()
        student.Name = columns[0]
        student.Surname = columns[1]
        student.Age = int(columns[2])
        student.Sex = columns[3]
        student.AverageGrade = float(columns[4])
        student.HeightInCm = int(columns[5])
        student.WeightInKg = int(columns[6])
        print(f"{student.Name} {student.Sex}")