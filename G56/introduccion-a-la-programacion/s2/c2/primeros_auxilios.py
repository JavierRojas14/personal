print('Bienvenido al programa de primeros auxilios! A pesar de estar'
      'en una emergencia, le pedimos encarecidamente que responda solamente'
      'con SI o NO (indistinto de mayusculas y minusculas)\n\n')


responde_a_estimulos = input('¿El paciente responde a estimulos? ').upper()

if responde_a_estimulos == 'NO':
    print('Por favor, abra la vía aérea del paciente')
    respira = input('¿El paciente respira? ').upper()

    if respira == 'NO':
        print('Por favor, administrar 5 ventilaciones y llamar a ambulancia')
        llego_ambulancia = False

        while not llego_ambulancia:
            signos_de_vida = input(
                '¿El paciente presenta signos de vida? ').upper()

            if signos_de_vida == 'NO':
                print(
                    'Por favor, administre compresiones torácicas hasta que llegue la ambulancia')

            elif signos_de_vida == 'SI':
                print('Por favor, reevaluar la espera de la ambulancia')

            ha_llegado_la_ambulancia = input('¿LLegó la ambulancia? ').upper()

            if ha_llegado_la_ambulancia == 'NO':
                pass

            elif ha_llegado_la_ambulancia == 'SI':
                llego_ambulancia = True
                print('Muchas gracias por asistir al paciente!')

    elif respira == 'SI':
        print('Por favor, permitirle al paciente una posición de suficiente ventilación')

elif responde_a_estimulos == 'SI':
    print('Usted debe valorar la necesidad de llevarlo al hospital más cercano')
