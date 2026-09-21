from django.shortcuts import get_object_or_404

from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from book.models import Author, Book, Collection, Genre, Review

from .filters import BookFilter
from .pagination import BookPagination
from .serializers import (
    AllBooksSerializer,
    AuthorSerializer,
    CollectionSerializer,
    DetailBooksSerializer,
    GenreSerializer,
    ReviewSerializer,
)
from .alternate_serializers import AuthorDetailSerializer, GenreDetailSerializer

# =========================================================
# Books
# =========================================================


class AllBookListView(generics.ListAPIView):
    serializer_class = AllBooksSerializer
    pagination_class = BookPagination
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]

    search_fields = ["title", "author__first_name", "author__last_name", "genres__name"]
    filterset_class = BookFilter
    ordering_fields = [
        "title",
        "author",
        "star",
        "published_date",
    ]

    ordering = ["-created_at"]

    queryset = Book.objects.select_related("author").prefetch_related("genres").all()


class DetailBookView(generics.RetrieveAPIView):
    serializer_class = DetailBooksSerializer
    lookup_field = "slug"

    queryset = (
        Book.objects.select_related("author")
        .prefetch_related(
            "genres",
            "reviews__user",
        )
        .all()
    )


# =========================================================
# Reviews
# =========================================================


class ReviewListCreateView(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return (
            Review.objects.filter(
                book__slug=self.kwargs["slug"],
                status=True,
                # parent__isnull=True,
            )
            .select_related("user", "book")
            .prefetch_related("replies__user")
        )

    def get_permissions(self):
        if self.request.method == "POST":
            return [permissions.IsAuthenticated()]

        return [permissions.AllowAny()]

    def perform_create(self, serializer):
        book = get_object_or_404(
            Book,
            slug=self.kwargs["slug"],
        )

        serializer.save(
            user=self.request.user,
            book=book,
        )


class ReviewReplyCreateView(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        review = get_object_or_404(
            Review,
            pk=self.kwargs["pk"],
            status=True,
        )

        serializer.save(
            user=self.request.user,
            book=review.book,
            parent=review,
        )


# =========================================================
# Authors
# =========================================================


class AuthorListView(generics.ListAPIView):
    serializer_class = AuthorSerializer
    pagination_class = BookPagination
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]

    search_fields = ["first_name", "last_name"]
    filterset_fields = {"slug": ["iexact"]}
    ordering_fields = [
        "slug",
    ]

    queryset = Author.objects.all()


class AuthorDetailView(generics.RetrieveAPIView):
    serializer_class = AuthorDetailSerializer
    lookup_field = "slug"
    filter_backends = [
        SearchFilter,
    ]

    search_fields = ["books__title"]
    queryset = Author.objects.prefetch_related("books").all()


# =========================================================
# Genres
# =========================================================


class GenreListView(generics.ListAPIView):
    serializer_class = GenreSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]

    search_fields = ["name"]
    filterset_fields = {"slug": ["iexact"]}
    ordering_fields = [
        "slug",
    ]

    queryset = Genre.objects.all()


class GenreDetailView(generics.RetrieveAPIView):
    serializer_class = GenreDetailSerializer
    # lookup_field = "pk"
    lookup_field = "slug"
    filter_backends = [
        SearchFilter,
    ]

    search_fields = [
        "books__title",
        "author__first_name",
        "author__last_name",
    ]
    queryset = Genre.objects.prefetch_related("books").all()


# =========================================================
# Collections
# =========================================================


class CollectionListView(generics.ListCreateAPIView):
    serializer_class = CollectionSerializer
    filter_backends = [SearchFilter, OrderingFilter]

    search_fields = [
        "books__title",
        "books__author__first_name",
        "books__author__last_name",
        "user__username",
    ]
    ordering_fields = ["slug", "title", "created_at"]

    def get_queryset(self):
        return (
            Collection.objects.filter(is_public=True)
            .select_related("user")
            .prefetch_related(
                "books__author",
                "books__genres",
            )
        )

    def get_permissions(self):
        if self.request.method == "POST":
            return [permissions.IsAuthenticated()]

        return [permissions.AllowAny()]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CollectionUserListView(generics.ListCreateAPIView):
    serializer_class = CollectionSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]

    search_fields = [
        "books__title",
        "books__author__first_name",
        "books__author__last_name",
    ]
    ordering_fields = ["slug", "title", "created_at"]
    filterset_fields = ["is_public"]

    def get_queryset(self):
        return (
            Collection.objects.filter(user=self.request.user)
            .select_related("user")
            .prefetch_related(
                "books__author",
                "books__genres",
            )
        )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CollectionDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CollectionSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [
        SearchFilter,
    ]

    search_fields = [
        "books__title",
        "books__author__first_name",
        "books__author__last_name",
    ]

    # lookup_field = 'pk'
    def get_queryset(self):
        return (
            Collection.objects.filter(user=self.request.user)
            .select_related("user")
            .prefetch_related(
                "books__author",
                "books__genres",
            )
        )


class CollectionPublicDetailView(generics.RetrieveAPIView):
    """for all users"""

    serializer_class = CollectionSerializer
    filter_backends = [
        SearchFilter,
    ]

    search_fields = [
        "books__title",
        "books__author__first_name",
        "books__author__last_name",
    ]

    # lookup_field = 'pk'
    def get_queryset(self):
        return (
            Collection.objects.filter(is_public=True)
            .select_related("user")
            .prefetch_related(
                "books__author",
                "books__genres",
            )
        )


class AddBookToCollectionView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk, book_id):
        collection = get_object_or_404(
            Collection,
            pk=pk,
            user=request.user,
        )

        book = get_object_or_404(
            Book,
            pk=book_id,
        )

        collection.books.add(book)
        return Response({"detail": "Book added to collection."})


class RemoveBookFromCollectionView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, pk, book_id):
        collection = get_object_or_404(
            Collection,
            pk=pk,
            user=request.user,
        )

        book = get_object_or_404(
            Book,
            pk=book_id,
        )

        collection.books.remove(book)
        return Response({"detail": "Book removed from collection."})
