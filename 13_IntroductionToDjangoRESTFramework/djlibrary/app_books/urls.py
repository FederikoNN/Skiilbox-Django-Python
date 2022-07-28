# from django.conf.urls.static import static
from django.urls import path
from .views import AuthorList, BookList
# from django.conf import settings

urlpatterns = [
    path('authors/', AuthorList.as_view(), name='authors_list'),
    path('books/', BookList.as_view(), name='books_list'),
    # path('register/', SignUpForm.as_view(), name='register'),
    # path('<int:pk>/my_account/', MyAccountView.as_view(),
    #      name='my_account'),
]
