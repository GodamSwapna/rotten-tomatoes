import os
import json
from bs4 import BeautifulSoup

with open("task5.json","r") as file:
    x=json.load(file)

def analyse_language_and_directors(movies_list):
    movies_dic={}
    for movies in movies_list:
        for director in movies["Director:"]:
            movies_dic[director]={}
    for i in range(len(movies_list)):
        for Director in movies_dic:
            if Director in movies_list[i]["Director:"]:
                for language in movies_list[i]["Language"]:
                    movies_dic[Director][language]=0
    for i in range(len(movies_list)):
        for Director in movies_dic:
            if Director in movies_list[i]["Director:"]:
                for language in movies_list[i]["Language"]:
                    movies_dic[Director][language]+=1
    with open("task10.json","w") as f:
        json.dump(movies_dic,f,indent=4)
    return movies_dic
analyse_language_and_directors(x)