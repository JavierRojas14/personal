¿Cómo escribir commits que tengan un significado?
¿Por qué los commits con significado son tan importantes?
¿Cuándo hacer un commit?

Un commit es como un snapshot. Se deben hacer comits cada vez que se hagan cambios importantes en el código. De esta forma, se puede ver una linea temporal del código.

Hacer buenos git commits habla de un buen colaborador.

Características de un buen commit:

1. Tiene un formato (sintaxis, puntuaciones, largo, uso de mayusculas/minùsculas) consistente y definido.
2. Tiene un contenido consistente y definido.
3. Tiene metadata para hacer referencia al commit.


# 7 Reglas para hacer un buen commit message

1. Separar el título del commit del cuerpo con una nueva linea (\n) o linea en blanco. Esto, sólo si es que se va a poner un cuerpo al commit.
  - El título del commit es el resumen del commmit. Debe tener menos de 50 carácteres.
  - El cuerpo del commit (si es que se incluye) puede tener una descripción mucho más detallada del commit.

2. El título debe tener hasta 50 carácteres (aunque es una flexible)
  - Si cuesta resumir el commit en 50 carácteres, significa que estas haciendo muchos commits. Hacer commits atómicos!

3. Empezar el título con una mayúscula.

4. Terminar el título sin un punto

5. Escribir el título en imperativo (como dando una órden)
  - Ej: Merge branch, clean your room, close the door, revert X, remove depracated methods.
  - Al principio es raro, pero el commit message debe poder unirse a la siguiente oración:
  "If applied, this commit will [commit message]".

6. Cada línea del cuerpo debe tener como máx 72 líneas.

7. El cuerpo debe explicar los "¿Qué se hizo en el commit?" "¿Por qué se hizo este commit?"

# Commits atómicos.

- Hacer un commit único para una tarea/arreglo
- SOLAMENTE HACER COMMITS CUANDO EL BLOQUE DE CÓDIGO ESTE LISTO.
- Si se modifican diversos archivos/carpetas/código, hacer commit de estos de forma agrupada cuando la tarea este lista.

What are two benefits of having well-written commit messages and a good commit history?

- Mejor capacidad de arreglar bugs
- Mejor capacidad de poder unir (mergear) características a código ya existente

How many characters should the subject line of your commit message be?

- Como regla flexible, menos de 50. Como regla rígida, menos de 72.


Plantilla de commit:
```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```