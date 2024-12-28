from sqlite3 import Connection, Cursor, connect


class Database:
    def __init__(self, db_name: str = "book_store"):
        self.db_name: str = db_name
        self.conn: Connection = connect(self.db_name)
        self.cursor: Cursor = self.conn.cursor()

    def create_tables(self):

        self.cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS authors (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        )
        """
        )
        self.cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS publishers (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        )
        """
        )
        self.cursor.execute(
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
        self.conn.commit()

    def close(self) -> None:
        self.conn.close()
