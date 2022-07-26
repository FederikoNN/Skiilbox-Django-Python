from django.conf.urls.static import static
from django.urls import path
from .views import LoginForm, LogoutForm, SignUpForm, MyAccountView, \
    ShopListView
from django.conf import settings

urlpatterns = [
                  path('login/', LoginForm.as_view(), name='login'),
                  path('logout/', LogoutForm.as_view(), name='logout'),
                  path('register/', SignUpForm.as_view(), name='register'),
                  path('', ShopListView.as_view(), name='main'),
                  path('<int:pk>/my_account/', MyAccountView.as_view(),
                       name='my_account'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
