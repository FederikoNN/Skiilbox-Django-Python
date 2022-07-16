from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.IntegerField(verbose_name='телефон')
    city = models.CharField(max_length=30, verbose_name='город')
    published_news = models.IntegerField(default=0,
                                         verbose_name='количество '
                                                      'опубликованных новостей')
    is_verified = models.BooleanField(default=False, verbose_name='Верификация')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'
        permissions = (
            ('change_profile.is_verified', 'Может верифицировать пользователя'),
        )
