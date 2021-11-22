from bs4 import BeautifulSoup
import json
import pprint

def load_data():
    with open("moviesdata.json","r") as f:
        data=json.load(f)
    return data

def group_of_years(movies):
    list1=[]
    for v in movies:
        year=v["Year"]
        if year not in list1:
            list1.append(year)
    dic={j:[]for j in list1}
    for values in movies:
        year=values["Year"]
        for x in dic:
            if str(x)==str(year) and values not in dic[x]:
                dic[x].append(values)
    with open("Group_of_years.json","w") as file:
        json.dump(dic,file,indent=2)
m=load_data()
group_of_years(m)
