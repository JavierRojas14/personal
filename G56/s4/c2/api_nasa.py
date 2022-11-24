import requests
import json

def pretty_print_request(respuesta):
    print(json.dumps(json.loads(respuesta.text), indent=1))

token = 'He6gOY5Zhgh8nSzdGHEhI9st5tndoP5XQtMpswwN'

url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/latest_photos'
url_token = f'{url}?api_key={token}'

response = requests.request('GET', url=url_token)
pretty_print_request(response)