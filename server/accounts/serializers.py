from rest_framework import serializers
from django.contrib.auth import get_user_model
from movies.models import Movie

class ProfileSerializer(serializers.ModelSerializer):

    class movieSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Movie
            fields = ('pk', 'title', 'poster_path',)

    like_movies = movieSerializer(many=True)
    movies = movieSerializer(many=True)

    class Meta:
        model = get_user_model()
        fields = ('pk', 'like_movies', 'username', 'email', 'instagram', 'facebook',)

