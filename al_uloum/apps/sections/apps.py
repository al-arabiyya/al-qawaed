"""AppConf for al_uloum.apps.sections"""

from django.apps import AppConfig


# Create your AppConf here.
class SectionsConfig(AppConfig):
    """App Configuration for al_uloum.apps.sections"""

    label = "al_uloum_sections"
    name = "al_uloum.apps.sections"
    default_auto_field = "django.db.models.BigAutoField"
