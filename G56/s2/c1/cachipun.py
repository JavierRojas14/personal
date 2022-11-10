import sys
import random

decisiones = ['piedra', 'papel', 'tijera']

decision_usuario = sys.argv[1]
print(f'Tu jugaste {decision_usuario}')

decision_usuario = decision_usuario.lower()

if decision_usuario in decisiones:
    decision_computadora = random.choice(decisiones)
    print(f'Computador jugó {decision_computadora}')

    if decision_usuario == 'piedra':
        if decision_computadora == 'piedra':
            print('Hubo un empate!!')

        elif decision_computadora == 'papel':
            print('Perdiste :(')

        elif decision_computadora == 'tijera':
            print('Ganaste!!')

    elif decision_usuario == 'papel':
        if decision_computadora == 'piedra':
            print('Ganaste!!')

        elif decision_computadora == 'papel':
            print('Hubo un empate!!')

        elif decision_computadora == 'tijera':
            print('Perdiste :(')

    elif decision_usuario == 'tijera':
        if decision_computadora == 'piedra':
            print('Perdiste :(')

        elif decision_computadora == 'papel':
            print('Ganaste!!')

        elif decision_computadora == 'tijera':
            print('Hubo un empate!!')

else:
    print('Arguemento inválido: Debe ser piedra, papel o tijera')
