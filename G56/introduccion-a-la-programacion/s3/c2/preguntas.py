preguntas_basicas = {
    'pregunta_1': {'enunciado':['¿Cuánto es 1 + 1?'],
    'alternativas': [['1', 0], 
                     ['2', 1], 
                     ['3', 0], 
                     ['4', 0]]},
    'pregunta_2': {'enunciado':['¿Cuánto es 2 + 1?'],
    'alternativas': [['3', 1], 
                     ['49', 0], 
                     ['soy', 0], 
                     ['asd', 0]]},
    
'pregunta_3': {'enunciado':['¿De qué color es el cielo?'],
    'alternativas': [['Azul', 1], 
                     ['Verde', 0], 
                     ['Morado', 0], 
                     ['Plata', 0]]}
}

preguntas_intermedias = {
    'pregunta_1': {'enunciado':['La refracción de la luz consiste en: '],
    'alternativas': [['Cómo se comporta la luz cuando choca con una superficie', 0], 
                     ['La energía que lleva la luz', 0], 
                     ['Las longitudes de onda que componen la luz', 0], 
                     ['El cambio de ángulo de la luz al entrar a otro medio', 1]]},

    'pregunta_2': {'enunciado':['¿De qué color es el cielo?'],
    'alternativas': [['Azul', 0], 
                     ['Celeste', 1], 
                     ['Azul-marino', 0], 
                     ['Acuamarino', 0]]},
    
'pregunta_3': {'enunciado':['¿Cuánto es la hipotenusa de un triangulo 1x1?'],
    'alternativas': [['sqrt(2)', 1], 
                     ['2', 0], 
                     ['raiz cubica de 2', 0], 
                     ['4', 0]]}
}

preguntas_avanzadas = {
    'pregunta_1': {'enunciado':['Enunciado avanzado 1'],
    'alternativas': [['alt_1', 0], 
                     ['alt_2', 1], 
                     ['alt_3', 0], 
                     ['alt_4', 0]]},
    'pregunta_2': {'enunciado':['Enunciado avanzado 2'],
    'alternativas': [['alt_1', 0], 
                     ['alt_2', 1], 
                     ['alt_3', 0], 
                     ['alt_4', 0]]},
    
'pregunta_3': {'enunciado':['Enunciado avanzado 3'],
    'alternativas': [['alt_1', 0], 
                     ['alt_2', 1], 
                     ['alt_3', 0], 
                     ['alt_4', 0]]}
}

pool_preguntas = {'basicas': preguntas_basicas,
                  'intermedias': preguntas_intermedias,
                  'avanzadas': preguntas_avanzadas}