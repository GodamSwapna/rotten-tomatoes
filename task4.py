import json
# from os import XATTR_CREATE
import requests
from bs4 import BeautifulSoup

movieurl="https://www.rottentomatoes.com/m/toy_story_4"
moviename="toy_story_4"
     
def scrape_movie_details(movieurl):
    url=requests.get(movieurl)
    url_link=BeautifulSoup(url.text,"html.parser")
    dic={}
    title_div=url_link.find("div",class_="thumbnail-scoreboard-wrap")
    sub_div=title_div.find("score-board",class_="scoreboard")
    name=sub_div.find("h1",class_="scoreboard__title").get_text()
    dic["Name"]=str(name)
    main=url_link.find_all("li",class_="meta-row clearfix")
    for x in main:
        y=x.get_text().strip()
        data=y.split()
        # print(data)
        if data[0]=="Rating:":
            dic[data[0]]=data[1]
        elif data[0]=="Genre:":
            a=[]
            for y in data:
                if y!="Genre:":
                    a.append(y)
            dic["Genre"]=a
        elif data[0]=="Original":
            dic["Language"]=[data[-1]]
        elif data[0]=="Director:":
            dic[data[0]]=[data[1]+data[2]]
        if data[0]=="Runtime:":
            a=data[2][0]
            minuts=int(data[1][0])*60+int(a)
            dic["Runtime"]=minuts
    with open("task4.json","w") as f:
        json.dump(dic,f,indent=4)
    return dic
# scrape_movie_details(movieurl)
# def dump_data(data):
#     with open("task4.json","w") as f:
#         json.dump(data,f,indent=4)

# dump_data(movie_infor)

# movie_infor=scrape_movie_details(movieurl)
