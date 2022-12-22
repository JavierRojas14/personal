import sys

conversor_sol_peruano = float(sys.argv[1])
conversor_peso_argentino = float(sys.argv[2])
conversor_dolar_americano = float(sys.argv[3])
dinero_chileno = float(sys.argv[4])

dinero_peruano = dinero_chileno * conversor_sol_peruano
dinero_argentino = dinero_chileno * conversor_peso_argentino
dinero_americano = dinero_chileno * conversor_dolar_americano

print(f'Los {dinero_chileno} pesos equivalen a:')
print(f'{dinero_peruano} Soles')
print(f'{dinero_argentino} Pesos Argentinos')
print(f'{dinero_americano} Dólares')