from bs4 import BeautifulSoup
import json
import requests 
from pprint import pprint
from task1 import adventure_movie
import os,time
import random

scraped=adventure_movie()
a=[]
def scrape_movie_details(link):
    print(link)
    name=link[33:]
    if os.path.exists(name+".json")==True:
        with open(name+".json", 'r') as file:
            data=file.read()
            print(json.loads(data))   
    else:
        b={}
        url=requests.get(link)
        soup=BeautifulSoup(url.text,"html.parser")
        b["movie name"]=soup.find("h1").text
        main=soup.find("div",class_="panel-body content_body")
        x=main.find("ul",class_="content-meta info")
        y=x.find_all("li",class_="meta-row clearfix")
        for i in y:
            b[i.find("div",class_="meta-label subtle").text]=" ".join(i.find("div",class_="meta-value").text.split())
        a.append(b)
        with open(name+".json","w")as file:
            json.dump(a,file,indent=4)
        print(a)
        return a
scrape_movie_details("https://www.rottentomatoes.com/m/doctor_strange_2016")
