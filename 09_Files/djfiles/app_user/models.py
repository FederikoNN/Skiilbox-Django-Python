from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.IntegerField(null=True, verbose_name='телефон')
    city = models.CharField(max_length=30, verbose_name='город')
    about_user = models.TextField(blank=True, verbose_name='о себе')
    avatar = models.ImageField(upload_to='images/', blank=True)

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'

