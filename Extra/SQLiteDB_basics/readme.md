# SQLite

**SQLite** is a popular database management system that is easy to use and perfect for learning about databases. In this article, we'll cover the basics of **SQLite**, including what a database is, how to handle the DB Browser, what tables are, and some key concepts like primary keys, foreign keys, data types, and SQL queries.

## What is a Database?

A database (DB) is a collection of organized data that can be easily accessed, managed, and updated. Think of it as a digital filing system where you can store and retrieve information efficiently.

## How to Handle the DB Browser

DB Browser for **SQLite** is a graphical tool that allows you to create, design, and edit **SQLite** databases. Here's how to get started:

1. **Download and Install**: [Download](https://**SQLite**browser.org/dl/) and install DB Browser for **SQLite** from its official website.
2. **Create a New Database**: Open the DB Browser and click on *"New Database"* to create a new database file.
3. **Create Tables**: 
   1. Use the *"Create Table"* option to define the structure of your tables.
   2. Go to the *"Execute SQL"* tab and create the tables via commands

## What is a Table?

A table is a collection of related data organized in rows and columns. Each row represents a record, and each column represents a field within the record. For example, a table called `students` might have columns like `id`, `name`, and `sex`.

## What are Primary Keys (PK) and Foreign Keys (FK)?

- **Primary Key (PK)**: A primary key is a unique identifier for each record in a table. It ensures that each record can be uniquely identified. For example, the `id` column in the `students` table can be a primary key.
- **Foreign Key (FK)**: A foreign key is a column that creates a relationship between two tables. It references the primary key of another table. For example, if you have a `grades` table, the `student_id` column can be a foreign key that references the `id` column in the `students` table. With this relationship you can keep the data integrity: you cannot insert any other value to the `grades` table's `student_id`, only the ones that **exist** in the `student` table!

## What Data Types Can Be Used?

**SQLite** supports several data types, including:

- **INTEGER**: Whole numbers
- **REAL**: Floating-point numbers
- **TEXT**: Text strings
- **BLOB**: Binary data

## Prepare the demo database
In this demo we will be using a school DB. There are students, that have more grades. Each grade is connected to one lesson. We can write it as 
```mermaid
erDiagram
    STUDENTS {
        INTEGER id
        TEXT name
        TEXT sex
    }
    LESSONS {
        INTEGER id
        TEXT name
    }
    GRADES {
        INTEGER id
        INTEGER student_id
        INTEGER lesson_id
        INTEGER grade
    }
    STUDENTS ||--o{ GRADES : "has"
    LESSONS ||--o{ GRADES : "has"
```

### Creating Tables

```sql
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    sex text
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

### Inserting Data

```sql
-- Insert data into students table
INSERT INTO students (name, sex) VALUES 
('Alice', 'Female'),
('Bob', 'Male'),
('Charlie', 'Male'),
('Diana', 'Female'),
('Eve', 'Female'),
('Frank', 'Male'),
('Grace', 'Female'),
('Hannah', 'Female'),
('Ian', 'Male'),
('Jack', 'Male'),
('Karen', 'Female'),
('Liam', 'Male'),
('Melany', 'Female'),
('Nancy', 'Female');
-- Insert data into lessons table
INSERT INTO lessons (name) VALUES 
('Math'),
('Physics'),
('PE'),
('Drawing'),
('History');

-- Insert data into grades table
INSERT INTO grades (student_id, lesson_id, grade) VALUES 
(1, 1, 85),
(1, 2, 90),
(1, 3, 78),
(1, 4, 82),
(1, 5, 88),
(2, 1, 91),
(2, 2, 76),
(2, 3, 79),
(2, 4, 85),
(2, 5, 87),
(3, 1, 92),
(3, 2, 89),
(3, 3, 80),
(3, 4, 83),
(3, 5, 90),
(4, 1, 94),
(4, 2, 88),
(4, 3, 82),
(4, 4, 86),
(4, 5, 89),
(5, 1, 93),
(5, 2, 87),
(5, 3, 81),
(5, 4, 84),
(5, 5, 88),
(6, 1, 90),
(6, 2, 85),
(6, 3, 78),
(6, 4, 82),
(6, 5, 87),
(7, 1, 88),
(7, 2, 83),
(7, 3, 76),
(7, 4, 80),
(7, 5, 85),
(8, 1, 91),
(8, 2, 86),
(8, 3, 79),
(8, 4, 83),
(8, 5, 88),
(9, 1, 89),
(9, 2, 84),
(9, 3, 77),
(9, 4, 81),
(9, 5, 86),
(10, 1, 92),
(10, 2, 87),
(10, 3, 80),
(10, 4, 84),
(10, 5, 89),
(11, 1, 90),
(11, 2, 85),
(11, 3, 78),
(11, 4, 82),
(11, 5, 87),
(12, 1, 88),
(12, 2, 83),
(12, 3, 76),
(12, 4, 80),
(12, 5, 85),
(13, 5, 85);
```

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
### Joining Tables

```sql
SELECT 
	s.name, 
	l.name AS lesson, 
	g.grade
FROM students s 
JOIN grades g ON s.id = g.student_id
JOIN lessons l ON g.lesson_id = l.id;
```
#### `LEFT JOIN`
`A LEFT JOIN` is a type of SQL join that returns **all** records from the *left* table (the first table in the join), and the **matched** records from the *right* table (the second table in the join). If there is **no match**, the result is **NULL** on the side of the *right* table.

In our example Melany has only grade and Nancy has no grades.
```sql
SELECT DISTINCT
	s.name
FROM students s 
JOIN grades g ON s.id = g.student_id
JOIN lessons l ON g.lesson_id = l.id;
```
returns:
```
name	numberOfLessons
Alice	5
Bob	    5
...
Liam	5
Melany	1
```
To see, how many grades/lessons Nancy has, we have to use the `LEFT JOIN` (for both of the tables grades and lessons, to maintain **all** values from the *left* table)
```sql
SELECT DISTINCT
	s.name,
	COUNT(l.id) numberOfLessons
FROM students s 
LEFT JOIN grades g ON s.id = g.student_id
LEFT JOIN lessons l ON g.lesson_id = l.id
GROUP BY
	s.name;
```
returns:
```
name	numberOfLessons
Alice	5
Bob	    5
...
Liam	5
Melany	1
Nancy	0
```

## What is `WHERE`?

The `WHERE` clause is used to **filter** records based on a condition. For example, to get students with a grade higher than 80, you can use:

```sql
SELECT * FROM students
WHERE grade > 80;
```
### Using WHERE

```sql
SELECT 
	s.name, 
	l.name AS lesson, 
	g.grade
FROM students s 
JOIN grades g ON s.id = g.student_id
JOIN lessons l ON g.lesson_id = l.id
WHERE 
	1=1
	AND g.grade > 90
```

## What is `GROUP BY`?

The `GROUP BY` clause is used to **group** rows that have the same values in specified columns. For example, to count the number of students in each sex group, you can use:

```sql
SELECT 
	s.sex,
	COUNT(s.sex) countOfStudents
FROM students s 
GROUP BY
	s.sex
```
### Using GROUP BY
#### Number of lessons per student
```sql
SELECT 
	s.name,
	COUNT(l.id) numberOfLessons
FROM students s 
JOIN grades g ON s.id = g.student_id
JOIN lessons l ON g.lesson_id = l.id
GROUP BY
	s.name
```

#### Counting average grade
```sql
SELECT 
	s.name, 
	SUM(g.grade)/COUNT(g.grade) averageGrade
FROM students s 
JOIN grades g ON s.id = g.student_id
GROUP BY 
	s.name;
```
#### Average of grade sorted by the top ranked lesson
```sql
SELECT 
	l.name,
	SUM(g.grade)/COUNT(l.name) averageOfGrade
FROM students s 
JOIN grades g ON s.id = g.student_id
JOIN lessons l ON g.lesson_id = l.id
GROUP BY
	l.name
ORDER BY
	averageOfGrade DESC
```
## Delete data
this command deletes **all the data** from the specified tables.
```sql
DELETE FROM grades;
DELETE FROM students;
DELETE FROM lessons;
```
## Remove tables
This command will delete the **whole table**, then you need to recreate the tables using the `CREATE TABLE ...` commands
```sql
DROP TABLE grades;
DROP TABLE students; 
DROP TABLE lessons;
```
