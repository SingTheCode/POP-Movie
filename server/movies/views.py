# movies/views.py

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Boxoffice, Movie, Comment
from .serializers.movie import MovieListSerializer, MovieSerializer, BoxofficeSerializer
from .serializers.comment import CommentSerializer
import datetime


@api_view(['GET'])
def movie_list(request):
    movies = Boxoffice.objects.order_by('-pk')
    serializer = BoxofficeSerializer(movies, many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

@api_view(['GET'])
def moviebydecade(request):
    movie_decade = ['2020s', '2010s', '2000s', '1990s', '1980s', '1970s', '1960s']
    movie_all = []
    movies = Movie.objects.filter(release_date__gte=datetime.date(2020, 1, 1)).order_by('-popularity')[:30]
    serializer = MovieListSerializer(movies, many=True)
    movie_all.append(serializer.data)

    movies = Movie.objects.filter(release_date__gte=datetime.date(2010, 1, 1)).filter(release_date__lte=datetime.date(2019, 12, 31)).order_by('-popularity')[:30]
    serializer = MovieListSerializer(movies, many=True)
    movie_all.append(serializer.data)

    movies = Movie.objects.filter(release_date__gte=datetime.date(2000, 1, 1)).filter(release_date__lte=datetime.date(2009, 12, 31)).order_by('-popularity')[:30]
    serializer = MovieListSerializer(movies, many=True)
    movie_all.append(serializer.data)

    movies = Movie.objects.filter(release_date__gte=datetime.date(1990, 1, 1)).filter(release_date__lte=datetime.date(1999, 12, 31)).order_by('-popularity')[:30]
    serializer = MovieListSerializer(movies, many=True)
    movie_all.append(serializer.data)

    movies = Movie.objects.filter(release_date__gte=datetime.date(1980, 1, 1)).filter(release_date__lte=datetime.date(1989, 12, 31)).order_by('-popularity')[:30]
    serializer = MovieListSerializer(movies, many=True)
    movie_all.append(serializer.data)

    movies = Movie.objects.filter(release_date__gte=datetime.date(1970, 1, 1)).filter(release_date__lte=datetime.date(1979, 12, 31)).order_by('-popularity')[:30]
    serializer = MovieListSerializer(movies, many=True)
    movie_all.append(serializer.data)

    movies = Movie.objects.filter(release_date__gte=datetime.date(1960, 1, 1)).filter(release_date__lte=datetime.date(1969, 12, 31)).order_by('-popularity')[:30]
    serializer = MovieListSerializer(movies, many=True)
    movie_all.append(serializer.data)
    movies_all = dict(zip(movie_decade, movie_all))

    return Response(movies_all)

    # movie_decade = ['2020s', '2010s', '2000s', '1990s', '1980s', '1970s', '1960s']
    # movie_dict = [[] for _ in range(7)]
    # for movie in movies:
    #     if 2020 <= int(movie.release_date[0:4]) < 2030:
    #         movie_dict[0].append(movie)
    #     elif 2010 <= int(movie.release_date[0:4]) < 2020:
    #         movie_dict[1].append(movie)
    #     elif 2000 <= int(movie.release_date[0:4]) < 2010:
    #         movie_dict[2].append(movie)
    #     elif 1990 <= int(movie.release_date[0:4]) < 2000:
    #         movie_dict[3].append(movie)
    #     elif 1980 <= int(movie.release_date[0:4]) < 1990:
    #         movie_dict[4].append(movie)
    #     elif 1970 <= int(movie.release_date[0:4]) < 1980:
    #         movie_dict[5].append(movie)
    #     elif 1960 <= int(movie.release_date[0:4]) < 1970:
    #         movie_dict[6].append(movie)
    # movies_all = dict(zip(movie_decade, movie_dict))


@api_view(['POST'])
def like_movie(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = request.user
    if movie.like_users.filter(pk=user.pk).exists():
        movie.like_users.remove(user)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    else:
        movie.like_users.add(user)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)


@api_view(['POST'])
def create_comment(request, movie_pk):
    user = request.user
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user=user)
        comments = movie.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
def comment_update_or_delete(request, movie_pk, comment_pk):
    movie = get_object_or_404(movie, pk=movie_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)

    def update_comment():
        if request.user == comment.user:
            serializer = CommentSerializer(instance=comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                comments = movie.comments.all()
                serializer = CommentSerializer(comments, many=True)
                return Response(serializer.data)

    def delete_comment():
        if request.user == comment.user:
            comment.delete()
            comments = movie.comments.all()
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data)
    
    if request.method == 'PUT':
        return update_comment()
    elif request.method == 'DELETE':
        return delete_comment()
