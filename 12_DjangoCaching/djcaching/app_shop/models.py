from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Balance(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.IntegerField(default=0, null=True,
                                  verbose_name=_('balance'))

    class Meta:
        verbose_name = _('balance')
        verbose_name_plural = _('balances')


class Promo(models.Model):
    title = models.CharField(max_length=100, verbose_name=_('title promo'))
    terms = models.CharField(max_length=1000, verbose_name=_('terms of promo'))

    class Meta:
        verbose_name = _('promotion')
        verbose_name_plural = _('promotions')


class Offer(models.Model):
    description = models.CharField(max_length=1000,
                                   verbose_name=_('offer description'))
    user_offer = models.ForeignKey(User, on_delete=models.CASCADE, blank=True,
                                   null=True,
                                   verbose_name=_('offer to user'),
                                   related_name='user')

    class Meta:
        verbose_name = _('offer')
        verbose_name_plural = _('offers')


class Purchase(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('purchase name'))
    price = models.IntegerField(verbose_name=_('purchase price'))
    user_purchase = models.ForeignKey(User, on_delete=models.CASCADE, null=True,
                                      blank=True,
                                      verbose_name=_('buyer'),
                                      related_name='buyer')

    class Meta:
        verbose_name = _('purchase')
        verbose_name_plural = _('purchases')


class Shop(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('shop name'))
    address = models.CharField(max_length=150, verbose_name=_('shop address'))

    class Meta:
        verbose_name = _('shop')
        verbose_name_plural = _('shops')
