"""Step 08, on the side: one object holds the collection and its rules.

uv run python B3/side/e08_library.py
uv run pytest B3/side            runs test_e08_library.py
"""

from dataclasses import dataclass


@dataclass
class Book:
    title: str
    author: str
    borrowed_by: str = ""

    def __lt__(self, other: "Book") -> bool:
        """sorted() and min() use <: here, by author then title."""
        return (self.author, self.title) < (other.author, other.title)

    def __str__(self) -> str:
        """What print() shows."""
        if self.borrowed_by:
            return f"{self.title} ({self.author}), borrowed by {self.borrowed_by}"
        return f"{self.title} ({self.author})"


class Library:
    """Every change goes through a method, so every rule is checked."""

    MAX_BOOKS_PER_READER = 2

    def __init__(self, name: str) -> None:
        self.name = name
        self.books: dict[str, Book] = {}  # by title: found in one step

    def add(self, book: Book) -> None:
        if book.title in self.books:
            raise ValueError(f"{book.title} is already in {self.name}.")
        self.books[book.title] = book

    def get(self, title: str) -> Book:
        if title not in self.books:
            raise ValueError(f"No book {title!r}.")
        return self.books[title]

    def books_of(self, reader: str) -> list[Book]:
        result = []
        for book in self.books.values():
            if book.borrowed_by == reader:
                result.append(book)
        return result

    def borrow(self, title: str, reader: str) -> None:
        book = self.get(title)
        if book.borrowed_by:
            raise ValueError(f"{title} is already borrowed.")
        if len(self.books_of(reader)) >= self.MAX_BOOKS_PER_READER:
            raise ValueError(f"{reader} already has {self.MAX_BOOKS_PER_READER}.")
        book.borrowed_by = reader

    def catalogue(self) -> list[Book]:
        return sorted(self.books.values())


if __name__ == "__main__":
    library = Library("Town library")
    library.add(Book("Persuasion", "Jane Austen"))
    library.add(Book("Dune", "Frank Herbert"))
    library.add(Book("Emma", "Jane Austen"))
    library.borrow("Emma", "lou")
    for book in library.catalogue():
        print(book)
    try:
        library.borrow("Emma", "yanis")
    except ValueError as error:
        print(f"Refused: {error}")
