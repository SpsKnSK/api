from database import Database
from Entities import *
from repositories import *

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

print("Authors:", author_repo.read())
print("Publishers:", publisher_repo.read())
print("Books:", book_repo.read())
