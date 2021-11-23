from bs4 import BeautifulSoup
import json
import requests
import pprint
a=[]
def scrape_movie_details(link):

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
    return a

# print(a)
print.pprint(scrape_movie_details("https://www.rottentomatoes.com/m/black_panther_2018"))
with open("task_4.json","w")as file:
    json.dump(a,file,indent=4)
scrape_movie_details("https://www.rottentomatoes.com/m/black_panther_2018")
