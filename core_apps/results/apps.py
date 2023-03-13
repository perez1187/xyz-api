from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class DsgresConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core_apps.results"
    verbose_name = _("results")
