from django.urls import path
from .views import LoginForm, LogoutForm, SignUpForm, MyAccountView, DepositView

urlpatterns = [
    path('login/', LoginForm.as_view(), name='login'),
    path('logout/', LogoutForm.as_view(), name='logout'),
    path('register/', SignUpForm.as_view(), name='register'),
    path('<int:pk>/my_account/', MyAccountView.as_view(),
         name='my_account'),
    path('<int:pk>/deposit/', DepositView.as_view(), name='deposit'),
]
