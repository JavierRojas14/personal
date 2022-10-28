recordatorios = [['2021-01-01', "11:00", "Levantarse y ejercitar"],
                 ['2021-05-01', "15:00", "No trabajar"],
                 ['2021-07-15', "13:00", "No hacer nada es feriado"],
                 ['2021-09-18', "16:00", "Ramadas"],
                 ['2021-12-25', "00:00", "Navidad"]]

primer_evento = ['2021-01-02', '06:00', 'Empezar el Año']
recordatorios.insert(2, primer_evento)

recordatorios[3][0] = '2021-07-16'

recordatorios.pop(1)

cena_navidad = ['2021-12-24', '22:00', 'Cena de Navidad']
cena_año_nuevo = ['2021-12-31', '22:00', 'Cena de Año Nuevo']

recordatorios.insert(-1, cena_navidad)
recordatorios.append(cena_año_nuevo)
# Output
print(recordatorios)
