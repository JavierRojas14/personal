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
    preguntas_dificultad = p.pool_preguntas[dificultad]
    
    # usar opciones desde ambiente global
    global opciones
    # escoger una pregunta
    opciones_disponibles = opciones[dificultad]
    indice_elegido = random.randrange((len(opciones_disponibles)))
    n_elegido = opciones_disponibles[indice_elegido]
    # eliminarla del ambiente global para no escogerla de nuevo
    opciones[dificultad].pop(indice_elegido)
    
    # escoger enunciado y alternativas mezcladas
    llave_pregunta = list(preguntas_dificultad.keys())[n_elegido - 1]
    pregunta = preguntas_dificultad[llave_pregunta]
    alternativas = shuffle_alt(pregunta)
    
    
    return pregunta['enunciado'], alternativas

if __name__ == '__main__':
    # si ejecuto el programa, las preguntas cambian de orden, pero nunca debieran repetirse
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}\n')
    
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}\n')
    
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}\n')