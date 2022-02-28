from bs4 import BeautifulSoup
import json
import requests
from task_13 import scrape_movie_details

def actor():
    with open("top_movie_1.json", 'r') as file:
        data=json.load(file)
    movie_url_list=[]
    for i in data:
        movie_url_list.append(i['Movie URL'])
    # print(movie_url_list)
    lis=[]
    for i in range(5):
        lis.append(scrape_movie_details(movie_url_list[i]))
        # print(lis)
    dict={}
    for i in lis:
        for j in i["cast"]:
            if j  not in dict:
                dict.update({j:[]})
    # print(dict)
    
    for i in dict:
        for j in lis:
            if i in j["cast"]:
                for k in j["cast"]:
                    if i==k:
                        continue
                    dict[i].append(k)
                    print(dict)
        
    with open('task14.json',  'w') as file:
        json.dump(dict, file, indent=4)
actor()