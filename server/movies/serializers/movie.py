from rest_framework import serializers
from django.contrib.auth import get_user_model
from ..models import Movie

class MovieListSerializer(serializers.ModelSerializer):
    # class UserSerializer(serializers.ModelSerializer):
    #     class Meta:
    #         model = get_user_model()
    #         fields = ('pk', 'username',)

    class Meta:
        model = Movie
        fields = ('pk', 'title', 'posterSrc', 'releaseDate', 'rank', 'screenNum', 'spectatorNum',)
