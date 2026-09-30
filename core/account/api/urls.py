from django.urls import path

from .views import (
    RegisterAPIView,
    LoginAPIView,
    RefreshTokenAPIView,
    MeAPIView,
)

# root = /api/auth/
urlpatterns = [
    path("register/", RegisterAPIView.as_view()),
    path("login/", LoginAPIView.as_view()),
    path("refresh/", RefreshTokenAPIView.as_view()),
    path("me/", MeAPIView.as_view()),
]
