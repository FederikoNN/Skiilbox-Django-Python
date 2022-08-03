from django.contrib.auth.models import User
from django.db import models


class Shop(models.Model):
    name = models.CharField(max_length=100, verbose_name='shop name')
    address = models.CharField(max_length=150, verbose_name='shop address')

    class Meta:
        verbose_name = 'shop'
        verbose_name_plural = 'shops'


class Item(models.Model):
    name = models.CharField(max_length=100, verbose_name='item name')
    price = models.IntegerField(default=0, verbose_name='price item ')
    shops = models.ManyToManyField(Shop, through='ItemInShop',
                                   related_name='shops')

    class Meta:
        verbose_name = 'item'
        verbose_name_plural = 'items'

    def __str__(self):
        return self.name


class ItemInShop(models.Model):
    items = models.ForeignKey(Item, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0, verbose_name='quantity')

    class Meta:
        verbose_name = 'item in shop'
        verbose_name_plural = 'items in shop'


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    product = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    @property
    def total_cost(self):
        return self.product.price * self.quantity

    class Meta:
        verbose_name = 'cart'
        verbose_name_plural = 'carts'

    def __str__(self):
        return self.product.name


class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    cost = models.IntegerField(default=0, verbose_name='cost')

    class Meta:
        verbose_name = 'purchase'
        verbose_name_plural = 'purchases'
