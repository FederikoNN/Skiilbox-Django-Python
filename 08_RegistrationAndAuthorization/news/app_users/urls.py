from django.urls import path
from .views import LoginForm, LogoutForm, SignUpForm, ProfileData

urlpatterns = [
    path('account_detail/', ProfileData.as_view(), name='account_detail'),
    path('login/', LoginForm.as_view(), name='login'),
    path('logout/', LogoutForm.as_view(), name='logout'),
    path('register/', SignUpForm.as_view(), name='register'),
]


