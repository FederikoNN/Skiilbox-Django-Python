from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.IntegerField(null=True, verbose_name='телефон')
    city = models.CharField(max_length=30, verbose_name='город')
    about_user = models.TextField(blank=True, verbose_name='о себе')
    # avatar = models.ImageField(upload_to='images/', blank=True)

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'


class Post(models.Model):
    title = models.CharField(max_length=1000, verbose_name='название поста')
    description = models.CharField(max_length=10000,
                                   verbose_name='содержание поста')
    date_create = models.DateField(auto_now_add=True,
                                   verbose_name='дата публикации')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,
                             blank=True)
    images = models.ManyToManyField('Gallery', blank=True,
                                    related_name='gallery')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'


class Gallery(models.Model):
    image = models.ImageField(upload_to='images/', null=True)

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
