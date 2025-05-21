from datetime import date

class Lesson:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Student:
    def __init__(self, id, surname, name, dob, address, grades):
        self.id = id
        self.surname = surname
        self.name = name
        self.dob = dob
        self.address = address
        self.grades = grades  # List of grades, one per lesson
    def age(self):
        today = date.today()
        return (
            today.year
            - self.dob.year
            - ((today.month, today.day) < (self.dob.month, self.dob.day))
        )
    def avg(self):
        return round(sum(self.grades) / len(self.grades), 2) if self.grades else 0

class SchoolClass:
    def __init__(self, id, name, students):
        self.id = id
        self.name = name
        self.students = students
