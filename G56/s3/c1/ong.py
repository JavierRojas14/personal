def factorial(numero_a_calcular):
    resultado = 1
    for i in range(numero_a_calcular):
        resultado *= (i + 1)

    return resultado


def productoria(lista_numeros):
    resultado = 1
    for numero in lista_numeros:
        resultado *= numero

    return resultado


def calcular(**kwargs):
    for funcion, argumento in kwargs.items():
        if 'fact' in funcion:
            print(f'El factorial de {argumento} es {factorial(argumento)}')

        elif 'prod' in funcion:
            print(f'La productoria de {argumento} es {productoria(argumento)}')


calcular(fact_1=5, prod_1=[3, 6, 4, 2, 8], fact_2=6)
