print('Bienvenido al calculador de utilidades! En este caso, también calcularemos la razón con el año anterior! \n\n'
      'Debes ingresar el precio de suscripción, numero de usuarios y gastos totales.\n'
      'EL PROGRAMA SÓLO FUNCIONARÁ SI ES QUE SE INGRESAN VALORES NUMÉRICOS.\n'
      'SI SE INGRESAN VALORES NO NUMÉRICOS, ES ESPERABLE QUE EL PROGRAMA FALLE.\n\n')

precio_suscripcion = input('¿Cuál es el precio de suscripción?: ')
numero_usuarios = input('¿Cuál es el número de usuarios?: ')
gasto_total = input('¿Cuál es el gasto total?: ')
utilidades_año_anterior = input('¿Cuáles son las utilidades del año anterior?: ')

precio_suscripcion = int(precio_suscripcion)
numero_usuarios = int(numero_usuarios)
gasto_total = int(gasto_total)
utilidades_año_anterior = int(utilidades_año_anterior)

utilidades_actuales = (precio_suscripcion * numero_usuarios) - gasto_total
razon_año_anterior = utilidades_actuales / utilidades_año_anterior

print(f'Tus utilidades son: {utilidades_actuales}')
print(f'Además, la razón de utilidades con el año anterior es de {razon_año_anterior:.2f}')
