import json
json_file = 'file.json'
with open ("file.json","r") as file:
    family = json.load(file)
print(json.dumps(family['children'], indent=4))

data['children']['favorite_color'] = "value to add"

with open ("file.json","w") as file:
    data = json.load(file)
    
