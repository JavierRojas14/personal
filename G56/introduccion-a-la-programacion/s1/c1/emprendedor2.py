print('Bienvenido al calculador de utilidades con usuarios Premium! \n\n'
      'Debes ingresar el precio de suscripción, numero de usuarios normales, '
      'numero de usuarios premium y gastos totales.\n'
      'EL PROGRAMA SÓLO FUNCIONARÁ SI ES QUE SE INGRESAN VALORES NUMÉRICOS ENTEROS.\n'
      'SI SE INGRESAN VALORES NO NUMÉRICOS ENTEROS, ES ESPERABLE QUE EL PROGRAMA FALLE.\n\n')

precio_suscripcion = int(input('¿Cuál es el precio de suscripción?: '))
numero_usuarios_normales = int(
    input('¿Cuál es el número de usuarios normales?: '))
numero_usuarios_premium = int(
    input('¿Cuál es el número de usuarios premium?: '))
gasto_total = int(input('¿Cuál es el gasto total?: '))

utilidades = (((precio_suscripcion * numero_usuarios_normales)
               + (precio_suscripcion * 1.5 * numero_usuarios_premium))
              - gasto_total)

print(f'Tus utilidades con los dos tipos de usaurios son: {utilidades}')
