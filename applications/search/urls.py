from django.urls import path

from .views import PostElasticSearchView

urlpatterns = [
    path(
        "search/",
        PostElasticSearchView.as_view({"get": "list"}),
        name="post_search",
    )
]
