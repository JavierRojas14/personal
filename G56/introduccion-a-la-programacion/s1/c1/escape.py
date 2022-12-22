import math

print('Bienvenido al programa para calcular la velocidad de escape!\n')
print('El programa solamente funcionará si se ingresan valores numéricos'
      ' en los siguientes campos.\n')

radio = float(input('Ingrese el radio del planeta en METROS: '))
gravedad = float(input('Ingrese la constante gravitacional en METROS/S^2: '))

velocidad_de_escape = math.sqrt(2 * radio * gravedad)

print(f'La velocidad de escape es: {velocidad_de_escape} METROS/S')
