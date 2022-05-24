from django.db import models
from django.conf import settings
# Create your models here.

class Genre(models.Model):
    genre_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.genre_name
    

class Movie(models.Model):
    title = models.CharField(max_length=100)
    posterSrc = models.CharField(max_length=200)
    releaseDate = models.CharField(max_length=100)
    average = models.FloatField()
    rank = models.IntegerField()
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies', blank=True)
    screenNum = models.IntegerField()
    spectatorNum = models.IntegerField()
    nation = models.CharField(max_length=100)
    genre = models.ManyToManyField(Genre)
    showtime = models.IntegerField()
    director = models.CharField(max_length=100)
    
   

class Comment(models.Model):
    content = models.CharField(max_length=200)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
