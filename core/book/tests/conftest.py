import pytest
from book.models import Author, Genre, Book
from datetime import date


@pytest.fixture
def author(db):
    return Author.objects.create(
        first_name="J.R.R.",
        last_name="Tolkien",
        biography="English writer",
        date_born=date(1892, 1, 3),
        place_born="South Africa",
    )


@pytest.fixture
def genre(db):
    return Genre.objects.create(
        name="fantasy",
        slug="fantasy",
    )


@pytest.fixture
def book(db, author):
    return Book.objects.create(
        author=author,
        title="The Hobbit",
        about="About the book",
        summary="A fantasy novel",
        pages=310,
        star=4.5,
        publisher="Allen & Unwin",
        published_date=date(1937, 9, 21),
        cover="books/covers/hobbit.jpg",
    )
