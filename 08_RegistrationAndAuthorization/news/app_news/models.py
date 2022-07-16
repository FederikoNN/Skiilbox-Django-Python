from datetime import datetime
from django.contrib.auth.models import User
from django.db import models


class News(models.Model):
    title = models.CharField(max_length=1000, verbose_name='название статьи')
    description = models.CharField(max_length=10000,
                                   verbose_name='содержание статьи')
    date_create = models.DateField(auto_now_add=True,
                                   verbose_name='дата публикации')
    date_edit = models.DateField(default=datetime.now(),
                                 verbose_name='дата редактирования')
    activity = models.IntegerField(default=0,
                                   verbose_name='количество комментариев')
    is_active = models.BooleanField(default=False, verbose_name='Опубликовано')
    # tags = models.ManyToManyField('Tag', blank=True, related_name='tags')
    tag = models.CharField(max_length=20, verbose_name='тег', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'


# class Tag(models.Model):
#     title = models.CharField(max_length=20)
#
#     def __str__(self):
#         return self.title


class Comment(models.Model):
    user_name = models.CharField(max_length=100, default='Имя',
                                 verbose_name='имя пользователя')
    description = models.CharField(max_length=10000,
                                   verbose_name='текст комментария')
    news_comment = models.ForeignKey('News', on_delete=models.CASCADE,
                                     related_name='news',
                                     verbose_name='Новость')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,
                             blank=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
