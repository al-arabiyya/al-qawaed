"""AppConf for al_uloum.cms"""

from django.apps import AppConfig


# Create your config here.
class CMSConfig(AppConfig):
    """App configuration for al_uloum.cms"""

    name = "al_uloum.cms"
    label = "al_uloum_cms"
    default_auto_field = "django.db.models.BigAutoField"
