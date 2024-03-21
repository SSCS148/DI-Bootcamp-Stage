# Read the file line by line
# Read only the 5th line of the file
# Read only the 5 first characters of the file
# Read all the file and return it as a list of strings. Then split each word
# Find out how many occurences of the names "Darth", "Luke" and "Lea" are in the file
# Append your first name at the end of the file
# Append "SkyWalker" next to each first name "Luke"

# f = open("namelist.txt","r")
# # for line in f:
# #     print(line)

# # print(f.read(3))
# # f.close()
# all_file = f.read()
# print(all_file)
# with open("namelist.txt") as file:
#     for line in file:
#         x = line.split()
    
# print(x)


# import requests

# # Exemple d'API REST
# api_url = "http://api.open-notify.org/iss-now.json"

# # Envoyer une requête GET à l'API
# response = requests.get(api_url)

# # Vérifier si la requête a réussi (code 200)
# if response.status_code == 200:
#     # Afficher les données récupérées
#     print(response.json(),"\n")
#     print(response.headers)
# else:
#     # Afficher un message d'erreur si la requête a échoué
#     print("Erreur lors de la requête à l'API:", response.status_code)



# import requests
# import json

# response = requests.get("http://api.open-notify.org/astros.json")

# # Vérifier si la requête a réussi (code 200)
# if response.status_code == 200:
#     # Charger les données JSON en tant qu'objet Python
#     data = response.json()
    
#     # Afficher les données JSON de manière ordonnée avec indentation
#     formatted_json = json.dumps(data, indent=4)
#     print(formatted_json)
# else:
#     # Afficher un message d'erreur si la requête a échoué
#     print("Erreur lors de la requête à l'API:", response.status_code)


# import requests
# import json
# response = requests.get("http://api.open-notify.org/astros.json")

# # Récupérer le contenu de la réponse HTTP sous forme de texte brut
# data = json.loads(response.text)
# format_doc = json.dumps(data, indent = 3)

# # Afficher le contenu
# print(format_doc)


import requests
import json

response = requests.get("https://api.chucknorris.io/jokes/random/")

if response.status_code == 200:
    data = response.json()
    # show_head = json.headers()
else:
    print("No")

print(data)