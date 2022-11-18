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


print(factorial(5))
print(productoria([3, 6, 4, 2, 8]))
