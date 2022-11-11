rut_sin_dv = input('Ingresa tu RUT sin puntos ni dígito verificador: ')
# Ej 12345678

serie_inicial = [2, 3, 4, 5, 6, 7]
numero_a_multiplicar = rut_sin_dv[::-1]

multiplicaciones = []
i_serie = 0

for numero_invertido in numero_a_multiplicar:
    digito = int(serie_inicial[i_serie])
    multiplicacion = int(numero_invertido) * digito
    multiplicaciones.append(multiplicacion)

    i_serie += 1
    if i_serie > len(serie_inicial) - 1:
        i_serie = 0

suma_multiplicaciones = sum(multiplicaciones)
modulo_once = suma_multiplicaciones % 11
dv = 11 - modulo_once

if dv == 10:
    dv = 'K'

elif dv == 11:
    dv = 0

else:
    pass

print(f'Su digito verificador es {dv}')
