from taggit.serializers import TaggitSerializer, TagListSerializerField
from rest_framework import serializers
from .models import Post,PostView,PostLike
from applications.profiles.serializers import ProfileSerializer


class PostSerailizer(TaggitSerializer, serializers.ModelSerializer):

    tags = TagListSerializerField()
    author = ProfileSerializer(source='author.profile', read_only=True)
    photo = serializers.SerializerMethodField()
    reading_time = serializers.SerializerMethodField()
    views = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'pkid',
            'id',
            'title',
            'slug',
            'content',
            'photo',
            'author',
            'description',
            'average_rating',
            'status',
            'reading_time',
            'tags',
            'views',
            'likes_count',
        ]

   

    def get_photo(self,obj):
        return obj.photo.url

    def get_reading_time(self,obj):
        return obj.reading_time


    def get_views(self, obj):
        return PostView.objects.filter(post=obj).count()

    def get_likes_count(self, obj):
        return obj.likes.count()

    def get_average_rating(self,obj):
        return obj.average_rating

       

class PostLikeSerailizer(serializers.ModelSerializer):
    post_title = serializers.CharField(source='post.title')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name') 
    class Meta:
        model = PostLike
        fields = [
            'first_name',
            'last_name',
            'post_title'
        ]