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

    def __init__(self, name:str, surname:str, age:int, sex:str, averageGrade:float, heightInCm:int, weightInKg:int):
        self.Name, self.Surname, self.Age, self.Sex, self.AverageGrade, self.HeightInCm, self.WeightInKg = name, surname, age, sex, averageGrade, heightInCm, weightInKg


with open(file_path, 'r') as file:
    lines = file.readlines()
    for l in lines:
        columns = l.split(',')
        student = Student(columns[0], columns[1], int(columns[2]), columns[3], float(columns[4]), int(columns[5]), int(columns[6]))
        print(f"{student.Name} {student.Sex}")