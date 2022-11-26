import requests
import json


def crear_website_pajaros(lista_pajaros):

    li_pajaros = []
    for pajaro in lista_pajaros:
        imagen = pajaro[0]
        nombre_espanol = pajaro[1]
        nombres_ingles = pajaro[2]
        objeto_li = f'  <li><img src="{imagen}"/> {nombre_espanol} - {nombres_ingles}</li>'
        li_pajaros.append(objeto_li)

    li_pajaros_str = '\n'.join(li_pajaros)

    documento = f'''
<html>
<head>
</head>
<body>
<ul>
{li_pajaros_str}
</ul>
</body>
</head>
</html>
'''
    return documento


url = 'https://aves.ninjas.cl/api/birds'

response = requests.request('GET', url=url)

objeto_respuesta = json.loads(response.text)

print(objeto_respuesta[0])
# Del print anterior se puede ver que la respuesta es una lista de diccionarios

print(list(objeto_respuesta[0].keys()))
# Cada diccionario tiene las llaves 'uid', 'name', 'images', '_links' y 'sort'

# La idea del programa es crear una página que tenga en formato lista
# cada uno de los pájaros, con una imágen, nombre en español e ingles.

# Por lo tanto, de cada pájaro hay que aislar ['images']['main'], ['name']['spanish']
# y ['name']['english']´´
info_pajaros = []
for pajaro in objeto_respuesta:
    imagen_pajaro = pajaro['images']['main']
    nombre_espanol = pajaro['name']['spanish']
    nombre_ingles = pajaro['name']['english']
    info_de_un_pajaro = [imagen_pajaro, nombre_espanol, nombre_ingles]
    info_pajaros.append(info_de_un_pajaro)

pagina_web = crear_website_pajaros(info_pajaros)
print(pagina_web)
