from django.urls import path
from .views import AuthorList, BookList, AuthorDetail, BookDetail


urlpatterns = [
    path('authors/', AuthorList.as_view(), name='authors_list'),
    path('books/', BookList.as_view(), name='books_list'),
    path('authors/<int:pk>/', AuthorDetail.as_view(), name='author_detail'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book_detail'),
]
