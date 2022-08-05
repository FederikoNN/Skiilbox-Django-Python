from django.db import models
from django.contrib.auth.models import User
import logging

logger = logging.getLogger(__name__)


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.IntegerField(default=0, null=True,
                                  verbose_name='balance')
    status_points = models.IntegerField(default=0, null=True,
                                        verbose_name='status')
    status_previous = models.CharField(max_length=20, default='No status')

    @property
    def status(self):
        if self.status_points > 1000:
            if self.status_previous != 'Platinum':
                logger.info('Congratulation with Platinum level')
            return 'Platinum'
        elif self.status_points > 500:
            if self.status_previous != 'Gold':
                logger.info('Congratulation with Gold level')
            return 'Gold'
        elif self.status_points > 100:
            if self.status_previous != 'Silver':
                logger.info('Congratulation with Silver level')
            return 'Silver'
        return 'No status'

    class Meta:
        verbose_name = 'account'
        verbose_name_plural = 'accounts'
