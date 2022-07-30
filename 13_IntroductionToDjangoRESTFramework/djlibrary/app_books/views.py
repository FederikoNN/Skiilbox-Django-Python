from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, \
    UpdateModelMixin, DestroyModelMixin
from rest_framework.generics import GenericAPIView
from django_filters.rest_framework import FilterSet, DjangoFilterBackend
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer


class AuthorList(ListModelMixin, GenericAPIView):
    """Представление для получения списка авторов и фильтрации по имени"""
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['first_name']

    def get(self, request):
        return self.list(request)


class AuthorDetail(UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin,
                   GenericAPIView):
    """Представление для получения детальной информации об авторе, а также
    для её редактирования и удаления"""
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class BooksFilter(FilterSet):
    """Представление фильтра для фильтрации по списку книг"""

    class Meta:
        model = Book
        fields = {
            'title': ['exact'],
            'pages_number': ['gt', 'exact', 'lt']
        }


class BookList(ListModelMixin, GenericAPIView):
    """Представление для получения списка книг и фильтрации по параметрам"""
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


class BookDetail(UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin,
                 GenericAPIView):
    """Представление для получения детальной информации о книге, а также
    для её редактирования и удаления"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
