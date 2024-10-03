import json

from pprint import pprint as print


with open("nimadir.json","r+") as file:
    
    str_data = file.read()

    data = json.loads(str_data)


    print(min(data, key=lambda i: i['yosh']))
    print(max(data, key=lambda i: i['yosh']))
