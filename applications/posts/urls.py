from django.urls import path
from .views import (
    PostListCreateAPIView,
    PostDetailAPIView,
    PostLikeAPIView,

)


urlpatterns = [
    path('posts/', PostListCreateAPIView.as_view(), name='post'),
    path('detail/<uuid:id>/', PostDetailAPIView.as_view(), name='detail'),
    path('like/<uuid:post_id>/',PostLikeAPIView.as_view(), name ='like')
]