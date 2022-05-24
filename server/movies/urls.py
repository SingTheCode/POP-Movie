from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.movie_list),
    path('<int:movie_pk>/', views.movie_detail),
    path('moviebydecade/', views.moviebydecade),
    path('<int:movie_pk>/like/', views.like_movie),
    path('<int:movie_pk>/comments/', views.create_comment),
    path('<int:movie_pk>/comments/<int:comment_pk>/', views.comment_update_or_delete)
]
