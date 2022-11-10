rut_sin_dv = input('Ingresa tu RUT sin puntos ni dígito verificador: ')
# Ej 12345678

serie_inicial = rut_sin_dv[1:-1]
numero_a_multiplicar = rut_sin_dv[::-1]
print(serie_inicial)
print(numero_a_multiplicar)

multiplicaciones = []
i_serie = 0

for numero_invertido in numero_a_multiplicar:
    digito = int(serie_inicial[i_serie])
    multiplicacion = int(numero_invertido) * digito
    multiplicaciones.append(multiplicacion)

    i_serie += 1
    if i_serie > len(serie_inicial) - 1:
        i_serie = 0

print(multiplicaciones)

