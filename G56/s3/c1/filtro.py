import sys

precios = {'Notebook': 700000,
           'Teclado': 25000,
           'Mouse': 12000,
           'Monitor': 250000,
           'Escritorio': 135000,
           'Tarjeta de Video': 1500000}


def filtrar_por_umbral(umbral, tipo='mayor'):
    if tipo == 'mayor':
        filtrados = {llave: valor for llave, valor in precios.items() if valor > umbral}
        articulos = list(filtrados.keys())
        print(f'Los productos mayores al umbral son: {", ".join(articulos)}')

    elif tipo == 'menor':
        filtrados = {llave: valor for llave, valor in precios.items() if valor < umbral}
        articulos = list(filtrados.keys())
        print(f'Los productos menores al umbral son: {", ".join(articulos)}')

    else:
        print('Lo sentimos, no es una operación válida')


umbral = int(sys.argv[1])
if len(sys.argv) == 2:
    filtrar_por_umbral(umbral)

elif len(sys.argv) == 3:
    tipo_calculo = sys.argv[2]
    filtrar_por_umbral(umbral, tipo_calculo)
