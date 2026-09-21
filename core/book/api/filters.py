import django_filters
from book.models import Book


class BookFilter(django_filters.FilterSet):
    genre = django_filters.CharFilter(
        field_name="genres__slug",
        lookup_expr="iexact",
    )

    author = django_filters.CharFilter(
        field_name="author__slug",
        lookup_expr="iexact",
    )

    class Meta:
        model = Book
        fields = ["author", "genre", "publisher"]
