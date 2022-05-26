from django.db import models
from django.conf import settings
# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Movie(models.Model):
    poster_path = models.CharField(max_length=200, blank=True, null=True)
    adult = models.BooleanField()
    overview = models.TextField(null=True, blank=True)
    release_date = models.TextField(null=True, blank=True)
    genre_ids = models.ManyToManyField(Genre, related_name='movie_genre')
    original_title = models.CharField(max_length=200)
    original_language = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    popularity = models.FloatField(null=True, blank=True)
    video_key = models.CharField(max_length=200, blank=True, null=True)
    vote_average = models.FloatField(null=True, blank=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')

class Boxoffice(models.Model):
    poster_path = models.CharField(max_length=200, blank=True, null=True)
    adult = models.BooleanField()
    overview = models.TextField(null=True, blank=True)
    release_date = models.TextField(null=True, blank=True)
    genre_ids = models.ManyToManyField(Genre, related_name='movie_genres')
    original_title = models.CharField(max_length=200)
    original_language = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    popularity = models.FloatField(null=True, blank=True)
    vote_average = models.FloatField(null=True, blank=True)
    
class Comment(models.Model):
    content = models.CharField(max_length=200)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
