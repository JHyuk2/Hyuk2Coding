import requests
from datetime import datetime
from pprint import pprint as pp


# 영화진흥위원회 api
auth_key = 'b258de996338d701bdc72509d7eee505'
year = str(datetime.today().year)
month = '0'+str(datetime.today().month) if len(str(datetime.today().month)) == 1 else str(datetime.today().month)
day = str(datetime.today().day -2)
targetDt = year + month + day
base_url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?'
json_url = f'{base_url}key={auth_key}&targetDt={targetDt}'

data = requests.get(json_url).json()
movie_list = data['boxOfficeResult']['dailyBoxOfficeList']
movies = []
for movie in movie_list:
    movieCode = movie['movieCd']
    movieName = movie['movieNm']
    movies.append((movieCode, movieName))

# print(movies)


# TMDb api
lang ='ko-KR'
TMDb_key = 'f790c6911bd5abe1dd9098d76849459f'
poster_base_url= 'https://image.tmdb.org/t/p/w500/'
discover_url = f'https://api.themoviedb.org/3/discover/movie?api_key={TMDb_key}&language={lang}&sort_by=popularity.desc&include_adult=false&include_video=false&page=1'
print(discover_url)
json_data = requests.get(discover_url).json()
movies = json_data['results']
movies_list = []
genre = f'https://api.themoviedb.org/3/genre/movie/list?api_key={TMDb_key}&language=ko-KR&sort_by=popularity.desc&include_adult=false&include_video=false&page=1'
print(genre)
# pp(json_data)

for idx, m in enumerate(movies):
    if type(m) == tuple:
        break
    m_image = m['poster_path']
    m_title = m['title']
    m_overview = m['overview']
    m_score = m['vote_average']
    poster_url = f'{poster_base_url}{m_image}'
    movies_list.append((poster_url, m_title, m_score, m_overview))
# pp(movies_list)