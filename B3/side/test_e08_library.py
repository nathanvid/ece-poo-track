"""Step 08, on the side: tests of the rules of e08_library.py.

    uv run pytest B3/side -v

A test is a function whose name starts with test_. It builds a situation,
acts, and checks with assert. pytest finds and runs them all.
"""

import pytest
from e08_library import Book, Library


# A fixture: a fresh library for every test that asks for it by name.
@pytest.fixture
def library() -> Library:
    library = Library("Test library")
    library.add(Book("Emma", "Jane Austen"))
    library.add(Book("Dune", "Frank Herbert"))
    library.add(Book("Persuasion", "Jane Austen"))
    return library


def test_catalogue_is_sorted_by_author_then_title(library):
    titles = [book.title for book in library.catalogue()]
    assert titles == ["Dune", "Emma", "Persuasion"]


def test_borrow(library):
    library.borrow("Emma", "lou")
    assert library.get("Emma").borrowed_by == "lou"


# A rule is tested by breaking it: pytest.raises checks that the error comes.
def test_a_book_cannot_be_borrowed_twice(library):
    library.borrow("Emma", "lou")
    with pytest.raises(ValueError, match="already borrowed"):
        library.borrow("Emma", "yanis")


def test_two_books_per_reader(library):
    library.borrow("Emma", "lou")
    library.borrow("Dune", "lou")
    with pytest.raises(ValueError):
        library.borrow("Persuasion", "lou")
    assert library.get("Persuasion").borrowed_by == ""  # nothing changed
