from bs4 import BeautifulSoup
import json
import requests
# import task12
from task12 import name
a=[]
def scrape_movie_details(link):
    cast=(name(link))
    b={}
    url=requests.get(link)
    soup=BeautifulSoup(url.text,"html.parser")
    b["movie name"]=soup.find("h1").text
    main=soup.find("div",class_="panel-body content_body")
    x=main.find("ul",class_="content-meta info")
    y=x.find_all("li",class_="meta-row clearfix")
    for i in y:
        b[i.find("div",class_="meta-label subtle").text]=i.find("div",class_="meta-value").text

    b["cast"]=cast
    with open("task13.json","w") as f:
        json.dump(b,f,indent=2)
    return b
    
        
scrape_movie_details("https://www.rottentomatoes.com/m/black_panther_2018")
