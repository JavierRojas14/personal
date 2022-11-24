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

###############################################################################

nuevo_usuario = {
    'user': 'Ignacio',
    'job': 'Profesor'
}

created_user = requests.request('POST', url=url, params=nuevo_usuario)
print(created_user, created_user.text)

###########################################################################
'''
Del primer print se puede ver que no existe ningún usuario llamado morpheus en la
base de datos. Por lo tanto, se actualizará cualquier usuario que si exista. En este caso
un usuario con id = 2.
'''

url_actualizar = 'https://reqres.in/api/users/2'

actualizar = {
    "name": "morpheus",
    "residence": "zion"
}

updated_user = requests.request('PUT', url=url_actualizar, data=actualizar)
print(updated_user, updated_user.text)


#############################################################################
'''
Del primer print se puede ver que el usuario "Tracey" tiene un id = 6. Por lo tanto,
hay que seleccionar este id en la url.
'''

url_a_borrar = 'https://reqres.in/api/users/6'

delete_user = requests.request('DELETE', url=url_a_borrar)
print(delete_user, delete_user.text)
