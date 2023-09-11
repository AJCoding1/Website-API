from rest_framework import serializers
from .models import Rating


class RatingSerializer(serializers.ModelSerializer):
    post_title = serializers.CharField(source='post.title', read_only=True)
    user_firstname = serializers.CharField(source='user.first_name', read_only=True)

    class Meta:
        model = Rating
        fields = ['pkid','id','post_title','user_firstname','created_at','updated_at']



