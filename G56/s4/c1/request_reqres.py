import requests
import json

url = 'https://reqres.in/api/users'

response = requests.request('GET', url=url)

print(json.dumps(json.loads(response.text), indent=1))

'''
De este print se puede ver que la base de datos contiene 12 usuarios
contenido en 2 páginas. Por lo tanto, para obtener todos los usuarios hay
que hacer 2 requests, uno para cada página de la API.
'''

url_1 = 'https://reqres.in/api/users?page=1'
url_2 = 'https://reqres.in/api/users?page=2'

response_1 = requests.request('GET', url=url_1)
response_2 = requests.request('GET', url=url_2)

users_data = [response_1, response_2]
for usuario in users_data:
    print(json.dumps(json.loads(usuario.text), indent=1))
