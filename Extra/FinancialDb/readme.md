# SQLite

**SQLite** is a popular database management system that is easy to use and perfect for learning about databases. In this article, we'll cover the basics of **SQLite**, including what a database is, how to handle the DB Browser, what tables are, and some key concepts like primary keys, foreign keys, data types, and SQL queries.

## What is a Database?

A database (DB) is a collection of organized data that can be easily accessed, managed, and updated. Think of it as a digital filing system where you can store and retrieve information efficiently.

## How to Handle the DB Browser

DB Browser for **SQLite** is a graphical tool that allows you to create, design, and edit **SQLite** databases. Here's how to get started:

1. **Download and Install**: [Download](https://**SQLite**browser.org/dl/) and install DB Browser for **SQLite** from its official website.
2. **Create a New Database**: Open the DB Browser and click on "New Database" to create a new database file.
3. **Create Tables**: Use the "Create Table" option to define the structure of your tables.

## What is a Table?

A table is a collection of related data organized in rows and columns. Each row represents a record, and each column represents a field within the record. For example, a table called `students` might have columns like `id`, `name`, and `grade`.

## What are Primary Keys (PK) and Foreign Keys (FK)?

- **Primary Key (PK)**: A primary key is a unique identifier for each record in a table. It ensures that each record can be uniquely identified. For example, the `id` column in the `students` table can be a primary key.
- **Foreign Key (FK)**: A foreign key is a column that creates a relationship between two tables. It references the primary key of another table. For example, if you have a `grades` table, the `student_id` column can be a foreign key that references the `id` column in the `students` table.

## What Data Types Can Be Used?

**SQLite** supports several data types, including:

- **INTEGER**: Whole numbers
- **REAL**: Floating-point numbers
- **TEXT**: Text strings
- **BLOB**: Binary data

## What is a `SELECT`/Query?

A `SELECT` statement, or query, is used to **retrieve** data from a database. For example, to get all records from the `students` table, you can use:

```sql
SELECT * FROM students;
```

## What is a `JOIN`?

A `JOIN` is used to **combine** rows from two or more tables based on a related column. For example, to get the names and grades of students, you can use:

```sql
SELECT students.name, grades.grade
FROM students
JOIN grades ON students.id = grades.student_id;
```

## What is `WHERE`?

The `WHERE` clause is used to **filter** records based on a condition. For example, to get students with a grade higher than 80, you can use:

```sql
SELECT * FROM students
WHERE grade > 80;
```

## What is `GROUP BY`?

The `GROUP BY` clause is used to **group** rows that have the same values in specified columns. For example, to count the number of students in each grade, you can use:

```sql
SELECT grade, COUNT(*)
FROM students
GROUP BY grade;
```

Sure! Let's expand the examples to include the `grades` and `lessons` tables, and insert some data into them.

### Example 1: Creating Tables

```sql
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    grade INTEGER
);

CREATE TABLE lessons (
    id INTEGER PRIMARY KEY,
    name TEXT
);

CREATE TABLE grades (
    id INTEGER PRIMARY KEY,
    student_id INTEGER,
    lesson_id INTEGER,
    grade INTEGER,
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (lesson_id) REFERENCES lessons(id)
);
```

### Example 2: Inserting Data

```sql
-- Insert data into students table
INSERT INTO students (name, grade) VALUES ('Alice', 85);
INSERT INTO students (name, grade) VALUES ('Bob', 90);

-- Insert data into lessons table
INSERT INTO lessons (name) VALUES ('Math');
INSERT INTO lessons (name) VALUES ('Physics');
INSERT INTO lessons (name) VALUES ('PE');
INSERT INTO lessons (name) VALUES ('Drawing');
INSERT INTO lessons (name) VALUES ('History');

-- Insert data into grades table
INSERT INTO grades (student_id, lesson_id, grade) VALUES (1, 1, 95); -- Alice, Math
INSERT INTO grades (student_id, lesson_id, grade) VALUES (1, 2, 88); -- Alice, Physics
INSERT INTO grades (student_id, lesson_id, grade) VALUES (2, 1, 92); -- Bob, Math
INSERT INTO grades (student_id, lesson_id, grade) VALUES (2, 3, 85); -- Bob, PE
```

### Example 3: Selecting Data

```sql
SELECT * FROM students;
```

### Example 4: Joining Tables

```sql
SELECT students.name, lessons.name AS lesson, grades.grade
FROM students
JOIN grades ON students.id = grades.student_id
JOIN lessons ON grades.lesson_id = lessons.id;
```

### Example 5: Using WHERE

```sql
SELECT * FROM students
WHERE grade > 80;
```

### Example 6: Using GROUP BY

```sql
SELECT grade, COUNT(*)
FROM students
GROUP BY grade;
```

By understanding these basic concepts and examples, you'll be well on your way to using SQLite effectively. Happy learning!