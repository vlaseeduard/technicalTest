# Django
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class ModulePageConfig(AppConfig):
    name = 'module_page'
    namespace = 'module_page'
    label = 'module_page'
    verbose_name = _('Page')

    def ready(self):
        super().ready()




