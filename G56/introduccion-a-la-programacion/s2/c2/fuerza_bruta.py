from string import ascii_lowercase

contraseña = input('Ingrese la contraseña: ').lower()

intentos = 0
for letra_contraseña in contraseña:
    for letra_abecedario in ascii_lowercase:
        intentos += 1
        if letra_abecedario == letra_contraseña:
            break

print(f'La contraseña fue forzada en {intentos} intentos')
