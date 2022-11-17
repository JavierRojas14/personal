def identificar_vel_sobre_promedio(lista_velocidades):
    suma_velocidades = sum(lista_velocidades)
    total_elementos = len(lista_velocidades)

    promedio_velocidad = suma_velocidades / total_elementos

    indices_sobre_el_promedio = []
    for i, dato in enumerate(lista_velocidades):
        if dato > promedio_velocidad:
            indices_sobre_el_promedio.append(i)

    print(indices_sobre_el_promedio)


velocidad = [25, 12, 19, 16, 11, 11, 24, 1,
             14, 14, 16, 10, 6, 23, 13, 25, 4, 19,
             14, 20, 18, 9, 18, 4, 18, 1, 3, 4, 2,
             14, 23, 19, 23, 9, 18, 20, 22, 14, 1,
             10, 5, 23, 3, 5, 9, 5, 3, 12, 20, 5,
             11, 10, 18, 10, 14, 5, 23, 20, 23, 21]

identificar_vel_sobre_promedio(velocidad)
