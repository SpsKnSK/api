from Db.school_db import SchoolDB
from datetime import date
from random import randint, choice
import names


if __name__ == "__main__":
    import os

    db = SchoolDB()
    if db.db_path and os.path.exists(db.db_path):
        os.remove(db.db_path)
    db.create_all()
    db.add_user("admin", "123", roles=["admin"])
    db.add_user("test", "123", roles=["viewer"])

    lessons = [
        ("English", "English language and literature"),
        ("Maths", "Mathematics"),
        ("Physics", "Physics"),
        ("Geography", "Geography"),
        ("IT", "Information Technology"),
        ("PE", "Physical Education"),
    ]
    for lesson in lessons:
        db.add_lesson(lesson[0], lesson[1])

    classes = [
        "Class 1A",
        "Class 2B",
        "Class 3C",
        "Class 4D",
        "Class 5E",
    ]
    for c in classes:
        class_id = db.add_class(c)
        studentIds = []
        for _ in range(randint(10, 35)):
            sex = choice(["male", "female"])
            student_id = db.add_student(
                names.get_first_name(gender=sex),
                names.get_last_name(),
                sex[0].upper(),
                date(randint(2000, 2010), randint(1, 12), randint(1, 28)),
                f"{randint(1, 999)} {names.get_last_name()}",
            )
            studentIds.append(student_id)
        student_class_pairs = [(class_id, student_id) for student_id in studentIds]
        db.add_more_student_to_class(student_class_pairs)

    student_lesson_grades = [
        (student.id, lesson.id, randint(1, 5))
        for student in db.get_students()
        for lesson in db.get_lessons()
    ]
    db.add_more_student_lesson(student_lesson_grades)
