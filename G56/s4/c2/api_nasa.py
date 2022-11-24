import requests
import json


def pretty_print_request(respuesta):
    print(json.dumps(json.loads(respuesta.text), indent=1))

def build_web_page(lista_urls):

    li_items = []
    lista_urls.append('soy')
    for url in lista_urls:
        objeto_li = f'  <li><img src="{url}"></li>'
        li_items.append(objeto_li)
    
    li_items_str = '\n'.join(li_items)


    documento = f'''
    <html>
    <head>
    </head>
    <body>
    <ul>
    {li_items_str}
    </ul>
    </body>
    </head>
    </html>
    '''
    print(documento)


token = 'He6gOY5Zhgh8nSzdGHEhI9st5tndoP5XQtMpswwN'

url = f'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/latest_photos?api_key={token}'
response = requests.request('GET', url=url)
pretty_print_request(response)


diccionario_respuesta = json.loads(response.text)
ultimas_fotos = diccionario_respuesta['latest_photos']
ultimas_fotos = ultimas_fotos[:25]

lista_urls = []
for fotos in diccionario_respuesta['latest_photos']:
    lista_urls.append(fotos['img_src'])

print(lista_urls)

build_web_page(lista_urls=lista_urls)