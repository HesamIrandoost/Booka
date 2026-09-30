import factory
from account.models import User
from book.models import Review, Book, Genre, Author, Collection, ReviewLike


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("user_name")
    password = "qwe123QWE@"
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")


class AuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Author

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    biography = factory.Faker("paragraph")


class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Book

    author = factory.SubFactory(AuthorFactory)
    title = factory.Faker("sentence")
    about = factory.Faker("sentence")
    summary = factory.Faker("paragraph")


class ReviewFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Review

    user = factory.SubFactory(UserFactory)
    book = factory.SubFactory(BookFactory)

    rating = factory.Faker("random_int", min=1, max=5)

    text = factory.Faker("paragraph")
