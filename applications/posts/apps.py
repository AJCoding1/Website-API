from django.apps import AppConfig
from django.utils.translation import gettext_lazy as trans


class PostsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "applications.posts"
    verbose_name = trans('Post')


    def ready(self):

        import applications.search.signals
