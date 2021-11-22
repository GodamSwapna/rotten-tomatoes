
from bs4 import BeautifulSoup
import json

with open("moviesdata.json","r") as f:
    m=json.load(f)
def group_by_year(Movies):
    list1=[]
    for v in Movies:
        year=v["Year"]
        if year not in list1:
            list1.append(year)
    dic={j:[]for j in list1}
    for values in Movies:
        year=values["Year"]
        for x in dic:
            if str(x)==str(year):
                dic[x].append(values)
    return dic
# print(group_by_year(m))

def group_by_decade(movies):
    year_list=[]
    dic={}
    for value in movies:
        year=value%10
        index=value-year
        if index not in year_list:
            year_list.append(index)
    year_list.sort()
    for year in year_list:
        dic[year]=[]
    for x in dic:
        y=x+9
        for d in movies:
            if d>=x and d<=y:
                for data in movies[d]:
                    dic[x].append(data)
    with open("moviedec2.json","w") as file:
        json.dump(dic,file,indent=4)
data=group_by_year(m)
group_by_decade(data)