import json
# from bs4 import BeautifulSoup
# from task__5  import get_movies_list_details
file4=open("my_file_5.json","r")
h=json.load(file4)
def analyse_movies_directors(h):
    list=[]
    list2=[]
    for i in h:
        a=i["Genre:"].split()
        for l in a:
            if l[-1]==",":
                # print(l)
                l=l[:-1]
                # print(l)
            list.append(l)

    # print(list)
    for i in list:
        if i not in list2:
            list2.append(i)
    # print(list2)
    dic={}
    for i in (list2):
        count=0
        k=0
        while k <len(list):
            if i==list[k]:
                count+=1
            k+=1
        dic.update({i:count})
    with open("task__11.json","w")as file:
     json.dump(dic,file,indent=4)
analyse_movies_directors(h) 
