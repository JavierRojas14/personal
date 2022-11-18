def factorial(numero_a_calcular):
    resultado = 1
    for i in range(numero_a_calcular):
        resultado *= (i + 1)
    
    return resultado

print(factorial(5))
