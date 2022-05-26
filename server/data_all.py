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

def create_genre_data():
    genre_url = url.get_genre_url()
    raw_data = requests.get(genre_url)
    json_data = raw_data.json()
    genres = json_data.get('genres')

    genre_data = []

    for genre in genres:
        tmp = {
            'model': 'movies.genre',
            'pk': genre['id'],
            'fields': {
                'name': genre['name']
            }
        }
        genre_data.append(tmp)

    with open('tmdb.json', 'w') as f:
        json.dump(genre_data, f, indent=4)

def create_box_data():
    with open('tmdb.json', 'r+') as f:
        box_data = json.load(f)

    box_url = url.get_box_url()
    raw_data = requests.get(box_url)
    json_data = raw_data.json()
    boxes = json_data.get('results')
    
    box_data = []
    
    for box in boxes:
        tmp = {
            'model': 'movies.boxoffice',
            'pk': box['id'],
            'fields': box
        }
        box_data.append(tmp)
    
    with open('tmdb.json', 'w') as f:
        json.dump(box_data, f, indent=4, ensure_ascii=False)


def create_movie_data():
    with open('tmdb.json', 'r+') as f:
        movie_data = json.load(f)

    for page in range(1, 2):
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
                'pk': movie.pop('id'),
                'fields': movie,
            }
            movie_data.append(tmp)

    with open('tmdb.json', 'w', encoding='UTF-8') as f:
        json.dump(movie_data, f, indent=4, ensure_ascii=False)

create_genre_data()
create_box_data()
create_movie_data()