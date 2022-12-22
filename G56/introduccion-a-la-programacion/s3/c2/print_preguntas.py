import preguntas as p

def print_pregunta(enunciado, alternativas):
    
    # Imprimir enunciado y alternativas
    ###############################################################
    print(f'{enunciado[0]} \n')
    diccionario_letras = {0: 'A', 1: 'B', 2: 'C', 3: 'D'}

    for i, alternativa in enumerate(alternativas):
        print(f'{diccionario_letras[i]}. {alternativa[0]}')
    
    
    
    
    ###############################################################
        
if __name__ == '__main__':
    # Las preguntas y alternativas deben mostrarse según lo indicado
    pregunta = p.pool_preguntas['basicas']['pregunta_1']
    print_pregunta(pregunta['enunciado'],pregunta['alternativas'])
    
    # Enunciado básico 1

    # A. alt_1
    # B. alt_2
    # C. alt_3
    # D. alt_4