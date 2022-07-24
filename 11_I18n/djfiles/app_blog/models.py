from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Post(models.Model):
    title = models.CharField(max_length=1000, verbose_name=_('title'))
    description = models.CharField(max_length=10000,
                                   verbose_name=_('description'))
    date_create = models.DateField(auto_now_add=True,
                                   verbose_name=_('date_create'))
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,
                             blank=True)
    images = models.ManyToManyField('Gallery', blank=True,
                                    related_name=_('gallery'),
                                    verbose_name=_('attach images'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')


class Gallery(models.Model):
    image = models.ImageField(upload_to='images/', null=True,
                              verbose_name=_('image'))

    class Meta:
        verbose_name = _('image')
        verbose_name_plural = _('images')
