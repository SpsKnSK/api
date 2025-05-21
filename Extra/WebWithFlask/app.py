from flask import Flask, render_template
from datetime import date

app = Flask(__name__)

# Sample data
classes = [
    {
        "id": 1,
        "name": "Class 1A",
        "students": [
            {
                "id": 1,
                "surname": "Smith",
                "name": "John",
                "dob": date(2010, 5, 14),
                "address": "123 Main St",
                "grades": [4, 5, 3, 4, 5, 4],
            },
            {
                "id": 2,
                "surname": "Brown",
                "name": "Alice",
                "dob": date(2011, 7, 22),
                "address": "456 Oak Ave",
                "grades": [5, 5, 4, 5, 5, 5],
            },
        ],
    },
    {
        "id": 2,
        "name": "Class 2B",
        "students": [
            {
                "id": 3,
                "surname": "Taylor",
                "name": "Bob",
                "dob": date(2010, 3, 2),
                "address": "789 Pine Rd",
                "grades": [3, 4, 4, 3, 4, 3],
            },
        ],
    },
    {"id": 3, "name": "Class 3C", "students": []},
]


def calculate_age(dob):
    today = date.today()
    return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))


def average(grades):
    return round(sum(grades) / len(grades), 2) if grades else 0


@app.route("/")
def index():
    return render_template("classes.html", classes=classes)


@app.route("/class/<int:class_id>")
def class_detail(class_id):
    cls = next((c for c in classes if c["id"] == class_id), None)
    if not cls:
        return "Class not found", 404
    students = sorted(cls["students"], key=lambda s: (s["surname"], s["name"]))
    for s in students:
        s["age"] = calculate_age(s["dob"])
        s["avg"] = average(s["grades"])
    return render_template("class_detail.html", cls=cls, students=students)


@app.route("/student/<int:student_id>")
def student_detail(student_id):
    for cls in classes:
        for s in cls["students"]:
            if s["id"] == student_id:
                student = s.copy()
                student["age"] = calculate_age(student["dob"])
                student["avg"] = average(student["grades"])
                return render_template("student_detail.html", student=student)
    return "Student not found", 404


if __name__ == "__main__":
    app.run(debug=True)
