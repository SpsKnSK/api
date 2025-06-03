from datetime import date


class User:
    def __init__(self, id: int, username: str, roles: list[str]):
        self.id = id
        self.username = username
        self.roles = roles

    def __repr__(self):
        return f"User(username={self.username}, role={self.roles})"


class Lesson:
    def __init__(self, id: int, name: str, description: str):
        self.id = id
        self.name = name
        self.description = description


class LessonStats:
    def __init__(self, name: str, sex: str, grade: int):
        self.name = name
        self.sex = sex
        self.grade = grade


class StudentLesson(Lesson):
    def __init__(self, id: int, name: str, description: str, grade: int):
        super().__init__(id=id, name=name, description=description)
        self.grade = grade


class Student:
    def __init__(
        self,
        id,
        surname,
        name,
        dob,
        address,
        sex,
        averageGrade=0.0,
        classId=None,
        className=None,
    ):
        self.id = id
        self.surname = surname
        self.name = name
        self.dob = dob if isinstance(dob, date) else date.fromisoformat(dob)
        self.address = address
        self.sex = sex
        self.averageGrade = round(averageGrade, 2)
        self.classId = classId
        self.className = className

    def age(self):
        today = date.today()
        return (
            today.year
            - self.dob.year
            - ((today.month, today.day) < (self.dob.month, self.dob.day))
        )


class ClassSimple:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name


class ClassSummary(ClassSimple):
    def __init__(
        self,
        id: int,
        name: str,
        studentCount: int,
        girlsCount: int,
        boysCount: int,
        girlsAvg: float,
        boysAvg: float,
        averageGrade: float,
    ):
        super().__init__(id, name)
        self.studentCount = studentCount
        self.girlsCount = girlsCount
        self.boysCount = boysCount
        self.girlsAvg = round(girlsAvg, 2)
        self.boysAvg = round(boysAvg, 2)
        self.averageGrade = round(averageGrade, 2)
