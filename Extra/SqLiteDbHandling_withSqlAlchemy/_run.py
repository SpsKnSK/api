# pip install sqlalchemy

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Define the database engine
# engine = create_engine("sqlite:///library.db", echo=True)
engine = create_engine(
    "sqlite:///library.db", echo=False
)  # True will display all the sql commands

# Define the base class for declarative models
Base = declarative_base()


# Define the Author model
class Author(Base):
    __tablename__ = "authors"
    author_id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)


# Define the Publisher model
class Publisher(Base):
    __tablename__ = "publishers"
    publisher_id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)


# Define the Book model
class Book(Base):
    __tablename__ = "books"
    book_id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey("authors.author_id"))
    publisher_id = Column(Integer, ForeignKey("publishers.publisher_id"))
    author = relationship("Author")
    publisher = relationship("Publisher")


# Create the tables in the database
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Example usage
# Create records
author = Author(name="J.K. Rowling")
publisher = Publisher(name="Bloomsbury")
book = Book(
    title="Harry Potter and the Philosopher's Stone", author=author, publisher=publisher
)

# Add records to the session and commit
session.add(author)
session.add(publisher)
session.add(book)
session.commit()

# Query records
books = session.query(Book).all()
print("Books:")
for book in books:
    print(
        f"Title: {book.title}, Author: {book.author.name}, Publisher: {book.publisher.name}"
    )

# Update records
book_to_update = (
    session.query(Book)
    .filter_by(title="Harry Potter and the Philosopher's Stone")
    .first()
)
if book_to_update:
    book_to_update.title = "Harry Potter and the Sorcerer's Stone"
    session.commit()

# Query updated records
updated_books = session.query(Book).all()
print("Updated Books:")
for book in updated_books:
    print(
        f"Title: {book.title}, Author: {book.author.name}, Publisher: {book.publisher.name}"
    )

# Delete records
book_to_delete = (
    session.query(Book).filter_by(title="Harry Potter and the Sorcerer's Stone").first()
)
if book_to_delete:
    session.delete(book_to_delete)
    session.commit()

# Query records after deletion
remaining_books = session.query(Book).all()
print("Remaining Books:")
for book in remaining_books:
    print(
        f"Title: {book.title}, Author: {book.author.name}, Publisher: {book.publisher.name}"
    )
