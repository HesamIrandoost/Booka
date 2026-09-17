from django.shortcuts import render
from .serializers import AuthorSerializer, GenreSerializer, AllBooksSerializer
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from book.models import Book
from .pagination import BookPagination
# Create your views here.

# class AllBooksAPIView(APIView):
#     def get(self, request):
#         serializer = AllBooksSerializer(request.data)
        
        # i don know


class AllBookListView(ListAPIView):
    serializer_class = AllBooksSerializer
    pagination_class = BookPagination
    queryset = Book.objects.all()