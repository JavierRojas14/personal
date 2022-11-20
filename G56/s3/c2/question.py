import preguntas as p
import random
from shuffle import shuffle_alt

# Opciones dadas para escoger.
###############################################
opciones = {'basicas': [1,2,3],
            'intermedias': [1,2,3],
            'avanzadas': [1,2,3]}
###############################################

def choose_q(dificultad):
    #escoger preguntas por dificultad
    pregunta_escogida = preguntas[dificultad]
    print(preguntas)
    
    # usar opciones desde ambiente global
    global opciones
    # escoger una pregunta
    opciones_disponibles = opciones[dificultad]
    n_elegido = random.randrange((len(opciones_disponibles)))
    print(n_elegido)
    # eliminarla del ambiente global para no escogerla de nuevo
    opciones[dificultad].pop(n_elegido)
    print(opciones)
    
    
    # escoger enunciado y alternativas mezcladas
    llave_pregunta = preguntas.keys()[n_elegido]
    pregunta = preguntas[llave_pregunta]
    alternativas = shuffle_alt(pregunta['alternativas'])
    
    
    return pregunta['enunciado'], alternativas

if __name__ == '__main__':
    # si ejecuto el programa, las preguntas cambian de orden, pero nunca debieran repetirse
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')