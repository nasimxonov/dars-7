import json


user = {
    'id': 62936,
    'firstname': 'Nasimxonov',
    'lastname': 'Saidnurmuhammadulloxon',
    'age': 18
}
 
 
js = json.dumps(user, indent=4)
 

with open("malumot.json", "w") as outfile:
    outfile.write(js)