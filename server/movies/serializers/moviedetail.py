from rest_framework import serializers
from django.contrib.auth import get_user_model
from ..models import Movie
from .comment import CommentSerializer

class MovieSerializer(serializers.ModelSerializer):
    
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('pk', 'username')

    comments = CommentSerializer(many=True, read_only=True)
    # user = UserSerializer(read_only=True)
    like_users = UserSerializer(read_only=True, many=True)

    class Meta:
        model = Movie
        fields = ('pk', 'title', 'posterSrc', 'realseDate', 'nation', 'genre', 'showtime', 'director', 'like_users', 'comments')