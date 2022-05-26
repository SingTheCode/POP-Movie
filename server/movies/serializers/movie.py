from rest_framework import serializers
from django.contrib.auth import get_user_model
from ..models import Movie, Genre, Boxoffice
from .comment import CommentSerializer


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('id','name',)

class MovieListSerializer(serializers.ModelSerializer):

    genre_ids = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ('__all__')

class BoxofficeSerializer(serializers.ModelSerializer):

    genre_ids = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = Boxoffice
        fields = ('__all__')

class MovieSerializer(serializers.ModelSerializer):
    
    genre_ids = GenreSerializer(many=True, read_only=True)

    class UserSerializer(serializers.ModelSerializer) :

        class Meta :
            model = get_user_model
            fields = ('pk','username')

    comments = CommentSerializer(many=True, read_only=True)
    # like_users = UserSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)


    class Meta:
        model = Movie
        fields = ('__all__')
        # fields = ('pk', 'poster_path', 'adult', 'overview', 'release_date', 'genre_ids', 'original_title', 'original_language', 'title', 'popularity', 'video_key', 'vote_average', 'comments', 'user',)