from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AppUserConfig(AppConfig):
    name = 'app_user'
    verbose_name = _('user')
