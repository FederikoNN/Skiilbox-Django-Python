from rest_framework.mixins import ListModelMixin
from rest_framework.generics import GenericAPIView
from django_filters.rest_framework import FilterSet, DjangoFilterBackend
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer


class AuthorList(ListModelMixin, GenericAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['first_name']

    def get(self, request):
        return self.list(request)


class BooksFilter(FilterSet):
    class Meta:
        model = Book
        fields = {
            'title': ['exact'],
            'pages_number': ['gt', 'exact', 'lt']
        }


class BookList(ListModelMixin, GenericAPIView):
    serializer_class = BookSerializer
    filterset_class = BooksFilter

    def get_queryset(self):
        queryset = Book.objects.all()
        author = self.request.query_params.get('authors')
        if author:
            author = Author.objects.filter(last_name=author).first()
            queryset = queryset.filter(authors=author)
        return queryset

    def get(self, request):
        return self.list(request)
