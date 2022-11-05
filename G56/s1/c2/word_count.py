import sys

ruta_archivo_texto = sys.argv[1]

with open(ruta_archivo_texto, 'r') as file:
    texto = file.read()

texto_separado_en_caracteres = list(texto)
caracteres_unicos_texto = set(texto)
print(f'El número de caracteres distintos es: {len(caracteres_unicos_texto)}')

palabras_separadas = texto.split(' ')
palabras_unicas = set(palabras_separadas)

print(f'El número de palabras distintas es: {len(palabras_unicas)}')
