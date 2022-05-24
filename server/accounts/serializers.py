from rest_framework import serializers
from django.contrib.auth import get_user_model
from movies.models import Movie
# from movies.serializers.moviedetail import MovieSerializer

class ProfileSerializer(serializers.ModelSerializer):

    class movieSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Movie
            fields = ('pk', 'movieNm', 'posterSrc', 'average', 'releaseDate')
            # fields = ('pk',)

    like_movies = movieSerializer(many=True)
    
    # movie = movieSerializer(many=True)

    class Meta:
        model = get_user_model()
        # fields = '__all__'
        fields = ('pk', 'like_movies', 'username',)
        read_only_fields = ('instagram', 'facebook',)

