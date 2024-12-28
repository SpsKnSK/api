from database import Database
from Entities import *
from repositories import *


def PrintBooks(books: [Book]) -> None:
    for book in books:
        print(
            f"Title: {book.title}, Author: {book.author.name}, Publisher: {book.publisher.name}"
        )


db: Database = Database()
db.create_tables()

author_repo = AuthorRepository(db)
publisher_repo = PublisherRepository(db)
book_repo = BookRepository(db)

author = Author(name="J.K. Rowling")
author_repo.create(author)

publisher = Publisher(name="Bloomsbury")
publisher_repo.create(publisher)

book = Book(
    title="Harry Potter and the Philosopher's Stone",
    author_id=author.id,
    publisher_id=publisher.id,
)
book_repo.create(book)

print("Books with Authors and Publishers:")
PrintBooks(book_repo.read())

author = author_repo.read()[0]
publisher = publisher_repo.read()[0]
book = book_repo.read()[0]

# Update records
author.name = "Joanne Rowling"
author_repo.update(author)

publisher.name = "Bloomsbury Publishing"
publisher_repo.update(publisher)

book.title = "Harry Potter and the Sorcerer's Stone"
book_repo.update(book)

print("\nUpdated Books with Authors and Publishers:")
PrintBooks(book_repo.read())

book_repo.delete(book.id)
author_repo.delete(author.id)
publisher_repo.delete(publisher.id)

print("\nAfter Deletion - Books with Authors and Publishers:")
PrintBooks(book_repo.read())

db.close()
