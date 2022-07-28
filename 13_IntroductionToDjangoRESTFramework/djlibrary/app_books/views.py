from rest_framework.mixins import ListModelMixin
from rest_framework.generics import GenericAPIView

from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer


class AuthorList(ListModelMixin, GenericAPIView):
    serializer_class = AuthorSerializer

    def get_queryset(self):
        queryset = Author.objects.all()
        author_name = self.request.query_params.get('first_name')
        if author_name:
            queryset = queryset.filter(first_name=author_name)
        return queryset

    def get(self, request):
        return self.list(request)


class BookList(ListModelMixin, GenericAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = Book.objects.all()
        pages = self.request.query_params.get('pages_number')
        title = self.request.query_params.get('title')
        author = self.request.query_params.get('authors')
        if pages:
            # Реализация фильтра "равно"
            # queryset = queryset.filter(pages_number=pages)
            #
            # Реализация фильтра "меньше"
            # queryset = queryset.filter(pages_number__lt=pages)
            #
            # Реализация фильтра "больше"
            queryset = queryset.filter(pages_number__gt=pages)
        elif author and title:
            author = Author.objects.filter(last_name=author).first()
            queryset = queryset.filter(authors=author, title=title)
        return queryset

    def get(self, request):
        return self.list(request)
