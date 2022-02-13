from django.urls import path
from . import views

urlpatterns = [path('', views.NewsListView.as_view()),
               path('news_creation_page/',
                    views.NewsCreationFormView.as_view()),
               path('news/<int:news_id>/news_edit/',
                    views.NewsEditFormView.as_view()),
               path('news/<int:pk>/news_single_page/',
                    views.NewsSinglePageView.as_view()),
               path('news_list/',
                    views.NewsListView.as_view()),
               ]
