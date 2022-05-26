import requests
import json


class URLMaker:
    url = 'https://api.themoviedb.org/3'

    def __init__(self, key):
        self.key = key

    def get_movie_url(self, category='movie', feature='popular', page='1'):
        url = f'{self.url}/{category}/{feature}'
        url += f'?api_key={self.key}&language=ko-KR&page={str(page)}'

        return url

    def movie_id(self, title):
        url = self.get_url('search', 'movie', region='KR', language='ko', query=title)
        res = requests.get(url)  
        movie = res.json() 

        if len(movie.get('results')): 
            return movie.get('results')[0].get('id')
        else:
            return None

    def get_genre_url(self):
        url = f'{self.url}/genre/movie/list?api_key={self.key}'
        return url

    def get_box_url(self):
        url = f'{self.url}/movie/now_playing?api_key={self.key}&language=ko-KR'
        return url

TMDB_KEY = 'ccd52823f0f41fe9f4e14f84c4169560'

url = URLMaker(TMDB_KEY)

def create_movie_data():
    movie_data = []

    for page in range(1, 100):
        raw_data = requests.get(url.get_movie_url(page=page))
        json_data = raw_data.json()
        movies = json_data.get('results')

        for movie in movies:
            if movie.get('release_date') == "" or movie.get('poster_path') == "":
                continue
            movie_id = movie.get('id')
            video_url = f'https://api.themoviedb.org/3/movie/{movie_id}/videos'
            params = {
                'api_key' : TMDB_KEY
            }
            video_raw_data = requests.get(video_url, params=params)
            video_json_data = video_raw_data.json()
            if len(video_json_data.get('results')) == 0 :
                continue
            video_key = video_json_data.get('results')[0].get('key')
            
            movie.pop('backdrop_path')
            movie.pop('video')
            movie['like_users'] = []
            movie['video_key'] = video_key
            tmp = {
                'model': 'movies.movie',
                'pk': movie['id'],
                'fields': {
                    "poster_path": movie['poster_path'],
                    "adult": movie['adult'],
                    "overview": movie['overview'],
                    "release_date": movie['release_date'],
                    "genre_ids": movie['genre_ids'],
                    "original_title": movie['original_title'],
                    "original_language": movie['original_language'],
                    "title": movie['title'],
                    "popularity": movie['popularity'],
                    "video_key": movie['video_key'],
                    "vote_average": movie['vote_average'],
                }
            }
            movie_data.append(tmp)

    with open('moviedata.json', 'w', encoding='UTF-8') as f:
        json.dump(movie_data, f, indent=4, ensure_ascii=False)

create_movie_data()