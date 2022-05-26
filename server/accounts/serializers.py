from rest_framework import serializers
from django.contrib.auth import get_user_model
from movies.models import Movie

class ProfileSerializer(serializers.ModelSerializer):

    class MovieSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Movie
            fields = ('pk', 'title', 'poster_path',)

    # like_movies = movieSerializer(many=True)
    # movies = MovieSerializer(many=True)

    class Meta:
        model = get_user_model()
        fields = ('pk', 'username', 'email',)

