import json
import requests
import random
import time
import os
from bs4 import BeautifulSoup
from task5 import get_movie_list1_det
from task1 import scrape_top_list

with open('task5.json','r') as f:
    a=json.load(f)
movie_data=a
for i in movie_data:
    random_sleep=random.randint(1,3)
    path=open('/home/dell/Desktop/Rotten and Tomatoas/9.txt'+str(i)+'.text','w')
    a=str(i)
    create=path.write(a)
    time.sleep(random_sleep)
    path.close()


