import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
from Models.models import (
    Student,
    ClassSimple,
    ClassSummary,
    Lesson,
    LessonStats,
    User,
    StudentLesson,
)


DB_PATH = "tamas.torok\FlaskApplicationWithCopilot\Db\school.db"


class SchoolDB:
    def __init__(self, db_path=DB_PATH):
        self.db_path = db_path

    def get_connection(self):
        return sqlite3.connect(self.db_path)

    def create_all(self):
        with self.get_connection() as conn:
            c = conn.cursor()
            # Student table
            c.execute(
                """
                CREATE TABLE IF NOT EXISTS student (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    surname TEXT NOT NULL,
                    sex TEXT NOT NULL,
                    dob TEXT,
                    address TEXT
                )
            """
            )
            # Class table
            c.execute(
                """
                CREATE TABLE IF NOT EXISTS class (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL
                )
            """
            )
            # Class-Student connection table
            c.execute(
                """
                CREATE TABLE IF NOT EXISTS class_student (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    class_id INTEGER,
                    student_id INTEGER,
                    FOREIGN KEY (class_id) REFERENCES class(id),
                    FOREIGN KEY (student_id) REFERENCES student(id)
                )
            """
            )
            # Lesson table
            c.execute(
                """
                CREATE TABLE IF NOT EXISTS lesson (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    description TEXT
                )
            """
            )
            # Student-Lesson connection table (with grades)
            c.execute(
                """
                CREATE TABLE IF NOT EXISTS student_lesson (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    student_id INTEGER,
                    lesson_id INTEGER,
                    grade REAL,
                    FOREIGN KEY (student_id) REFERENCES student(id),
                    FOREIGN KEY (lesson_id) REFERENCES lesson(id)
                )
            """
            )
            # User table
            c.execute(
                """
                CREATE TABLE IF NOT EXISTS user (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    password_hash TEXT NOT NULL
                )
            """
            )
            # Roles table
            c.execute(
                """
                CREATE TABLE IF NOT EXISTS role (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT UNIQUE NOT NULL
                )
            """
            )
            # User-Roles connection table
            c.execute(
                """
                CREATE TABLE IF NOT EXISTS user_roles (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    role_id INTEGER,
                    FOREIGN KEY (user_id) REFERENCES user(id),
                    FOREIGN KEY (role_id) REFERENCES role(id)
                )
            """
            )
            conn.commit()

    def add_lesson(self, name: str, description: str = None):
        with self.get_connection() as conn:
            c = conn.cursor()
            c.execute(
                "INSERT INTO lesson (name, description) VALUES (?, ?)",
                (name, description),
            )
            conn.commit()
            return c.lastrowid

    def add_student_lesson(self, student_id: int, lesson_id: int, grade: int):
        with self.get_connection() as conn:
            c = conn.cursor()
            c.execute(
                "INSERT INTO student_lesson (student_id, lesson_id, grade) VALUES (?, ?, ?)",
                (student_id, lesson_id, grade),
            )
            conn.commit()
            return c.lastrowid

    def add_more_student_lesson(
        self, student_lesson_grades: list[tuple[int, int, int]]
    ):
        with self.get_connection() as conn:
            c = conn.cursor()
            c.executemany(
                "INSERT INTO student_lesson (student_id, lesson_id, grade) VALUES (?, ?, ?)",
                student_lesson_grades,
            )
            conn.commit()

    def add_class(self, name: str):
        with self.get_connection() as conn:
            c = conn.cursor()
            c.execute("INSERT INTO class (name) VALUES (?)", (name,))
            conn.commit()
            return c.lastrowid

    def add_student(
        self, name: str, surname: str, sex: str, dob: str = None, address: str = None
    ):
        with self.get_connection() as conn:
            c = conn.cursor()
            c.execute(
                "INSERT INTO student (name, surname, sex, dob, address) VALUES (?, ?, ?, ?, ?)",
                (name, surname, sex, dob, address),
            )
            conn.commit()
            return c.lastrowid

    def add_student_to_class(self, student_id: int, class_id: int):
        with self.get_connection() as conn:
            c = conn.cursor()
            c.execute(
                "INSERT INTO class_student (class_id, student_id) VALUES (?, ?)",
                (class_id, student_id),
            )
            conn.commit()
            return c.lastrowid

    def add_more_student_to_class(self, student_class: list[tuple[int, int]]):
        with self.get_connection() as conn:
            c = conn.cursor()
            c.executemany(
                "INSERT INTO class_student (class_id, student_id) VALUES (?, ?)",
                student_class,
            )
            conn.commit()

    def add_user(self, username: str, password: str, roles=None):
        password_hash = generate_password_hash(password)
        with self.get_connection() as conn:
            c = conn.cursor()
            c.execute(
                "INSERT INTO user (username, password_hash) VALUES (?, ?)",
                (username, password_hash),
            )
            user_id = c.lastrowid
            if roles:
                for role in roles:
                    c.execute("SELECT id FROM role WHERE name=?", (role,))
                    role_row = c.fetchone()
                    if role_row:
                        role_id = role_row[0]
                    else:
                        c.execute("INSERT INTO role (name) VALUES (?)", (role,))
                        role_id = c.lastrowid
                    c.execute(
                        "INSERT INTO user_roles (user_id, role_id) VALUES (?, ?)",
                        (user_id, role_id),
                    )
            conn.commit()
        return user_id

    def get_lessons(self):

        with self.get_connection() as conn:
            c = conn.cursor()
            c.execute("SELECT id, name, description FROM lesson")
            rows = c.fetchall()
            return [Lesson(id=row[0], name=row[1], description=row[2]) for row in rows]

    def get_class_by_id(self, class_id):

        with self.get_connection() as conn:
            c = conn.cursor()
            c.execute("""SELECT * FROM class WHERE id = ?""", (class_id,))
            row = c.fetchone()
            return ClassSimple(id=row[0], name=row[1]) if row else None

    def get_classes(self):
        with self.get_connection() as conn:
            c = conn.cursor()
            c.execute(
                """SELECT 
                    c.id, 
                    c.name, 
                    COUNT(s.sex) AS studentCount,
                    SUM(CASE WHEN s.sex == 'F' THEN 1 END) AS girlsCount, 
                    SUM(CASE WHEN s.sex == 'M' THEN 1 END) AS boysCount, 
                    SUM(CASE WHEN s.sex == 'F' THEN average.averageGrade END)/SUM(CASE WHEN s.sex == 'F' THEN 1 END) AS girlsAvg, 
                    SUM(CASE WHEN s.sex == 'M' THEN average.averageGrade END)/SUM(CASE WHEN s.sex == 'M' THEN 1 END) AS boysAvg, 
                    avg(average.averageGrade) AS averageGrade
                FROM class c
                JOIN class_student cs ON c.id = cs.class_id
                JOIN student s ON cs.student_id = s.id
                JOIN (SELECT student_id, AVG(grade) averageGrade FROM student_lesson sl GROUP BY sl.student_id) AS average ON s.id = average.student_id
                GROUP BY c.id, c.name"""
            )
            return [
                ClassSummary(
                    id=row[0],
                    name=row[1],
                    studentCount=row[2],
                    girlsCount=row[3],
                    boysCount=row[4],
                    girlsAvg=row[5],
                    boysAvg=row[6],
                    averageGrade=row[7],
                )
                for row in c.fetchall()
            ]

    def get_students_by_class(self, class_id):
        with self.get_connection() as conn:
            c = conn.cursor()
            c.execute(
                """
                SELECT s.*, average.averageGrade
                FROM class_student cs
                JOIN student s ON cs.student_id = s.id
                JOIN (SELECT student_id, AVG(grade) averageGrade FROM student_lesson sl GROUP BY sl.student_id) AS average ON s.id = average.student_id
                WHERE 
                    cs.class_id = ?
                ORDER BY
                    s.surname,
                    s.Name
                """,
                (class_id,),
            )
            return [
                Student(
                    id=row[0],
                    name=row[1],
                    surname=row[2],
                    sex=row[3],
                    dob=row[4],
                    address=row[5],
                    averageGrade=row[6],
                )
                for row in c.fetchall()
            ]

    def get_lessons_by_class(self, class_id):
        with self.get_connection() as conn:
            c = conn.cursor()
            c.execute(
                """
                SELECT 
                l.name, 
                s.sex,
                sl.grade
            FROM class_student cs
            JOIN student s ON cs.student_id = s.id
            JOIN student_lesson sl ON s.id = sl.student_id
            JOIN lesson l ON l.id = sl.lesson_id
            WHERE 
                cs.class_id = ?
                """,
                (class_id,),
            )
            return [
                LessonStats(name=row[0], sex=row[1], grade=row[2])
                for row in c.fetchall()
            ]

    def update_student_lesson(self, student_lesson_id: int, grade: int):
        with self.get_connection() as conn:
            c = conn.cursor()
            c.execute(
                """
                UPDATE student_lesson
                SET grade = ?
                WHERE id = ?
            """,
                (grade, student_lesson_id),
            )
            conn.commit()

    def update_student(self, student: Student):
        with self.get_connection() as conn:
            c = conn.cursor()
            c.execute(
                """
                UPDATE student
                SET 
                      name = ?, 
                      surname = ?, 
                      dob = ?, 
                      address = ?
                WHERE id = ?
            """,
                (
                    student.name,
                    student.surname,
                    student.dob,
                    student.address,
                    student.id,
                ),
            )

    def get_students(self):

        with self.get_connection() as conn:
            c = conn.cursor()
            c.execute("SELECT id, name, surname, dob, address, sex FROM student")
            rows = c.fetchall()
            return [
                Student(
                    id=row[0],
                    name=row[1],
                    surname=row[2],
                    dob=row[3],
                    address=row[4],
                    sex=row[5],
                )
                for row in rows
            ]

    def get_student_by_id(self, student_id):
        with self.get_connection() as conn:
            c = conn.cursor()
            c.execute(
                """
                      SELECT 
                        s.*,
                        cs.class_id,
                        c.name
                    FROM class_student cs
                    JOIN class c ON cs.class_id = c.id
                    JOIN student s ON cs.student_id = s.id
                    -- JOIN student_lesson sl ON s.id = sl.student_id
                    -- JOIN lesson l ON l.id = sl.lesson_id
                    WHERE 
                        cs.student_id = ?
                      """,
                (student_id,),
            )
            row = c.fetchone()
            if not row:
                return None
            return Student(
                id=row[0],
                name=row[1],
                surname=row[2],
                sex=row[3],
                dob=row[4],
                address=row[5],
                classId=row[6],
                className=row[7],
            )

    def get_lessons_by_student(self, student_id):
        with self.get_connection() as conn:
            c = conn.cursor()
            c.execute(
                """
                SELECT
                    sl.id, 
                    l.name,
                    l.description,
                    sl.grade
                FROM student_lesson sl
                JOIN lesson l ON sl.lesson_id = l.id
                WHERE 
                    sl.student_id = ?
                ORDER BY
                    l.name
                """,
                (student_id,),
            )
            return [
                StudentLesson(id=row[0], name=row[1], description=row[2], grade=row[3])
                for row in c.fetchall()
            ]

    def get_user_by_credentials(self, username, password):
        with self.get_connection() as conn:
            c = conn.cursor()
            c.execute(
                "SELECT id, username, password_hash FROM user WHERE username = ?",
                (username,),
            )
            row = c.fetchone()
            if row and check_password_hash(row[2], password):
                user_id = row[0]
                # Retrieve roles
                c.execute(
                    """
                    SELECT r.name FROM role r
                    JOIN user_roles ur ON ur.role_id = r.id
                    WHERE ur.user_id = ?
                    """,
                    (user_id,),
                )
                roles = [r[0] for r in c.fetchall()]
                return User(id=row[0], username=row[1], roles=roles)
            return None
