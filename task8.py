import requests
import json
import os
from task1 import scrape_top_list
from task4 import scrape_movie_details
movie = scrape_top_list()

def get_movie_lists_details():
    movie_list = []
    for i in movie: 
        # print(i["name"])    
        path="/home/dell/Desktop/rosteb and tomatos/all_movies"+i["name"]+".text"

        if os.path.exists(path):
            pass
        else:
            # create=open("/home/dell/Desktop/rosteb and tomatos/all_movies"+i["name"]+".text","w")
            create=open(i["name"]+".text","w")
            # url=open(create,"x")
            # print(create)
            url=requests.get(i["Url"])
            create1=create.write(url.text)
            print(create1)
            create.close()
    with open("task8.json","w+") as file5:
        json.dump(movie_list,file5,indent=4)
get_movie_lists_details()