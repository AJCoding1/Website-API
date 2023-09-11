from django.urls import path
from .views import BookmarkListCreateAPIView


urlpatterns = [
    path('bookmark/<uuid:post_id>/',BookmarkListCreateAPIView.as_view(), name='bookmark'),
]