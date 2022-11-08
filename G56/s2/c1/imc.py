'''
Este programa asume que el input de peso y altura son números int.
'''

import sys

peso = int(sys.argv[1])
altura_en_cm = int(sys.argv[2])

altura_en_m = altura_en_cm / 100

imc = round(peso/(altura_en_m ** 2), 2)

print(f'Su IMC es {imc}')
