from django.db import models
from django.contrib.auth.models import User
from django.apps import apps
from django.db.models import Count


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.IntegerField(verbose_name='телефон')
    city = models.CharField(max_length=30, verbose_name='город')
    is_verified = models.BooleanField(default=False, verbose_name='Верификация')

    @property
    def published_news(self):
        news_model = apps.get_model('app_news', 'News')
        news_count = news_model.objects.filter(user=self.user)
        return news_count.count()

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'
        permissions = (
            ('change_profile.is_verified', 'Может верифицировать пользователя'),
        )
