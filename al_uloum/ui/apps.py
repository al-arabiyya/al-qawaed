"""AppConf for al_uloum.ui"""

from django.apps import AppConfig


# Create your config here.
class UIConfig(AppConfig):
    """App configuration for al_uloum.ui"""

    name = "al_uloum.ui"
    label = "al_uloum_ui"
    default_auto_field = "django.db.models.BigAutoField"
