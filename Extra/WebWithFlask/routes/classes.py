from flask import Blueprint, render_template, session
from Db.school_db import SchoolDB
from helpers.auth_helpers import login_required

classes_bp = Blueprint("classes", __name__)


@classes_bp.route("/")
@login_required
def index():
    schoolDb = SchoolDB()
    classes = schoolDb.get_classes()
    return render_template(
        "classes.html", classes=classes, user_name=session.get("user_name", "")
    )


@classes_bp.route("/class/<int:class_id>")
@login_required
def class_detail(class_id):
    schoolDb = SchoolDB()
    cls = schoolDb.get_class_by_id(class_id)
    if not cls:
        return "Class not found", 404
    students = schoolDb.get_students_by_class(class_id)
    lessons = schoolDb.get_lessons_by_class(class_id)

    return render_template(
        "class_detail.html",
        cls=cls,
        lessons=lessons,
        students=students,
        user_name=session.get("user_name", ""),
    )
