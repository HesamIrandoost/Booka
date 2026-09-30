import pytest
from datetime import date
from book.models import Genre, Book, Author, Review
from account.models import User
from .factories import UserFactory


@pytest.mark.django_db
class TestModelBook:
    def test_book_creation(self, author, genre, book):

        book.genres.add(genre)

        assert book.pk is not None
        assert book.title == "The Hobbit"
        assert book.author == author
        assert genre in book.genres.all()

    def test_book_update_star(self, book):
        user1 = UserFactory()
        user2 = UserFactory()
        user3 = UserFactory()

        Review.objects.create(
            user=user1,
            book=book,
            subject="Great",
            text="Amazing book",
            star=5,
        )

        Review.objects.create(
            user=user2,
            book=book,
            subject="Good",
            text="Very good",
            star=4,
        )

        Review.objects.create(
            user=user3,
            book=book,
            subject="Okay",
            text="It was okay",
            star=3,
        )

        book.update_star()
        book.refresh_from_db()

        assert book.star == 4


@pytest.mark.django_db
class TestModelAuthor:
    def test_author_full_name(self, author):

        assert author.full_name == "J.R.R. Tolkien"


@pytest.mark.django_db
class TestModelGenre:

    def test_genre_creation(self, genre):

        assert genre.pk is not None
        assert genre.name == "fantasy"
        assert genre.slug == "fantasy"
        # assert genre.slug == 'Fantasy'
        # assert genre.slug == 'fantasy-'

    def test_genre_str(self, genre):

        assert str(genre) == "fantasy"
