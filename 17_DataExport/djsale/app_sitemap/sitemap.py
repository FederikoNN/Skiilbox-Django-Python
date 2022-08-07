from django.contrib.sitemaps import Sitemap
from django.apps import apps
from django.urls import reverse

News = apps.get_model('app_news', 'News')
Housing = apps.get_model('app_real_estate', 'HousingObject')


class RealEstateStaticSitemap(Sitemap):
    changefreq = 'dayly'
    priority = 0.9

    def items(self):
        return ['about', 'contacts']

    def location(self, item):
        return reverse(item)


class RealEstateDynamicSitemap(Sitemap):
    changefreq = 'dayly'
    priority = 0.9

    def items(self):
        return Housing.objects.all()


class NewsSitemap(Sitemap):
    changefreq = 'dayly'
    priority = 0.9

    def items(self):
        return News.objects.filter(is_published=True).all()

    def lastmod(self, obj: News):
        return obj.date_create
