from django.apps import AppConfig
from django.utils.translation import gettext_lazy as trans


class ProfilesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "applications.profiles"
    verbose_name = trans("Profiles")


    def ready(self):

        from applications.profiles import signals
