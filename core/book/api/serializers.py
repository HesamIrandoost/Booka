from rest_framework import serializers
from book.models import Book, Author,Collection,Review,Genre


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name', 'description']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'profile', 'biography', 'website','date_born', 'place_born']


class AllBooksSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)

    author = AuthorSerializer(read_only=True)
    class Meta:
        model = Book
        fields = ['id',
            'author', 'slug', 'title', 'about',
            'summary', 'cover', 'pages', 'genres',
            'star', 'publisher', 'published_date', 
            'created_at'
        ]
