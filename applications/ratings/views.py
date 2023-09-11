from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework import generics,status,permissions
from .models import Rating
from .serailizers import RatingSerializer
from applications.posts.models import Post




class RatingAPIVIew(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticated]



    def create(self, request, *args, **kwargs):
        user = request.user
        post_id = kwargs.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        if Rating.objects.filter(user=user, post=post).exists():
            return Response({'message':'Your can not rate same post twice'})
        Rating.objects.create(user=user, post=post)
        return Response({'message':'Rating is successfull !'})
