import sys

precios = {'Notebook': 700000,
           'Teclado': 25000,
           'Mouse': 12000,
           'Monitor': 250000,
           'Escritorio': 135000,
           'Tarjeta de Video': 1500000}

def filtrar_por_umbral(umbral, tipo='mayor'):
    if tipo == 'mayor':
        filtrados = {llave: valor for llave, valor in precios.items() if valor >= umbral}
        articulos = list(filtrados.keys())
        print(f'Los productos mayores al umbral son: {", ".join(articulos)}')




umbral = int(sys.argv[1])
filtrar_por_umbral(umbral)