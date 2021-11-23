# import json 
# from bs4 import BeautifulSoup
# import requests
# from task__5 import t5

# def analyse_movies_language(movies) 
                
#  

import json
def  analyse_movies_language():
    file4=open("my_file_5.json","r")
    h=json.load(file4)
    # print(y)
    list=[]
    for i in h:
        # print(y)
        # print(i["Original Language"])
        if i["Original Language:"]not in list:
            list.append(i["Original Language:"])
            print(list)
            dict8={}
            list9=[]
            for k in list9:
                i=0
                count=0
                while i<len(h):
                    if k==h[i]["Original Language:"]:
                        count+=1
                    i+=1
                dict8.update({k:count})
            list9.append(dict8)
            with open("task_6.json","w")as file:
                json.dump(dict8,file,indent=4)
            return dict8
analyse_movies_language()
