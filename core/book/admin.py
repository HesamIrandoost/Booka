from django.contrib import admin

from .models import Author, Book, Genre, Review, Collection


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "slug",
        "first_name",
        "last_name",
        "date_born",
        "place_born",
    )

    search_fields = (
        "first_name",
        "last_name",
        "biography",
    )

    list_filter = ("date_born",)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name",)

    search_fields = (
        "name",
        "description",
    )


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "slug",
        "star",
        "pages",
        "published_date",
        "created_at",
    )

    search_fields = (
        "title",
        "about",
        "summary",
        "author__first_name",
        "author__last_name",
    )

    list_filter = (
        "published_date",
        "genres",
    )

    filter_horizontal = ("genres",)

    readonly_fields = (
        "star",
        "created_at",
    )


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "subject",
        "user",
        "book",
        "star",
        "likes",
        "status",
        "created_at",
    )

    search_fields = (
        "subject",
        "text",
        "user__username",
        "book__title",
    )

    list_filter = (
        "star",
        "status",
        "created_at",
    )

    readonly_fields = ("created_at",)


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "title",
        "user",
        "created_at",
        "is_public",
    )

    search_fields = (
        "title",
        "description",
        "is_public",
        "user__username",
        "books__title",
    )

    filter_horizontal = ("books",)

    readonly_fields = ("created_at",)
