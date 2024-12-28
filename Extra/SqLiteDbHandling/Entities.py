from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Entity:
    id: Optional[int] = field(default=None)


# Define dataclasses
@dataclass
class Author(Entity):
    name: str = field(default="")


@dataclass
class Publisher(Entity):
    name: str = field(default="")


@dataclass
class Book(Entity):
    title: str = field(default="")
    author_id: int = field(default=0)
    publisher_id: int = field(default=0)
    author: Author = field(default=None)
    publisher: Publisher = field(default=None)
