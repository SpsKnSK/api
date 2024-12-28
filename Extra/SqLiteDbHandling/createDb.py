from sqlite3 import Connection, Cursor, connect


class Database:
    def __init__(self, db_name: str = "book_store"):
        self.db_name: str = db_name

    def create_tables(self):
        conn: Connection = connect(self.db_name)
        cursor: Cursor = conn.cursor()
        cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS authors (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        )
        """
        )
        cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS publishers (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        )
        """
        )
        cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            author_id INTEGER,
            publisher_id INTEGER,
            FOREIGN KEY (author_id) REFERENCES authors (id),
            FOREIGN KEY (publisher_id) REFERENCES publishers (id)
        )
        """
        )
        conn.commit()
        conn.close()
