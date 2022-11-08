import sys
import random

decisiones = ['piedra', 'papel', 'tijera']

decision_usario = sys.argv[1]
decision_computadora = random.choice(decisiones)

print(f'Tu jugaste {decision_usario}')
print(f'Computador jugó {decision_computadora}')

decision_usario = decision_usario.lower()

if decision_usario == 'piedra':
    if decision_computadora == 'piedra':
        print('Hubo un empate!!')

    elif decision_computadora == 'papel':
        print('Perdiste :(')

    elif decision_computadora == 'tijera':
        print('Ganaste!!')

elif decision_usario == 'papel':
    if decision_computadora == 'piedra':
        print('Ganaste!!')

    elif decision_computadora == 'papel':
        print('Hubo un empate!!')

    elif decision_computadora == 'tijera':
        print('Perdiste :(')

elif decision_usario == 'tijera':
    if decision_computadora == 'piedra':
        print('Perdiste :(')

    elif decision_computadora == 'papel':
        print('Ganaste!!')

    elif decision_computadora == 'tijera':
        print('Hubo un empate!!')

else:
    print('Arguemento inválido: Debe ser piedra, papel o tijera')
