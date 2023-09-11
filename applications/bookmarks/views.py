from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import permissions,static,generics
from .serializers import BookmarkSerializer
from .models import Bookmark
from applications.posts.models import Post
from django.exceptions import NotFound


class BookmarkListCreateAPIView(generics.ListCreateAPIView):

    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
    permission_classes = [permissions.IsAuthenticated]


    def get_queryset(self):
        user = self.request.user
        bookmarks = self.queryset.filter(user=user)
        return bookmarks

    def create(self, request, *args, **kwargs):
        user = self.request.user
        post_id = self.kwargs['post_id']

        try:
            post = Post.objects.get(id=post_id)
            if Bookmark.objects.filter(user=user, post=post).exists():
                return Response({'message':f'You already bookmarked \{self.post.title}'})

            Bookmark.objects.create(user=user, post=post)
            return Response({'message':f'Your bookmark of \{self.post.title} is successfull '})

        except Post.DoesNotExist:
            raise NotFound('This post is not found')

