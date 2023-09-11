from django.urls import path
from .views import RatingAPIVIew


urlpatterns = [
    path('ratings/<uuid:post_id>/', RatingAPIVIew.as_view(), name='ratings'),
]