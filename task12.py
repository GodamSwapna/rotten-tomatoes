import json
from bs4 import BeautifulSoup
import requests
# movieurl="https://www.rottentomatoes.com/m/toy_story_4"
# movieName="toy_story_4"
def scrape_movie_cast(movie_caste_url):
    url=requests.get(movie_caste_url)
    # print(url)
    data=BeautifulSoup(url.text,"html.parser")
    mainDiv=data.find("div",class_="castSection")
    # print(mainDiv)
    castDiv= mainDiv.find_all("div",class_="media-body")
    link=mainDiv.find_all("a",class_="unstyled articleLink")
    # print(link)te
    for l in link:
        a=l.text.split()
        print(a)
    dict1={}
    list1=[]
    for i in castDiv:
        a=i.span.text.split()

        j= a[0].replace(",","").strip()
        k= a[1].replace(",","").strip()
        # print(k)
        h=j+" "+ k
        list1.append(h)
    dict1["rt_id"]=list1
    # print(dict1)
    with open("task12.json","w")as f:
        json.dump(dict1,f,indent=4)
    return dict1
movieurl="https://www.rottentomatoes.com/m/toy_story_4"
scrape_movie_cast(movieurl)

# def scrape_movie_cast(movie_caste_url):
#     pass
# scrape_movie_cast()