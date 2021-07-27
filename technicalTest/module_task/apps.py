# Django
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class ModuleTaskConfig(AppConfig):
    name          = 'module_task'
    namespace     = 'module_task'
    label         = 'module_task'
    verbose_name  = _('Task')

    def ready(self):
        super().ready()




