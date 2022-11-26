import requests
import json


def pretty_print_request(respuesta):
    print(json.dumps(json.loads(respuesta.text), indent=1))

def build_web_page(lista_urls):

    li_items = []
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
    return documento


token = 'He6gOY5Zhgh8nSzdGHEhI9st5tndoP5XQtMpswwN'

url = f'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/latest_photos?api_key={token}'
response = requests.request('GET', url=url)
pretty_print_request(response)


diccionario_respuesta = json.loads(response.text)
ultimas_fotos = diccionario_respuesta['latest_photos'][:25]
lista_urls = [fotos['img_src'] for fotos in ultimas_fotos]

web_page = build_web_page(lista_urls=lista_urls)

with open('index.html', 'w') as file:
    file.write(web_page)