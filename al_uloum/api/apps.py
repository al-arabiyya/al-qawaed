"""AppConf for al_uloum.api"""

from django.apps import AppConfig


# Create your AppConf here.
class APIConfig(AppConfig):
    """App Configuration for al_uloum.api"""

    name = "al_uloum.api"
    label = "al_uloum_api"
    default_auto_field = "django.db.models.BigAutoField"
