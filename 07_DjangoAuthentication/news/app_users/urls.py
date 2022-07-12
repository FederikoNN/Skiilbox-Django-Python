from django.urls import path
from .views import LoginForm, LogoutForm

urlpatterns = [
    path('login/', LoginForm.as_view(), name='login'),
    path('logout/', LogoutForm.as_view(), name='logout'),
]
