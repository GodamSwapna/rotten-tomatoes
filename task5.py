import json 
import requests
from bs4 import BeautifulSoup
from task4 import scrape_movie_details
from task1 import scrape_top_list
with open("moviesdata.json","r") as f:
    top_movies=json.load(f)

def get_movie_list1_det(movies_list):
    movies=[]
    for i in range(0,len(movies_list)):
        for key in movies_list[i]:
            if key=="Url":
                movies.append(scrape_movie_details(movies_list[i][key]))
    return movies
data=get_movie_list1_det(top_movies[::])

with open("task5.json","w") as f:
    json.dump(data,f,indent=4)