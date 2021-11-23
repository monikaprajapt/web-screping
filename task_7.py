# import json 
# from bs4 import BeautifulSoup
# # from task__5 import get_movies_list_details
# file4=open("my_file_5.json","r")
# h=json.load(file4)
# def analyse_movies_directors(h):
#     list=[]
#     for i in h:
#         if i["Director:"]not in list:
#             list.append(i["Director:"])
#             print(list)
    
#             # dict8={}
#             # list9=[]
#             # for k in list:
#             #     i=0
#             #     count=0
#             #     while i<len(h):
#             #         if k==h[i]["Director:"]:
#             #             count+=1
#             #         i+=1
#             #     dict8.update({k:count})
#             # list9.append(dict8)
#             # with open("task_7.json","w")as file:
#             #     json.dump(dict8,file,indent=4)
#             # return dict8
# analyse_movies_directors(h) 






import json 
from bs4 import BeautifulSoup
# from task__5 import get_movies_list_details
file4=open("my_file_5.json","r")
h=json.load(file4)
def analyse_movies_directors(h):
    list=[]
    list2=[]
    for i in h:
        # if i["Director:"]not in list:
        list.append(i["Director:"])
    # print(list)
    for j in list:
        if j not in list2:
            list2.append(j)
    print(list2)
    list3=[]
    for k in list2:
        c=0
        for l in list:
            if k==l:
                c=c+1
        list3.append(c)
    print(list3)
    dic={}
    for r in range(len(list2)):
        dic[list2[r]]=list3[r]
    print(dic)
    with open("task__7","w")as file:
     json.dump(dic,file,indent=4)
analyse_movies_directors(h) 
