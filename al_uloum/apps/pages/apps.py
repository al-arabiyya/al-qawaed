"""AppConf for al_uloum.apps.pages"""

from django.apps import AppConfig


# Create your AppConf here.
class PagesConfig(AppConfig):
    """App Configuration for al_uloum.apps.pages"""

    label = "al_uloum_pages"
    name = "al_uloum.apps.pages"
    default_auto_field = "django.db.models.BigAutoField"
