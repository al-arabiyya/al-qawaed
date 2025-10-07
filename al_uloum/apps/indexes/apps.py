"""AppConf for al_uloum.apps.indexes"""

from django.apps import AppConfig


# Create your AppConf here.
class IndexesConfig(AppConfig):
    """App Configuration for al_uloum.apps.indexes"""

    label = "al_uloum_indexes"
    name = "al_uloum.apps.indexes"
    default_auto_field = "django.db.models.BigAutoField"
