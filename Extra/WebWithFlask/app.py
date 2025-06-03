from flask import Flask
from routes.classes import classes_bp
from routes.students import students_bp
from routes.auth import auth_bp

app = Flask(__name__, template_folder="templates", static_folder="static")
app.secret_key = "supersecretkey"  # Use a secure key in production


app.register_blueprint(classes_bp)
app.register_blueprint(students_bp)
app.register_blueprint(auth_bp)

if __name__ == "__main__":
    app.run(debug=True)
