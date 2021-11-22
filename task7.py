import json 
from task5 import get_movie_list1_det 

with open("task5.json","r") as f:
    data=json.load(f)
    
def analyse_movies_directors(movies_list):
    movies=[]
    for i in range(0,len(movies_list)):
        movies.append(movies_list[i]["Director:"])
    # print(movies)
    list1=[]
    for i in movies:
        for j in i:
            list1.append(j)
    dic={}
    for x in list1:
        count=0
        for y in list1:
            if x==y:
                count+=1
        dic[x]=count
    return dic
data1=analyse_movies_directors(data)
with open("task7.json","w") as file:
    json.dump(data1,file,indent=4)