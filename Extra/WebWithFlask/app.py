from flask import Flask, render_template, request, redirect, url_for, session
from datetime import date
from Models.models import Lesson, Student, SchoolClass
import random
from functools import wraps


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
            Student(1, "Smith", "John", date(2010, 5, 14), "123 Main St", sex="M"),
            Student(2, "Brown", "Alice", date(2011, 7, 22), "456 Oak Ave", sex="F"),
            Student(4, "Johnson", "Emily", date(2010, 8, 10), "789 Maple St", sex="F"),
            Student(
                5, "Williams", "Michael", date(2011, 2, 18), "321 Birch Rd", sex="M"
            ),
            Student(6, "Jones", "Olivia", date(2010, 11, 5), "654 Cedar Ave", sex="F"),
            Student(7, "Garcia", "Daniel", date(2011, 4, 30), "987 Spruce Dr", sex="M"),
            Student(
                8, "Martinez", "Sophia", date(2010, 9, 12), "159 Willow Ln", sex="F"
            ),
            Student(9, "Davis", "James", date(2011, 1, 25), "753 Aspen Ct", sex="M"),
            Student(10, "Rodriguez", "Mia", date(2010, 6, 8), "852 Poplar St", sex="F"),
            Student(
                11,
                "Hernandez",
                "Benjamin",
                date(2011, 3, 19),
                "951 Walnut Ave",
                sex="M",
            ),
            Student(
                12, "Lopez", "Charlotte", date(2010, 12, 3), "357 Chestnut Rd", sex="F"
            ),
            Student(
                13, "Gonzalez", "Elijah", date(2011, 5, 27), "258 Hickory Dr", sex="M"
            ),
            Student(
                14, "Wilson", "Amelia", date(2010, 7, 15), "654 Magnolia Ln", sex="F"
            ),
            Student(
                15, "Anderson", "Logan", date(2011, 10, 21), "159 Sycamore Ct", sex="M"
            ),
            Student(
                16, "Thomas", "Harper", date(2010, 3, 29), "753 Redwood St", sex="F"
            ),
            Student(
                17, "Taylor", "Lucas", date(2011, 8, 6), "852 Dogwood Ave", sex="M"
            ),
        ],
    ),
    SchoolClass(
        2,
        "Class 2B",
        [
            Student(3, "Taylor", "Bob", date(2010, 3, 2), "789 Pine Rd", sex="M"),
            Student(18, "Moore", "Ella", date(2010, 9, 14), "123 Oak St", sex="F"),
            Student(
                19, "Jackson", "Henry", date(2011, 2, 11), "456 Maple Ave", sex="M"
            ),
            Student(20, "Martin", "Avery", date(2010, 11, 23), "789 Birch Rd", sex="F"),
            Student(21, "Lee", "Jack", date(2011, 5, 8), "321 Cedar St", sex="M"),
            Student(
                22, "Perez", "Scarlett", date(2010, 7, 30), "654 Spruce Ave", sex="F"
            ),
            Student(23, "White", "Mason", date(2011, 4, 17), "987 Willow Dr", sex="M"),
            Student(24, "Harris", "Lily", date(2010, 10, 2), "159 Aspen Ln", sex="F"),
            Student(
                25, "Sanchez", "Carter", date(2011, 1, 13), "753 Poplar Ct", sex="M"
            ),
            Student(26, "Clark", "Grace", date(2010, 6, 25), "852 Walnut St", sex="F"),
            Student(
                27,
                "Ramirez",
                "Sebastian",
                date(2011, 3, 7),
                "951 Chestnut Ave",
                sex="M",
            ),
            Student(28, "Lewis", "Zoe", date(2010, 12, 19), "357 Hickory Rd", sex="F"),
            Student(
                29, "Robinson", "David", date(2011, 8, 3), "258 Magnolia Dr", sex="M"
            ),
            Student(
                30, "Walker", "Layla", date(2010, 5, 11), "654 Sycamore Ln", sex="F"
            ),
            Student(
                31, "Young", "Matthew", date(2011, 10, 28), "159 Redwood Ct", sex="M"
            ),
            Student(32, "Allen", "Chloe", date(2010, 2, 16), "753 Dogwood St", sex="F"),
            Student(
                33, "Smith", "Bob", date(2011, 3, 19), "798/A Washington St", sex="M"
            ),
            Student(
                34, "Smith", "Amalia", date(2011, 3, 19), "798/A Washington St", sex="F"
            ),
            Student(
                35, "Bluehorn", "Jessica", date(2009, 12, 19), "11 Pinewood St", sex="F"
            ),
        ],
    ),
    SchoolClass(3, "Class 3C", []),
]

app = Flask(__name__, template_folder="templates", static_folder="static")
app.secret_key = "supersecretkey"  # Use a secure key in production

# Dummy user for demonstration
USERS = {"admin": "password123", "test": "123"}


def is_logged_in():
    return session.get("logged_in", False)


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username in USERS and USERS[username] == password:
            session["logged_in"] = True
            return redirect(url_for("index"))
        else:
            error = "Invalid username or password."
    return render_template("login.html", error=error)


@app.route("/logout")
def logout():
    session.pop("logged_in", None)
    return redirect(url_for("login"))


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not is_logged_in():
            return redirect(url_for("login"))
        return f(*args, **kwargs)

    return decorated_function


@app.route("/")
@login_required
def index():
    return render_template("classes.html", classes=classes)


@app.route("/class/<int:class_id>")
@login_required
def class_detail(class_id):
    cls = next((c for c in classes if c.id == class_id), None)
    if not cls:
        return "Class not found", 404
    students = sorted(cls.students, key=lambda s: (s.surname, s.name))
    return render_template(
        "class_detail.html", cls=cls, lessons=lessons, students=students
    )


@app.route("/student/<int:student_id>")
@login_required
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
