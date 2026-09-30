from django.urls import path

from . import views

app_name = "book"

urlpatterns = [
    path("books/", views.AllBookListView.as_view(), name="books-list"),
    path("books/<slug:slug>/", views.DetailBookView.as_view(), name="books-detail"),
    path(
        "books/<slug:slug>/reviews/",
        views.ReviewListCreateView.as_view(),
        name="books-reviews",
    ),
    path(
        "books/<slug:slug>/reviews/<int:pk>/",
        views.ReviewReplyCreateView.as_view(),
        name="books-reviews-replies",
    ),
    path("authors/", views.AuthorListView.as_view(), name="authors-list"),
    path(
        "authors/<slug:slug>/", views.AuthorDetailView.as_view(), name="authors-detail"
    ),
    path("genres/", views.GenreListView.as_view(), name="genres-list"),
    path("genres/<int:pk>/", views.GenreDetailView.as_view(), name="genres-detail"),
    path("collections/", views.CollectionListView.as_view(), name="collection-list"),
    path(
        "collections/user/",
        views.CollectionUserListView.as_view(),
        name="collection-list-user",
    ),
    path(
        "collections/<int:pk>/",
        views.CollectionDetailView.as_view(),
        name="collection-detail",
    ),
    path(
        "collections/public/<int:pk>/",
        views.CollectionPublicDetailView.as_view(),
        name="collection-detail-public",
    ),
    path(
        "collections/<int:pk>/add/<int:book_id>/",
        views.AddBookToCollectionView.as_view(),
        name="collection-add-book",
    ),
    path(
        "collections/<int:pk>/remove/<int:book_id>/",
        views.RemoveBookFromCollectionView.as_view(),
        name="collection-remove-book",
    ),
    # test
    path(
        "reviews/recent/", views.RecentReviewListView.as_view(), name="reviews-recent"
    ),
    path(
        "reviews/<int:pk>/like/",
        views.ReviewLikeToggleView.as_view(),
        name="review-like",
    ),
]
