from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework import generics
from .serializers import RegisterSerializer, UserSerializer, UserUpdateSerializer
from account.models import User
from book.api.serializers import UserSerializer as us


class RegisterAPIView(CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


class LoginAPIView(TokenObtainPairView):
    pass


class RefreshTokenAPIView(TokenRefreshView):
    pass


class UserDetailView(generics.RetrieveAPIView):
    serializer_class = us
    queryset = User.objects.all()
    lookup_field = "username"


class MeAPIView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

    def get_serializer_class(self):
        if self.request.method in ("PUT", "PATCH"):
            return UserUpdateSerializer
        return UserSerializer
