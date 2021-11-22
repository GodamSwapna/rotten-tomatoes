import requests
from bs4 import BeautifulSoup
import json

# url_link=requests.get("https://www.rottentomatoes.com/top/bestofrt/top_100_animation_movies/")
# movie_name=BeautifulSoup(url_link.text,"html.parser")
# def Store(filename,top_movies):
#     with open(filename,"w") as f:
#         json.dump(top_movies,f,indent=4)
def scrape_top_list():
    url_link=requests.get("https://www.rottentomatoes.com/top/bestofrt/top_100_animation_movies/")
    movie_name=BeautifulSoup(url_link.text,"html.parser")
    main_div=movie_name.find('div',class_="body_main container")
    table=main_div.find('table',class_='table')
    trs=table.find_all('tr')
    movie_rank=[]
    movie_name=["/home/dell/Desktop/rosteb and tomatos/all_movies"]
    year_of_release=[]
    movie_rating=[]
    movie_urls=[]
    for tr in trs:
        position=tr.find_all("td")
        for i in position:
            rank=tr.find("td",class_="bold").get_text()[:-1]
            if rank!="":
                movie_rank.append(int(rank))
        
            title=tr.find('a',class_="unstyled articleLink")["href"][3:]
            movie_name.append(str(title))
            
            year=tr.find("a", class_="unstyled articleLink").get_text()[-5:-1]
            year_of_release.append(int(year))

            rating=tr.find("span", class_="tMeterScore").get_text()[:-1]
            movie_rating.append(float(rating))

            link=tr.find("a", class_="unstyled articleLink")["href"]
            movie_urls.append(str("https://www.rottentomatoes.com"+link))
    top_movies=[]
    for i in range(0,len(movie_rank)):
        details={"name":'',"Year":"","Position":"","Url":"","Rating":""}   
    
        details["Position"]=int(movie_rank[i])
        details["name"]=str(movie_name[i])
        details["Url"]=str(movie_urls[i])
        details["Rating"]=float(movie_rating[i])
        details["Year"]=year_of_release[i]
        if details not in top_movies:
            top_movies.append(details)
    with open("moviesdata.json","w") as f:
        json.dump(top_movies,f,indent=4)
    return top_movies
scrape_top_list()