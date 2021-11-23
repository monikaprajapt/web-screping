from bs4 import BeautifulSoup
from task1 import adventure_movie
import json
import requests
import pprint
screpped=adventure_movie()
# with open("top_movie_1.json","r")as file:
#     data=file.read()
#     a=json.loads(data)
def get_movies_list_details(movies):
    j=0
    list4=[]
    while j<len(movies):
        url=movies[j]["Movie URL"]
        x=requests.get(url)
        soup=BeautifulSoup(x.text,"html.parser")
        # main=soup.find("dev",class_="panel-body content_body")
        main=soup.find("ul",class_="content-meta info")
        all=main.find_all("li",class_="meta-row clearfix")
        my_dict={}
        # print(all)
        for i in all:
            my_dict[i.find("div",class_="meta-label subtle").text.strip()]=i.find("div",class_="meta-value").get_text().strip().replace("\n","")
            # alldeta=i.get_text()
            # print(alldeta,"allllll")
            # allvalue=i.find("div",class_="meta-value").get_text().strip().replace("\n")
            # title=soup.find("h1")
            # my_dict.update({alldeta:allvalue})
        list4.append(my_dict)
        print(my_dict)
        print(list4)
        j+=1
    with open("my_file_5.json","w")as f:
        json.dump(list4,f,indent=4)
    return list4
get_movies_list_details(screpped)
    
