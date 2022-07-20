from django.conf.urls.static import static
from django.urls import path
from .views import LoginForm, LogoutForm, SignUpForm, EditProfileFormView, \
    PostSinglePageView, PostCreationFormView, PostsListView, load_posts
from django.conf import settings

urlpatterns = [
                  path('', PostsListView.as_view(), name='main'),
                  path('login/', LoginForm.as_view(), name='login'),
                  path('logout/', LogoutForm.as_view(), name='logout'),
                  path('register/', SignUpForm.as_view(), name='register'),
                  path('<int:pk>/edit_profile/', EditProfileFormView.as_view(),
                       name='edit_profile'),
                  path('<int:pk>/post_single_page/',
                       PostSinglePageView.as_view(), name='запись'),
                  path('post_creation_page/',
                       PostCreationFormView.as_view()),
                  path('upload_posts_file/', load_posts, name='upload')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
