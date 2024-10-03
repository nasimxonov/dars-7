import json

from pprint import pprint as print


with open("nimadir.json","r+") as file:
    
    str_data = file.read()

    data = json.loads(str_data)

    n = list(filter(lambda g : g['yosh'] > 30, data))


print(n)

