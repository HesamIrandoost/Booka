from rest_framework import serializers

from account.models import User
from book.models import Author, Book, Collection, Genre, Review


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "avatar",
        ]


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["pk", "name", "description", "slug"]


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = [
            "pk",
            "slug",
            "first_name",
            "last_name",
            "profile",
            "biography",
            "website",
            "date_born",
            "place_born",
        ]


class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Review
        fields = [
            "id",
            "user",
            "book",
            "subject",
            "text",
            "likes",
            "parent",
            "star",
            "status",
            "created_at",
        ]
        read_only_fields = [
            "id",
            "user",
            "book",
            "likes",
            "parent",
            "status",
            "created_at",
        ]


class AllBooksSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    genres = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = [
            "id",
            "author",
            "slug",
            "title",
            "about",
            "summary",
            "cover",
            "pages",
            "genres",
            "star",
            "publisher",
            "published_date",
            "created_at",
        ]


class DetailBooksSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    genres = GenreSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = [
            "id",
            "author",
            "slug",
            "title",
            "about",
            "summary",
            "cover",
            "pages",
            "genres",
            "star",
            "reviews",
            "publisher",
            "published_date",
            "created_at",
        ]


class CollectionSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    books = AllBooksSerializer(many=True, read_only=True)

    class Meta:
        model = Collection
        fields = [
            "pk",
            "user",
            "books",
            "title",
            "cover",
            "description",
            "is_public",
            "created_at",
        ]
        read_only_fields = [
            "id",
            "user",
            "books",
            "created_at",
        ]
