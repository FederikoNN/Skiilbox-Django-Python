from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.IntegerField(default=0, null=True,
                                  verbose_name='balance')
    status_points = models.IntegerField(default=0, null=True,
                                        verbose_name='status')

    @property
    def status(self):
        if self.status_points > 1000:
            return 'Platinum'
        elif self.status_points > 500:
            return 'Gold'
        elif self.status_points > 100:
            return 'Silver'
        return 'No status'

    class Meta:
        verbose_name = 'account'
        verbose_name_plural = 'accounts'

# class Purchase(models.Model):
#     name = models.CharField(max_length=100, verbose_name=_('purchase name'))
#     price = models.IntegerField(verbose_name=_('purchase price'))
#     user_purchase = models.ForeignKey(User, on_delete=models.CASCADE,
#     null=True,
#                                       blank=True,
#                                       verbose_name=_('buyer'),
#                                       related_name='buyer')
#
#     class Meta:
#         verbose_name = _('purchase')
#         verbose_name_plural = _('purchases')
