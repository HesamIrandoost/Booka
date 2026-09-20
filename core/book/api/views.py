from django.shortcuts import get_object_or_404

from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from book.models import Author, Book, Collection, Genre, Review

from .pagination import BookPagination
from .serializers import (
    AllBooksSerializer,
    AuthorSerializer,
    CollectionSerializer,
    DetailBooksSerializer,
    GenreSerializer,
    ReviewSerializer,
)

# =========================================================
# Books
# =========================================================


class AllBookListView(generics.ListAPIView):
    serializer_class = AllBooksSerializer
    pagination_class = BookPagination

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

from .alternate_serializers import AuthorDetailSerializer, GenreDetailSerializer


class AuthorListView(generics.ListAPIView):
    serializer_class = AuthorSerializer
    pagination_class = BookPagination

    queryset = Author.objects.all()


class AuthorDetailView(generics.RetrieveAPIView):
    serializer_class = AuthorDetailSerializer
    lookup_field = "slug"
    queryset = Author.objects.prefetch_related("books").all()


# =========================================================
# Genres
# =========================================================


class GenreListView(generics.ListAPIView):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()


class GenreDetailView(generics.RetrieveAPIView):
    serializer_class = GenreDetailSerializer
    lookup_field = "pk"
    # lookup_field = "slug"
    queryset = Genre.objects.prefetch_related("books").all()


# =========================================================
# Collections
# =========================================================


class CollectionListView(generics.ListCreateAPIView):
    serializer_class = CollectionSerializer

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
