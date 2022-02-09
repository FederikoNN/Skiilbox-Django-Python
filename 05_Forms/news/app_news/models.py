from django.db import models


# from django.forms import Textarea


class News(models.Model):
    title = models.CharField(max_length=1000, verbose_name='название статьи')
    description = models.CharField(max_length=10000,
                                   verbose_name='содержание статьи')
    date_create = models.DateField(auto_now_add=True,
                                   verbose_name='дата публикации')
    date_edit = models.DateField(auto_now=True,
                                 verbose_name='дата редактирования')
    activity = models.IntegerField(default=0,
                                   verbose_name='количество комментариев')

    def __str__(self):
        return self.title


class Comment(models.Model):
    user_name = models.CharField(max_length=100,
                                 verbose_name='имя пользователя')
    description = models.CharField(max_length=10000,
                                   verbose_name='текст комментария')
    news_comment = models.ForeignKey('News', on_delete=models.CASCADE,
                                     related_name='news',
                                     verbose_name='Новость')

    def __str__(self):
        return self.user_name
