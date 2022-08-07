from django.contrib.syndication.views import Feed
from django.db.models import QuerySet
from django.urls import reverse
from django.apps import apps

News = apps.get_model('app_news', 'News')


class LatestNewsFeed(Feed):
    title = "Новости"
    link = "/sitenews/"
    description = "Самые свежие новости"

    def items(self) -> QuerySet:
        return News.objects.order_by('date_create')

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description

    def item_link(self, item):
        return reverse('news_detail', args=[item.pk])
