import random

from faker import Faker

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from book.models import Author, Book, Genre, Review, Collection

fake = Faker()


class Command(BaseCommand):
    help = "Seed BookIMDb with realistic book data"

    def handle(self, *args, **kwargs):
        User = get_user_model()

        # ==========================================================
        # Clear old data
        # ==========================================================

        Review.objects.all().delete()
        Collection.objects.all().delete()
        Book.objects.all().delete()
        Author.objects.all().delete()
        Genre.objects.all().delete()
        User.objects.exclude(is_superuser=True).delete()

        # ==========================================================
        # Users
        # ==========================================================

        users = []

        for _ in range(20):
            user = User.objects.create_user(
                username=fake.unique.user_name(),
                password="Test12345",
                first_name=fake.first_name(),
                last_name=fake.last_name(),
            )

            users.append(user)

        self.stdout.write(self.style.SUCCESS("20 users created."))

        # ==========================================================
        # Genres
        # ==========================================================

        genre_data = [
            ("Fantasy", "Fantasy and magical stories."),
            ("Science Fiction", "Stories about science, technology and the future."),
            ("Mystery", "Stories centered around solving mysterious events."),
            ("Thriller", "Suspenseful and exciting stories."),
            ("Romance", "Stories focused on romantic relationships."),
            ("Historical Fiction", "Fictional stories set in historical periods."),
            ("Horror", "Stories designed to create fear and suspense."),
            ("Adventure", "Stories involving exploration and exciting journeys."),
            ("Classic", "Important and influential works of literature."),
            ("Dystopian", "Stories about oppressive or imagined future societies."),
            ("Philosophy", "Books dealing with philosophical questions and ideas."),
            (
                "Young Adult",
                "Literature primarily written for teenage and young adult readers.",
            ),
        ]

        genres = {}

        for name, description in genre_data:
            genre = Genre.objects.create(
                name=name,
                description=description,
            )

            genres[name] = genre

        self.stdout.write(self.style.SUCCESS("Genres created."))

        # ==========================================================
        # Authors + Books
        # ==========================================================

        books_data = [
            {
                "author": {
                    "first_name": "George",
                    "last_name": "Orwell",
                    "date_born": "1903-06-25",
                    "place_born": "Motihari, India",
                },
                "title": "1984",
                "publisher": "Secker & Warburg",
                "published_date": "1949-06-08",
                "pages": 328,
                "genres": ["Dystopian", "Classic"],
            },
            {
                "author": {
                    "first_name": "J.R.R.",
                    "last_name": "Tolkien",
                    "date_born": "1892-01-03",
                    "place_born": "Bloemfontein, South Africa",
                },
                "title": "The Hobbit",
                "publisher": "George Allen & Unwin",
                "published_date": "1937-09-21",
                "pages": 310,
                "genres": [
                    "Fantasy",
                    "Adventure",
                    "Classic",
                ],
            },
            {
                "author": {
                    "first_name": "Frank",
                    "last_name": "Herbert",
                    "date_born": "1920-10-08",
                    "place_born": "Tacoma, Washington, USA",
                },
                "title": "Dune",
                "publisher": "Chilton Company",
                "published_date": "1965-08-01",
                "pages": 412,
                "genres": [
                    "Science Fiction",
                    "Adventure",
                    "Classic",
                ],
            },
            {
                "author": {
                    "first_name": "F. Scott",
                    "last_name": "Fitzgerald",
                    "date_born": "1896-09-24",
                    "place_born": "St. Paul, Minnesota, USA",
                },
                "title": "The Great Gatsby",
                "publisher": "Charles Scribner's Sons",
                "published_date": "1925-04-10",
                "pages": 180,
                "genres": [
                    "Classic",
                    "Romance",
                ],
            },
            {
                "author": {
                    "first_name": "Jane",
                    "last_name": "Austen",
                    "date_born": "1775-12-16",
                    "place_born": "Steventon, Hampshire, England",
                },
                "title": "Pride and Prejudice",
                "publisher": "T. Egerton",
                "published_date": "1813-01-28",
                "pages": 432,
                "genres": [
                    "Romance",
                    "Classic",
                ],
            },
            {
                "author": {
                    "first_name": "J.K.",
                    "last_name": "Rowling",
                    "date_born": "1965-07-31",
                    "place_born": "Yate, Gloucestershire, England",
                },
                "title": "Harry Potter and the Philosopher's Stone",
                "publisher": "Bloomsbury",
                "published_date": "1997-06-26",
                "pages": 223,
                "genres": [
                    "Fantasy",
                    "Adventure",
                    "Young Adult",
                ],
            },
            {
                "author": {
                    "first_name": "Harper",
                    "last_name": "Lee",
                    "date_born": "1926-04-28",
                    "place_born": "Monroeville, Alabama, USA",
                },
                "title": "To Kill a Mockingbird",
                "publisher": "J.B. Lippincott & Co.",
                "published_date": "1960-07-11",
                "pages": 281,
                "genres": [
                    "Classic",
                    "Historical Fiction",
                ],
            },
            {
                "author": {
                    "first_name": "Leo",
                    "last_name": "Tolstoy",
                    "date_born": "1828-09-09",
                    "place_born": "Yasnaya Polyana, Russia",
                },
                "title": "War and Peace",
                "publisher": "The Russian Messenger",
                "published_date": "1869-01-01",
                "pages": 1225,
                "genres": [
                    "Classic",
                    "Historical Fiction",
                    "Romance",
                ],
            },
            {
                "author": {
                    "first_name": "Fyodor",
                    "last_name": "Dostoevsky",
                    "date_born": "1821-11-11",
                    "place_born": "Moscow, Russia",
                },
                "title": "Crime and Punishment",
                "publisher": "The Russian Messenger",
                "published_date": "1866-01-01",
                "pages": 671,
                "genres": [
                    "Classic",
                    "Philosophy",
                    "Mystery",
                ],
            },
            {
                "author": {
                    "first_name": "Aldous",
                    "last_name": "Huxley",
                    "date_born": "1894-07-26",
                    "place_born": "Godalming, Surrey, England",
                },
                "title": "Brave New World",
                "publisher": "Chatto & Windus",
                "published_date": "1932-01-01",
                "pages": 311,
                "genres": [
                    "Dystopian",
                    "Science Fiction",
                    "Classic",
                ],
            },
            {
                "author": {
                    "first_name": "Mary",
                    "last_name": "Shelley",
                    "date_born": "1797-08-30",
                    "place_born": "London, England",
                },
                "title": "Frankenstein",
                "publisher": "Lackington, Hughes, Harding, Mavor & Jones",
                "published_date": "1818-01-01",
                "pages": 280,
                "genres": [
                    "Horror",
                    "Science Fiction",
                    "Classic",
                ],
            },
            {
                "author": {
                    "first_name": "Bram",
                    "last_name": "Stoker",
                    "date_born": "1847-11-08",
                    "place_born": "Clontarf, Dublin, Ireland",
                },
                "title": "Dracula",
                "publisher": "Archibald Constable and Company",
                "published_date": "1897-05-26",
                "pages": 418,
                "genres": [
                    "Horror",
                    "Classic",
                    "Mystery",
                ],
            },
            {
                "author": {
                    "first_name": "Gabriel",
                    "last_name": "García Márquez",
                    "date_born": "1927-03-06",
                    "place_born": "Aracataca, Colombia",
                },
                "title": "One Hundred Years of Solitude",
                "publisher": "Harper & Row",
                "published_date": "1967-05-30",
                "pages": 417,
                "genres": [
                    "Classic",
                    "Historical Fiction",
                ],
            },
            {
                "author": {
                    "first_name": "Paulo",
                    "last_name": "Coelho",
                    "date_born": "1947-08-24",
                    "place_born": "Rio de Janeiro, Brazil",
                },
                "title": "The Alchemist",
                "publisher": "HarperCollins",
                "published_date": "1988-01-01",
                "pages": 208,
                "genres": [
                    "Adventure",
                    "Philosophy",
                ],
            },
            {
                "author": {
                    "first_name": "Hermann",
                    "last_name": "Hesse",
                    "date_born": "1877-07-02",
                    "place_born": "Calw, Germany",
                },
                "title": "Siddhartha",
                "publisher": "S. Fischer Verlag",
                "published_date": "1922-01-01",
                "pages": 152,
                "genres": [
                    "Philosophy",
                    "Classic",
                ],
            },
        ]

        authors = []
        books = []

        for data in books_data:

            author_data = data["author"]

            author, _ = Author.objects.get_or_create(
                first_name=author_data["first_name"],
                last_name=author_data["last_name"],
                defaults={
                    "biography": fake.paragraph(nb_sentences=10),
                    "date_born": author_data["date_born"],
                    "place_born": author_data["place_born"],
                    "website": f"https://{fake.domain_name()}",
                },
            )

            authors.append(author)

            book = Book.objects.create(
                author=author,
                title=data["title"],
                about=fake.paragraph(nb_sentences=5),
                summary=fake.paragraph(nb_sentences=8),
                pages=data["pages"],
                publisher=data["publisher"],
                published_date=data["published_date"],
            )

            book.genres.set(genres[genre] for genre in data["genres"])

            books.append(book)

        self.stdout.write(
            self.style.SUCCESS(
                f"{len(authors)} authors and " f"{len(books)} books created."
            )
        )

        # ==========================================================
        # Reviews
        # ==========================================================

        review_subjects = [
            "Absolutely loved it",
            "A memorable reading experience",
            "One of my favorite books",
            "Really interesting",
            "Worth reading",
            "A powerful story",
            "Beautifully written",
            "Not what I expected",
            "A fascinating book",
            "Highly recommended",
        ]

        review_texts = [
            "The story was engaging from beginning to end.",
            "I really enjoyed the characters and the writing style.",
            "This book gave me a lot to think about.",
            "The world building was impressive and memorable.",
            "Some parts were slow, but overall I enjoyed the experience.",
            "The themes of this book are still relevant today.",
            "I would definitely recommend this book to other readers.",
            "The characters felt surprisingly realistic.",
        ]

        reviews = []

        # 150 root reviews

        for _ in range(150):

            user = random.choice(users)
            book = random.choice(books)

            review = Review.objects.create(
                user=user,
                book=book,
                subject=random.choice(review_subjects),
                text=random.choice(review_texts),
                likes=random.randint(0, 100),
                star=random.randint(1, 5),
                status=True,
            )

            reviews.append(review)

        # ==========================================================
        # Replies
        # ==========================================================

        reply_texts = [
            "I completely agree with you.",
            "I had a similar experience.",
            "Interesting point!",
            "I actually felt the opposite.",
            "This is exactly what I thought.",
            "Thanks for sharing your opinion.",
            "I might give this book another try.",
            "The ending was my favorite part too.",
        ]

        replies = []

        for review in random.sample(reviews, k=int(len(reviews) * 0.3)):

            reply = Review.objects.create(
                user=random.choice(users),
                book=review.book,
                subject="Reply",
                text=random.choice(reply_texts),
                likes=random.randint(0, 30),
                parent=review,
                star=0,
                status=True,
            )

            replies.append(reply)

        self.stdout.write(
            self.style.SUCCESS(
                f"{len(reviews)} reviews and " f"{len(replies)} replies created."
            )
        )

        # ==========================================================
        # Update Book ratings
        # ==========================================================

        for book in books:
            book.update_star()

        self.stdout.write(self.style.SUCCESS("Book ratings calculated."))

        # ==========================================================
        # Collections
        # ==========================================================

        collection_names = [
            "My Favorite Books",
            "Books I Want to Read",
            "Best Classics",
            "My Favorite Fantasy Books",
            "Books Everyone Should Read",
            "My Weekend Reading",
            "Books That Changed My Perspective",
            "My All-Time Favorites",
        ]

        collections = []

        for user in users:

            for _ in range(random.randint(1, 3)):

                collection = Collection.objects.create(
                    user=user,
                    title=random.choice(collection_names),
                    description=fake.paragraph(nb_sentences=3),
                    is_public=random.choice([True, True, True, False]),
                )

                collection.books.set(
                    random.sample(books, random.randint(3, min(8, len(books))))
                )

                collections.append(collection)

        self.stdout.write(
            self.style.SUCCESS(f"{len(collections)} collections created.")
        )

        # ==========================================================
        # Done
        # ==========================================================

        self.stdout.write(
            self.style.SUCCESS("\nBookIMDb database seeded successfully!")
        )
