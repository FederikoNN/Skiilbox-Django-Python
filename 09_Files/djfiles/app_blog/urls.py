from django.conf.urls.static import static
from django.urls import path
from .views import PostSinglePageView, PostCreationFormView, PostsListView, \
    load_posts
from django.conf import settings

urlpatterns = [
                  path('', PostsListView.as_view(), name='main'),
                  path('<int:pk>/post_single_page/',
                       PostSinglePageView.as_view(), name='post'),
                  path('post_creation_page/',
                       PostCreationFormView.as_view(), name='post_creation'),
                  path('upload_posts_file/', load_posts, name='upload')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
