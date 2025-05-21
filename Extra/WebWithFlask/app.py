from flask import Flask, render_template
from datetime import date
from Models.models import Lesson, Student, SchoolClass
import random


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
            Student(1, "Smith", "John", date(2010, 5, 14), "123 Main St"),
            Student(2, "Brown", "Alice", date(2011, 7, 22), "456 Oak Ave"),
            Student(4, "Johnson", "Emily", date(2010, 8, 10), "789 Maple St"),
            Student(5, "Williams", "Michael", date(2011, 2, 18), "321 Birch Rd"),
            Student(6, "Jones", "Olivia", date(2010, 11, 5), "654 Cedar Ave"),
            Student(7, "Garcia", "Daniel", date(2011, 4, 30), "987 Spruce Dr"),
            Student(8, "Martinez", "Sophia", date(2010, 9, 12), "159 Willow Ln"),
            Student(9, "Davis", "James", date(2011, 1, 25), "753 Aspen Ct"),
            Student(10, "Rodriguez", "Mia", date(2010, 6, 8), "852 Poplar St"),
            Student(11, "Hernandez", "Benjamin", date(2011, 3, 19), "951 Walnut Ave"),
            Student(12, "Lopez", "Charlotte", date(2010, 12, 3), "357 Chestnut Rd"),
            Student(13, "Gonzalez", "Elijah", date(2011, 5, 27), "258 Hickory Dr"),
            Student(14, "Wilson", "Amelia", date(2010, 7, 15), "654 Magnolia Ln"),
            Student(15, "Anderson", "Logan", date(2011, 10, 21), "159 Sycamore Ct"),
            Student(16, "Thomas", "Harper", date(2010, 3, 29), "753 Redwood St"),
            Student(17, "Taylor", "Lucas", date(2011, 8, 6), "852 Dogwood Ave"),
        ],
    ),
    SchoolClass(
        2,
        "Class 2B",
        [
            Student(3, "Taylor", "Bob", date(2010, 3, 2), "789 Pine Rd"),
            Student(18, "Moore", "Ella", date(2010, 9, 14), "123 Oak St"),
            Student(19, "Jackson", "Henry", date(2011, 2, 11), "456 Maple Ave"),
            Student(20, "Martin", "Avery", date(2010, 11, 23), "789 Birch Rd"),
            Student(21, "Lee", "Jack", date(2011, 5, 8), "321 Cedar St"),
            Student(22, "Perez", "Scarlett", date(2010, 7, 30), "654 Spruce Ave"),
            Student(23, "White", "Mason", date(2011, 4, 17), "987 Willow Dr"),
            Student(24, "Harris", "Lily", date(2010, 10, 2), "159 Aspen Ln"),
            Student(25, "Sanchez", "Carter", date(2011, 1, 13), "753 Poplar Ct"),
            Student(26, "Clark", "Grace", date(2010, 6, 25), "852 Walnut St"),
            Student(27, "Ramirez", "Sebastian", date(2011, 3, 7), "951 Chestnut Ave"),
            Student(28, "Lewis", "Zoe", date(2010, 12, 19), "357 Hickory Rd"),
            Student(29, "Robinson", "David", date(2011, 8, 3), "258 Magnolia Dr"),
            Student(30, "Walker", "Layla", date(2010, 5, 11), "654 Sycamore Ln"),
            Student(31, "Young", "Matthew", date(2011, 10, 28), "159 Redwood Ct"),
            Student(32, "Allen", "Chloe", date(2010, 2, 16), "753 Dogwood St"),
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
