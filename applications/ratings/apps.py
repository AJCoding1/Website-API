from django.apps import AppConfig
from django.utils.translation import gettext_lazy as trans


class RatingsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "applications.ratings"
    verbose_name = trans('Rating')
