from django.views.generic import DetailView, ListView
from .models import News


class NewsListView(ListView):
    model = News
    ordering = ['-date_create']
    template_name = 'news/news_list.html'
    context_object_name = 'news_list'


class NewsSinglePageView(DetailView):
    model = News
    template_name = 'news/news_single_page.html'
