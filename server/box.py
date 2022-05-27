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

def create_box_data():

    box_url = url.get_box_url()
    raw_data = requests.get(box_url)
    json_data = raw_data.json()
    boxes = json_data.get('results')
    
    box_data = []
    
    for box in boxes:
        tmp = {
            'model': 'movies.boxoffice',
            'pk': box['id'],
            'fields': {
                "poster_path": box['poster_path'],
                "adult": box['adult'],
                "overview": box['overview'],
                "release_date": box['release_date'],
                "genre_ids": box['genre_ids'],
                "original_title": box['original_title'],
                "original_language": box['original_language'],
                "title": box['title'],
                "popularity": box['popularity'],
                "vote_average": box['vote_average'],
            }
        }
        box_data.append(tmp)
    
    with open('box.json', 'w', encoding='UTF-8') as f:
        json.dump(box_data, f, indent=4, ensure_ascii=False)


create_box_data()
