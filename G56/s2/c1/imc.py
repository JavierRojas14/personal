'''
Este programa asume que el input de peso y altura son números int.
'''

import sys

peso = int(sys.argv[1])
altura_en_cm = int(sys.argv[2])

altura_en_m = altura_en_cm / 100

imc = round(peso/(altura_en_m ** 2), 2)

if imc < 18.5:
    clasificacion = 'Bajo Peso'

elif imc >= 18.5 and imc < 25:
    clasificacion = 'Adecuado'

elif imc >= 25 and imc < 30:
    clasificacion = 'Sobrepeso'

elif imc >= 30 and imc < 35:
    clasificacion = 'Obesidad Grado I'

elif imc >= 35 and imc < 40:
    clasificacion = 'Obesidad Grado II'

elif imc > 40:
    clasificacion = 'Obesidad Grado III'

print(f'Su IMC es {imc}')
print(f'La clasificación OMS es {clasificacion}')
