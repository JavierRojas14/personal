import requests
import json

url = 'https://aves.ninjas.cl/api/birds'

response = requests.request('GET', url=url)

objeto_respuesta = json.loads(response.text)

print(diccionario_respuesta[0])
