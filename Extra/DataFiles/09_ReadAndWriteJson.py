import json
import os
directory = os.path.dirname(__file__)
file_path = os.path.join(directory, '01_students.json')

class Student:

    def __init__(self, name:str, surname:str, age:int, sex:str, averageGrade:float, heightInCm:int, weightInKg:int):
        self.Name, self.Surname, self.Age, self.Sex, self.AverageGrade, self.HeightInCm, self.WeightInKg = name, surname, age, sex, averageGrade, heightInCm, weightInKg

    def __str__(self):
        return f"{self.Name}, {self.Surname} {self.Age}"
    def __repr__(self):
        return f"({self.__str__()})"
    
    def to_dict(self):
        return {
            'Name': self.Name,
            'Surname': self.Surname,
            'Age': self.Age,
            'Sex': self.Sex,
            'AverageGrade': self.AverageGrade,
            'HeightInCm': self.HeightInCm,
            'WeightInKg': self.WeightInKg
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data['Name'],
            surname=data['Surname'],
            age=data['Age'],
            sex=data['Sex'],
            averageGrade=data['AverageGrade'],
            heightInCm=data['HeightInCm'],
            weightInKg=data['WeightInKg']
        )

def save_students_to_json(students, file_path):
    data = [student.to_dict() for student in students]
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def read_students_from_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        students : list[Student] = [Student.from_dict(student_data) for student_data in data]
    return students

students : list[Student] = [
    Student("Emily", "Wilson", 12, "F", 1.0, 160, 35),
    Student("Oliver", "Gray", 11, "M", 3.0, 165, 40),
    Student("Ava", "Taylor", 13, "F", 2.0, 155, 32)
]

save_students_to_json(students, file_path)
loaded_students = read_students_from_json(file_path)

print(loaded_students)
