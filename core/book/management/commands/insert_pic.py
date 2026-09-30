import random
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand

from book.models import Author, Book


class Command(BaseCommand):
    help = "Assign random author and book images from media directory"

    def handle(self, *args, **kwargs):

        # ==========================================================
        # Paths
        # ==========================================================

        authors_dir = Path(settings.MEDIA_ROOT) / "authors"
        books_dir = Path(settings.MEDIA_ROOT) / "books"

        # ==========================================================
        # Supported image extensions
        # ==========================================================

        image_extensions = {
            ".jpg",
            ".jpeg",
            ".png",
            ".webp",
        }

        # ==========================================================
        # Get images
        # ==========================================================

        author_images = [
            path
            for path in authors_dir.iterdir()
            if path.is_file() and path.suffix.lower() in image_extensions
        ]

        book_images = [
            path
            for path in books_dir.iterdir()
            if path.is_file() and path.suffix.lower() in image_extensions
        ]

        # ==========================================================
        # Validate images
        # ==========================================================

        if not author_images:
            self.stdout.write(
                self.style.ERROR(f"No author images found in: {authors_dir}")
            )
            return

        if not book_images:
            self.stdout.write(self.style.ERROR(f"No book images found in: {books_dir}"))
            return

        # ==========================================================
        # Authors
        # ==========================================================

        authors = Author.objects.all()

        for author in authors:

            image = random.choice(author_images)

            # ImageField stores path relative to MEDIA_ROOT
            author.profile = f"authors/{image.name}"

            author.save(update_fields=["profile"])

        self.stdout.write(
            self.style.SUCCESS(f"{authors.count()} author images assigned.")
        )

        # ==========================================================
        # Books
        # ==========================================================

        books = Book.objects.all()

        for book in books:

            image = random.choice(book_images)

            # ImageField stores path relative to MEDIA_ROOT
            book.cover = f"books/{image.name}"

            book.save(update_fields=["cover"])

        self.stdout.write(self.style.SUCCESS(f"{books.count()} book covers assigned."))

        # ==========================================================
        # Done
        # ==========================================================

        self.stdout.write(self.style.SUCCESS("\nImages inserted successfully!"))
