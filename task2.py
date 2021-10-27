
from task1 import adventure_movie
monika=adventure_movie()
import pprint
import json
def group_of_year(movies):
    years=[]
    for i in movies:
        year=i["Year"]
        if year not in years:
            years.append(year)
    d={}
    for k in years:
        d[k]=[]
        for i in movies:
                year=i['Year']
                if k==year:
                    d[k].append(i)
    with open("monika.json","w")as file:
            json.dump(d,file,indent=4)
    return d
pprint.pprint(group_of_year(monika))





     


    