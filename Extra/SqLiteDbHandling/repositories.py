from Entities import Author, Book, Publisher
from typing import List
from database import Database


class Repository:
    def __init__(self, db: Database):
        self.db = db


class PublisherRepository(Repository):
    def create(self, publisher: Publisher):
        self.db.cursor.execute(
            "INSERT INTO publishers (name) VALUES (?)", (publisher.name,)
        )
        self.db.conn.commit()
        publisher.id = self.db.cursor.lastrowid

    def read(self) -> List[Publisher]:
        self.db.cursor.execute("SELECT * FROM publishers")
        rows = self.db.cursor.fetchall()
        return [Publisher(id=row, name=row) for row in rows]

    def update(self, publisher: Publisher):
        self.db.cursor.execute(
            "UPDATE publishers SET name = ? WHERE id = ?",
            (publisher.name, publisher.id),
        )
        self.db.conn.commit()

    def delete(self, id: int):
        self.db.cursor.execute("DELETE FROM publishers WHERE id = ?", (id,))
        self.db.conn.commit()


class AuthorRepository(Repository):
    def create(self, author: Author):
        self.db.cursor.execute("INSERT INTO authors (name) VALUES (?)", (author.name,))
        self.db.conn.commit()
        author.id = self.db.cursor.lastrowid

    def read(self) -> List[Author]:
        self.db.cursor.execute("SELECT * FROM authors")
        rows = self.db.cursor.fetchall()
        return [Author(id=row, name=row) for row in rows]

    def update(self, author: Author):
        self.db.cursor.execute(
            "UPDATE authors SET name = ? WHERE id = ?",
            (author.name, author.id),
        )
        self.db.conn.commit()

    def delete(self, id: int):
        self.db.cursor.execute("DELETE FROM authors WHERE id = ?", (id,))
        self.db.conn.commit()


class BookRepository(Repository):
    def create(self, book: Book):
        self.db.cursor.execute(
            "INSERT INTO books (title, author_id, publisher_id) VALUES (?, ?, ?)",
            (book.title, book.author_id, book.publisher_id),
        )
        self.db.conn.commit()
        book.id = self.db.cursor.lastrowid

    def read(self) -> List[Book]:
        self.db.cursor.execute("SELECT * FROM books")
        rows = self.db.cursor.fetchall()
        return [
            Book(id=row, title=row, author_id=row, publisher_id=row) for row in rows
        ]

    def update(self, book: Book):
        self.db.cursor.execute(
            "UPDATE books SET title = ?, author_id = ?, publisher_id = ? WHERE id = ?",
            (book.title, book.author_id, book.publisher_id, book.id),
        )
        self.db.conn.commit()

    def delete(self, id: int):
        self.db.cursor.execute("DELETE FROM books WHERE id = ?", (id,))
        self.db.conn.commit()
