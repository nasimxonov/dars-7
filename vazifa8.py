import json

with open('malumot.json', 'r') as file:
    
    a = json.load(file)

a['firstname'] = input("Ismizi kiriting: ")

with open('malumot.json', 'w') as file:

    json.dump(a, file, indent=4)
