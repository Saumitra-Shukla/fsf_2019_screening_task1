from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class tasksConfig(AppConfig):
    name = 'tasks'
    verbose_name = _(' Task Management')
