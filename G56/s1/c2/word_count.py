import sys

ruta_archivo_texto = sys.argv[1]

with open(ruta_archivo_texto, 'r') as file:
    texto = file.read()

texto_separado_en_caracteres = list(texto)
caracteres_unicos_texto = set(texto)
cantidad_caracteres_unicos_texto = len(caracteres_unicos_texto)

palabras_separadas = texto.split(' ')
cantidad_palabras_separadas = len(palabras_separadas)

print(
    f'El número de caracteres distintos es: {cantidad_caracteres_unicos_texto}')
print(f'El número de palabras distintas es: {cantidad_palabras_separadas}')
