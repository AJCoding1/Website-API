from rest_framework.views import APIView
from rest_framework import status, permissions, generics
from rest_framework.response import Response
from django.http import Http404,HttpResponse
from rest_framework.exceptions import NotFound
from .serializers import FollowingSerializer, ProfileSerializer
from .models import Profile
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from .exeptions import CantFollowYourself
from .renderers import ProfileJSONRenderer


class ProfileListAPIView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProfileDetailAPIView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProfileSerializer
    renderer_classes = [ProfileJSONRenderer]

    def get_queryset(self):
        queryset = Profile.objects.select_related("user")
        return queryset

    def get_object(self):
        user = self.request.user
        profile = self.get_queryset().get(user=user)
        return profile

class FollowersListAPIView(generics.ListAPIView):

    queryset = Profile.objects.all()
    serializer_class = FollowingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user.profile
        followers = user.followers.all()
        return followers


class FollowingListAPIView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = FollowingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user.profile
        following = user.following.all()
        return following
 

class FollowApiView(APIView):
    def post(self, request, pkid, format=None):

        follower = self.request.user.profile
        follwee = get_object_or_404(Profile, user__pkid=pkid)
        
        if follower == follwee:
            return Response({'message':'You can not follow yourself!'})

        if follwee.followers.filter(user__pkid=follower.pkid).exists():
            return Response({'message':'You are alreday followind this user'})

        follwee.followers.add(follower)
        return Response({'message':'Success'})


class UnFollowAPIView(APIView):
    def post(self, request,pkid, format=None):
        follower = self.request.user.profile
        followee = get_object_or_404(Profile, user__pkid=pkid)
        if followee.followers.filter(user__pkid=follower.pkid).exists():
            followee.followers.remove(follower)
            return Response({'message':'Unfollow is successfull!'})

        return Response({'message':'You are not following this user already!'})
        



  