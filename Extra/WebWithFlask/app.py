from flask import Flask, render_template
from datetime import date
from Models.models import Lesson, Student, SchoolClass


# Define lessons
lessons = [
    Lesson("English", "English language and literature"),
    Lesson("Maths", "Mathematics"),
    Lesson("Physics", "Physics"),
    Lesson("Geography", "Geography"),
    Lesson("IT", "Information Technology"),
    Lesson("PE", "Physical Education"),
]

# Sample data using classes
classes = [
    SchoolClass(
        1,
        "Class 1A",
        [
            Student(
                1, "Smith", "John", date(2010, 5, 14), "123 Main St", [4, 5, 3, 4, 5, 4]
            ),
            Student(
                2,
                "Brown",
                "Alice",
                date(2011, 7, 22),
                "456 Oak Ave",
                [5, 5, 4, 5, 5, 5],
            ),
        ],
    ),
    SchoolClass(
        2,
        "Class 2B",
        [
            Student(
                3, "Taylor", "Bob", date(2010, 3, 2), "789 Pine Rd", [3, 4, 4, 3, 4, 3]
            ),
        ],
    ),
    SchoolClass(3, "Class 3C", []),
]

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("classes.html", classes=classes)


@app.route("/class/<int:class_id>")
def class_detail(class_id):
    cls = next((c for c in classes if c.id == class_id), None)
    if not cls:
        return "Class not found", 404
    students = sorted(cls.students, key=lambda s: (s.surname, s.name))
    return render_template("class_detail.html", cls=cls, students=students)


@app.route("/student/<int:student_id>")
def student_detail(student_id):
    for cls in classes:
        for s in cls.students:
            if s.id == student_id:
                return render_template(
                    "student_detail.html", student=s, lessons=lessons, cls=cls
                )
    return "Student not found", 404


if __name__ == "__main__":
    app.run(debug=True)
