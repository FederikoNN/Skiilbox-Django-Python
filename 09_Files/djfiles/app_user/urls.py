from django.conf.urls.static import static
from django.urls import path
from .views import LoginForm, LogoutForm, SignUpForm, EditProfileFormView
from django.conf import settings

urlpatterns = [
                  path('login/', LoginForm.as_view(), name='login'),
                  path('logout/', LogoutForm.as_view(), name='logout'),
                  path('register/', SignUpForm.as_view(), name='register'),
                  path('<int:pk>/edit_profile/',
                       EditProfileFormView.as_view(), name='edit_profile'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
