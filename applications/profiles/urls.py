from django.urls import path
from .views import ( 
    FollowApiView,
    ProfileListAPIView,
    ProfileDetailAPIView,
    UnFollowAPIView,
    FollowersListAPIView,
    FollowingListAPIView,
    )


urlpatterns = [
    path('follow/<int:pkid>/', FollowApiView.as_view(), name='follow'),
    path('unfollow/<int:pkid>/', UnFollowAPIView.as_view(), name='unfollow'),
    path('', ProfileListAPIView.as_view(), name='profiles'),
    path('my/',ProfileDetailAPIView.as_view(), name='my-profile'),
    path('my/followers/', FollowersListAPIView.as_view(), name='my-followers'),
    path('my/following/',FollowingListAPIView.as_view(), name='following'),
]