import requests
from bs4 import BeautifulSoup
import csv

soup_objects = []

URL='https://movie.naver.com/movie/running/current.nhn'
response = requests.get(URL)

soup = BeautifulSoup(response.text, 'html.parser')


movie_list = soup.select{'#content > .article > .obj_section >.lst_wrap > ul > li'}

for movie in movie_list:
    a_tag = movie.select_one('dl.lst_dsc > dt > a')
    movie_title = a_tag.get_text()
    movie_code = a_tag['href'].split('=')[-1]

    movie_data = {
        'title' : movie_title, 
        'code' : movie_code
        }
        
    print(movie_title, movie_code)
    
    # with open('naver_movie.csv','a',newline='',encoding='utf-8-sig') as csvfile:
       # fieldname = ['title', 'link']
       # csvwriter = csv.DictWriter(csvfile, fieldname)
       # csvwriter.writerow(data)

