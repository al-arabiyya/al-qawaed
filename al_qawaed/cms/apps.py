"""AppConf for al_qawaed.cms"""

from django.apps import AppConfig


# Create your config here.
class CMSConfig(AppConfig):
    """App configuration for al_qawaed.cms"""

    name = "al_qawaed.cms"
    label = "al_qawaed_cms"
    default_auto_field = "django.db.models.BigAutoField"
