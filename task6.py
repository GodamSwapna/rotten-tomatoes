import json 
from task5 import get_movie_list1_det

with open("task5.json","r") as f:
    data=json.load(f)
    # print(data)


def  analyse_movies_language(movies_list):
    dic={}
    count1=0
    count2=0
    for x in movies_list:
        for y in x["Language"]:
            if y=="English":
                count1+=1
            if y=="Kingdom)":
                count2+=1
        dic["English"]=count1
        dic["Kingdom"]=count2
    return dic
print(analyse_movies_language(data))