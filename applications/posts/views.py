import logging
from django.shortcuts import render,get_object_or_404
from rest_framework.response import Response
from rest_framework import generics , status
from .models import Post,PostLike,PostView
from .serializers import PostSerailizer,PostLikeSerailizer


logger = logging.getLogger(__name__)


class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerailizer


    def get_queryset(self):
        return self.queryset.filter(status=True)

    def perform_create(self,serializer):
        author = request.user

        serializer.save(author=author)
        logger.info(f" Post {serializer.data.get('title')} created by {author.first_name}")


class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerailizer
    lookup_field = 'id'
   

    def retrieve(self, request, *args, **kwargs):
        user = self.request.user
        post = self.get_object()
        serializer = self.get_serializer(post)
        x_forwarded_for = self.request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = self.request.META.get('REMOTE_ADDR', None)

            print(ip)
        

        PostView.save_post_view(user=user, post=post, ip=ip)

        return Response(serializer.data)

    def perform_update(self, serializer):
        instance = serializer.save(author=self.request.user)
        instance.save()

    def destroy(self, request, *args, **kwargs):
        post = get_object_or_404(Post, id=kwargs['id'])  # Retrieve 'id' from kwargs
        post.delete()
        return Response(status=204)  # Return a success response after deletion





class PostLikeAPIView(generics.CreateAPIView, generics.DestroyAPIView):

    queryset = PostLike.objects.all()
    serializer_class = PostLikeSerailizer

    def create(self,request,*args,**kwargs):
        user = request.user
        post_id = kwargs.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        if not PostLike.objects.filter(user=user, post=post).exists():
            PostLike.objects.create(user=user,post=post)
            return Response({"message":"Your like is added successfull"}, status=status.HTTP_201_CREATED,)
        return Response({'message':'You have already liked this post'}, status=status.HTTP_400_BAD_REQUEST,)


    def delete(self,request,*args,**kwargs):
        user = request.user
        post_id = kwargs.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        like = get_object_or_404(PostLike, user=user, post=post)
        like.delete()
        return Response({'message':'Deletion is completed!'}, status=status.HTTP_204_NO_CONTENT,)

        








