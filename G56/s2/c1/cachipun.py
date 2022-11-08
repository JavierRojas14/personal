import sys
import random

decisiones = ['piedra', 'papel', 'tijera']

decision_usario = sys.argv[1]
decision_computadora = random.choice(decisiones)

print(f'Tu jugaste {decision_usario}')
print(f'Computador jugó {decision_computadora}')
