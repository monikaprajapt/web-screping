import json
import pprint


with open("my_file_5.json","r") as f:
    data1=json.load(f)
    # print(data1)

def language_and_directores(movies_list):
    DirectoresDict={}
    for movies in movies_list:
        # print(movies)
        for Director in movies:
            # print(Director)
            if Director=="Director:":
                DirectoresDict[movies[Director]]={}
                print(DirectoresDict)
    for i in range(len(movies_list)):
        # print(i)
        for Director in DirectoresDict:
            # print(Director)
            if Director in movies_list[i][ "Director:"]:
                for language in movies_list[i]:
                    if language=="Original Language:":
                        a=movies_list[i]["Original Language:"]
                        DirectoresDict[Director][a]=0
    for i in range(len(movies_list)):
        for Director in DirectoresDict:
            if Director in movies_list[i][ "Director:"]:
                for language in movies_list[i]:
                    if language=="Original Language:":
                        for l in DirectoresDict[Director]:
                            DirectoresDict[Director][l]+=1
    return DirectoresDict


Director_language=language_and_directores(data1)
with open("task10.json","w") as f:
    json.dump(Director_language,f,indent=4)


pprint.pprint(Director_language)



