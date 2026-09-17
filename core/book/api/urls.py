from django.urls import path

from .views import AllBookListView

app_name = 'book'

urlpatterns = [
    path("books/", AllBookListView.as_view(), name="all-books"),
]