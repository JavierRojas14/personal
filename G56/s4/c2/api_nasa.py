import requests
import json


def pretty_print_request(respuesta):
    print(json.dumps(json.loads(respuesta.text), indent=1))


token = 'He6gOY5Zhgh8nSzdGHEhI9st5tndoP5XQtMpswwN'

url_25_fotos = f'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date=2016-12-27&api_key={token}'
response_25_fotos = requests.request('GET', url=url_25_fotos)
pretty_print_request(response_25_fotos)
