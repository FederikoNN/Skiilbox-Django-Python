from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.IntegerField(null=True, verbose_name=_('phone'))
    city = models.CharField(max_length=30, verbose_name=_('city'))
    about_user = models.TextField(blank=True, verbose_name=_('about'))
    avatar = models.ImageField(upload_to='images/', blank=True,
                               verbose_name=_('avatar'))

    class Meta:
        verbose_name = _('user profile')
        verbose_name_plural = _('user profiles')
