from flask import Blueprint, render_template, request, redirect, url_for, session
from Db.school_db import SchoolDB

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        schoolDb = SchoolDB()
        user = schoolDb.get_user_by_credentials(username, password)
        if user:
            session["logged_in"] = True
            session["user_name"] = username
            session["roles"] = user.roles
            return redirect(url_for("classes.index"))
        else:
            error = "Invalid username or password."
    return render_template("login.html", error=error)


@auth_bp.route("/logout")
def logout():
    for session_key in list(session.keys()):
        session.pop(session_key, None)
    return redirect(url_for("auth.login"))
