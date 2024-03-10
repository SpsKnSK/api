class Man:
    Name:str
    Surname:str
    Age:int

    def __init__(self, name:str, surname:str, age:int) -> None:
        self.Name, self.Surname, self.Age = name, surname, age

class Student(Man):
    Notes:list[int]

    def __init__(self, name: str, surname: str, age: int) -> None:
        super().__init__(name, surname, age)
        self.Notes = []

    def Learn(self)->None:
        print(f"{self.Name} {self.Surname} at age {self.Age} learns")

    def Answers(self)->None:
        print(f"{self.Name} {self.Surname} at age {self.Age} answers")

class Teacher(Man):
    NumberOfLessonsPerWeek:int
    FieldOfStudy:str

    def __init__(self, name:str, surname:str, age:int, numberOfLessonsPerWeek:int, fieldOfStudy:str) -> None:
        super().__init__(name,surname, age)
        self.NumberOfLessonsPerWeek, self.FieldOfStudy = numberOfLessonsPerWeek, fieldOfStudy

    def Questions(self, student:Student)->None:
        print(f"Teacher {self.Name} {self.Surname} at age {self.Age} questions student {student.Name} {student.Surname}")
    
class Principal(Man):
    def Manage(self):
        print(f"Principal {self.Name} {self.Surname} at age {self.Age} manages the school")

student = Student("Bob", "Novak", 16)
teacher = Teacher("Alice", "White", 40, 20, "Mathematics")
principal = Principal("Dave", "MacDonald", 50)

student.Learn()
student.Answers()

teacher.Questions(student)
principal.Manage()