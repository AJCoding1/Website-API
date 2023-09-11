from django.apps import AppConfig
from django.utils.translation import gettext_lazy as trans


class UsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "applications.users"
    verbose_name = trans('User')
