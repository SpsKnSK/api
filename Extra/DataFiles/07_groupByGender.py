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
    def __repr__(self):
        return f"({self.__str__()})"

students : list[Student] = []

with open(file_path, 'r') as file:
    [students.append(Student.FromLine(l)) for l in file.readlines()]

sexDictionary : dict[str, list[Student]] = {"Boy" if s == 'M' else 'Girl':[student for student in students if student.Sex == s] for s in set([s.Sex for s in students])}

for k,v in sexDictionary.items():
    header:str = f"{k}\n{'Surname':<10}Name"
    print(header)
    print("-"*len(header))
    for s in sorted(v,key=lambda x: x.Surname):
        print(f"{s.Surname:<10}{s.Name}")
    print("\n")