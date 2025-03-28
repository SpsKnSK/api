import pandas as pd
import os
directory = os.path.dirname(__file__)
file_path = os.path.join(directory, '01_students.csv')

class Student:

    def __init__(self, name:str, surname:str, age:int, sex:str, averageGrade:float, heightInCm:int, weightInKg:int):
        self.Name, self.Surname, self.Age, self.Sex, self.AverageGrade, self.HeightInCm, self.WeightInKg = name, surname, age, sex, averageGrade, heightInCm, weightInKg
    def __str__(self):
        return f"{self.Name}, {self.Surname} {self.Age}"
    def __repr__(self):
        return f"({self.__str__()})"

df = pd.read_csv(file_path)

students : list[Student] = [Student(row['name'], row['surname'], row['age'], row['sex'], row['average score'], row['height in cm'], row['weight in kg'])for _, row in df.iterrows()]

for s in students:
    print(s)

