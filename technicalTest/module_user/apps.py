# Django
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class ModuleUserConfig(AppConfig):
    name          = 'module_user'
    namespace     = 'module_user'
    label         = 'module_user'
    verbose_name  = _('User')

    def ready(self):
        super().ready()




