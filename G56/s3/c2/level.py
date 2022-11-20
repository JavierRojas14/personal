def choose_level(n_pregunta, p_level):
    
    # Construir lógica para escoger el nivel
    ##################################################
    if p_level == 1:
        if n_pregunta == 1:
            level = 'basicas'
        
        elif n_pregunta == 2:
            level = 'intermedias'
        
        elif n_pregunta >= 3:
            level = 'avanzadas'

    elif p_level == 2:
        if n_pregunta >= 1 and n_pregunta <= 2:
            level = 'basicas'
        
        elif n_pregunta >= 3 and n_pregunta <= 4:
            level = 'intermedias'
        
        elif n_pregunta >= 5:
            level = 'avanzadas'
        
    elif p_level == 3:
        if n_pregunta >= 1 and n_pregunta <= 3:
            level = 'basicas'
        
        elif n_pregunta >= 4 and n_pregunta <= 6:
            level = 'intermedias'
        
        elif n_pregunta >= 7:
            level = 'avanzadas'
    
    ##################################################
    
    return level

if __name__ == '__main__':
    # verificar resultados
    print(choose_level(2, 2)) # básicas
    print(choose_level(3, 2)) # intermedias
    print(choose_level(7, 2)) # avanzadas
    print(choose_level(4, 3)) # intermedias