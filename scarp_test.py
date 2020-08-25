import requests
import os
import sys
import urllib.request
import json

from pprint import pprint as pp

api_key = 'f790c6911bd5abe1dd9098d76849459f'

tmdbUrl = 'https://api.themoviedb.org/3/movie/299536/credits?api_key=f790c6911bd5abe1dd9098d76849459f&language=ko-kr'
castData = requests.get(tmdbUrl).json()
cname = castData['cast'][0]['name']


# 2) movie_obj와 Actor정보 등록하기
def en_to_kr(cname):
    papago_url = 'https://openapi.naver.com/v1/papago/detectLangs'
    client_id = 'DnpIALAz5nZRI_RUU4O_'
    clitent_secret = 'Kp1APx_Zt8'

    client_id = "DnpIALAz5nZRI_RUU4O_" # 개발자센터에서 발급받은 Client ID 값
    client_secret = "Kp1APx_Zt8" # 개발자센터에서 발급받은 Client Secret 값

    encText = urllib.parse.quote(cname)
    data = "source=en&target=ko&text=" + encText

    url = "https://openapi.naver.com/v1/papago/n2mt"

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        trans = json.loads(response_body.decode('utf-8'))['message']['result']['translatedText']
        return trans
    else:
        print("Error Code:" + rescode)
        return

def get_actors_and_directors(movie_id):
    global api_key
    credit_URL = f'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={api_key}&language=ko-kr'
    credit_data = requests.get(credit_URL).json()
    cast_data = credit_data['cast']
    crew_data = credit_data['crew']

    # casting
    cast_list = []
    for cast in cast_data:
        cast_list.append(en_to_kr(cast['name']))

    director_list = []
    # director
    for crew in crew_data:
        if crew['job'] == 'Director':
            director_list.append(en_to_kr(crew['name']))
    return {'cast_data':cast_list, 'directors': director_list}


movie_id = 299536
credit_data = get_actors_and_directors(movie_id)
pp(credit_data)

# for cname in cast_list:
#     print(en_to_kr(cname))