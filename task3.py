from task1 import adventure_movie
import json
des=adventure_movie()


# task2=(group_by_year(monika))
def group_by_decade(movies):
    moviedec1={}
    list=[]
    for i in movies:
        mod=i["Year"]%10
        decade=i["Year"]-mod
        if decade not in list:
            list.append(decade)
    list.sort()
    for index in list:
        moviedec=[]
        for x in movies:
            if x["Year"]>=index and x["Year"]<=index+10:
                moviedec.append(x)
                moviedec1[index]=moviedec
                with open("task_3.json","w")as file1:
                    json.dump(moviedec1,file1,indent=3)
group_by_decade(des)
          