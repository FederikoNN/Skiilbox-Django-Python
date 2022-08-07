from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=1000, verbose_name='название статьи')
    description = models.CharField(max_length=10000, default='',
                                   verbose_name='описание')
    date_create = models.DateField(auto_now_add=True,
                                   verbose_name='дата публикации')
    text = models.TextField(default='', verbose_name='содержание статьи')
    is_published = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('news_detail', args=[str(self.id)])

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'


class NewsType(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    code = models.CharField(max_length=50, verbose_name='код')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'тип новостей'
        verbose_name_plural = 'типы новостей'
