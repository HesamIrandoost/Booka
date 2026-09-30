from rest_framework.pagination import PageNumberPagination


class BookPagination(PageNumberPagination):
    page_size = 20
