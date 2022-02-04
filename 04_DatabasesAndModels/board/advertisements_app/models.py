from django.db import models
from datetime import datetime
from pycbrf.toolbox import ExchangeRates

date_now = datetime.now().strftime('%Y-%m-%d')
rates = ExchangeRates(date_now)['USD'].rate


class Advertisement(models.Model):
    title = models.CharField(max_length=1000,
                             verbose_name='заголовок объявления')
    description = models.CharField(max_length=1000, default='',
                                   verbose_name='описание')
    price = models.IntegerField(default=0, verbose_name='цена')
    publication_date = models.DateTimeField(auto_now_add=True,
                                            verbose_name='дата публикации')
    publication_end_date = models.DateField(
        verbose_name='дата окончания публикации')
    views_count = models.IntegerField(default=0,
                                      verbose_name='количество просмотров')
    user_adv = models.ForeignKey('AdvertisementUser', on_delete=models.CASCADE,
                                 related_name='advertisements',
                                 verbose_name='автор объявления')
    category_adv = models.ForeignKey('AdvertisementCategory',
                                     related_name='advertisements',
                                     on_delete=models.CASCADE,
                                     verbose_name='Рубрика')
    type_adv = models.ForeignKey('AdvertisementType', on_delete=models.CASCADE,
                                 related_name='advertisements',
                                 verbose_name='Тип объявления')

    def get_price_usd(self):
        return round(self.price / rates, 2)

    price_usd = property(get_price_usd)

    def __str__(self):
        return self.title


class AdvertisementUser(models.Model):
    name = models.CharField(max_length=100, verbose_name='имя')
    e_mail = models.EmailField(verbose_name='E-mail')
    phone = models.IntegerField(verbose_name='телефон')

    def __str__(self):
        return self.name


class AdvertisementCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class AdvertisementType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
