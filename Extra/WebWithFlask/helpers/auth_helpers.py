from flask import session, redirect, url_for
from functools import wraps


def is_logged_in():
    return session.get("logged_in", False)


def get_user_role():
    return session.get("roles", "viewer")


def role_required(role):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not is_logged_in() or role not in session.get("roles"):
                return redirect(url_for("auth.login"))
            return f(*args, **kwargs)

        return decorated_function

    return decorator


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not is_logged_in():
            return redirect(url_for("auth.login"))
        return f(*args, **kwargs)

    return decorated_function
