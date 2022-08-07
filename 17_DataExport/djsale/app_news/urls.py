from django.urls import path
from .views import NewsSinglePageView, NewsListView

urlpatterns = [
    path('news/<int:pk>/news_single_page/',
         NewsSinglePageView.as_view(), name='news_detail'),
    path('news_list/', NewsListView.as_view(), name='news_list'),
]
