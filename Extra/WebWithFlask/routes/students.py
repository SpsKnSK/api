import datetime
from flask import Blueprint, render_template, session, request, redirect, url_for
from Db.school_db import SchoolDB
from helpers.auth_helpers import login_required, role_required

students_bp = Blueprint("students", __name__)


@students_bp.route("/student/<int:student_id>")
@login_required
def student_detail(student_id):
    schoolDb = SchoolDB()
    student = schoolDb.get_student_by_id(student_id)
    if not student:
        return "Student not found", 404
    lessons = schoolDb.get_lessons_by_student(student_id)
    return render_template(
        "student_detail.html",
        student=student,
        lessons=lessons,
        user_name=session.get("user_name", ""),
    )


@students_bp.route("/student/new", methods=["GET"])
@login_required
@role_required("admin")
def student_create():
    schoolDB = SchoolDB()
    all_classes = schoolDB.get_classes()
    all_lessons = schoolDB.get_lessons()
    student = type(
        "Student",
        (),
        {
            "id": 0,
            "name": "test",
            "surname": "test",
            "dob": datetime.datetime.now().strftime("%Y-%m-%d"),
            "address": "test",
            "sex": "M",
            "classId": "1",
            "className": "",
        },
    )()
    return render_template(
        "student_edit.html",
        student=student,
        lessons=all_lessons,
        all_classes=all_classes,
        method="POST",
        user_name=session.get("user_name", ""),
    )


def parse_student_form(form):
    return {k: form.get(k, "") for k in ["name", "surname", "dob", "address", "sex"]}


def parse_class_id_form(form):
    class_id = form.get("class_id", "")
    return int(class_id) if class_id.isdigit() else 0


def parse_lesson_grades(form):
    grades = []
    for key, value in form.items():
        if key.startswith("student_lesson"):
            lesson_id = int(key.split("_")[2])
            grades.append((lesson_id, int(float(value))))
    return grades


@students_bp.route("/student/<int:student_id>/edit", methods=["GET", "PUT", "POST"])
@login_required
@role_required("admin")
def student_edit(student_id):
    schoolDB = SchoolDB()
    all_classes = schoolDB.get_classes()
    student = schoolDB.get_student_by_id(student_id)
    lessons = schoolDB.get_lessons_by_student(student_id)

    if request.method == "POST":
        form_method = request.form.get("_method")
        student_data = parse_student_form(request.form)
        lesson_grades = parse_lesson_grades(request.form)

        if form_method == "POST":
            student_id = schoolDB.add_student(
                name=student_data["name"],
                surname=student_data["surname"],
                sex=student_data["sex"],
                dob=student_data["dob"],
                address=student_data["address"],
            )
            class_id = parse_class_id_form(request.form)
            schoolDB.add_student_to_class(student_id=student_id, class_id=class_id)
            for lesson_id, grade in lesson_grades:
                schoolDB.add_student_lesson(
                    student_id=student_id,
                    lesson_id=lesson_id,
                    grade=grade,
                )
            return redirect(url_for("students.student_detail", student_id=student_id))

        elif form_method == "PUT":
            student.name = student_data["name"]
            student.surname = student_data["surname"]
            student.dob = student_data["dob"]
            student.address = student_data["address"]
            student.sex = student_data["sex"]
            student.classId = parse_class_id_form(request.form)
            schoolDB.update_student(student)
            for lesson_id, grade in lesson_grades:
                schoolDB.update_student_lesson(lesson_id, grade)
            return redirect(url_for("students.student_detail", student_id=student_id))

    return render_template(
        "student_edit.html",
        student=student,
        lessons=lessons,
        all_classes=all_classes,
        method="PUT",
        user_name=session.get("user_name", ""),
    )
