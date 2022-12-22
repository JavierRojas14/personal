print('Bienvenido al calculador de utilidades! \n\n'
      'Debes ingresar el precio de suscripción, numero de usuarios y gastos totales.\n'
      'EL PROGRAMA SÓLO FUNCIONARÁ SI ES QUE SE INGRESAN VALORES NUMÉRICOS ENTEROS.\n'
      'SI SE INGRESAN VALORES NO NUMÉRICOS ENTEROS, ES ESPERABLE QUE EL PROGRAMA FALLE.\n\n')

precio_suscripcion = int(input('¿Cuál es el precio de suscripción?: '))
numero_usuarios = int(input('¿Cuál es el número de usuarios?: '))
gasto_total = int(input('¿Cuál es el gasto total?: '))

utilidades = (precio_suscripcion * numero_usuarios) - gasto_total

print(f'Tus utilidades son: {utilidades}')
