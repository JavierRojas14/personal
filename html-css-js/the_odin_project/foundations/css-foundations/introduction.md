# Selectores

**- Selector de todo:**

```
* {
    ...
}
```

**- Selector de elemento HTML. Por ejemplo, seleccionar los elementos div:**

```
div {
    ...
}

```

**- Selector de clases. Con un punto al inicio.**

```
.class {
    ...
}
```

**- Selector de id. Con un gato al principio.**

```
#id {
    ...
}
```

**- Agrupar elementos. Agrupandolos en una lista separada por coma:**

```
.class, elemento, #id {
    ...
}
```

**- Selección encadenada. Se hace seleccionando los elementos sin un espacio. Selecciona los elemento que solamente contengan todos los selectores:**

```
.subsection.header {
    ...
}
```
**Selecciona todos los elementos que tengan clase subsesction Y header.**

```
.subsection#preview {
    ...
}
```
**Selecciona todos los elementos que tengan clase subsection Y preview.**

**- Selección por descendencia:** Selecciona todos los elementos de la derecha, que tengan como ancestro al elemento de la izquierda.

```
.ancestor .contents {
    ...
}
```

Selecciona los elementos que tengan como clase "contents", y que sean descendientes de algún elemento con clase "ancestor". O, elegirá todos los elementos que tengan como clase "contents" que estén anidados dentro de un elemento con clase "ancestor".

# CSS Propertys:

Las más comunes:

## Color and Background - Color:

- color se utiliza para cambiar el color del texto
- background-color se utiliza para cambiar el color del fondo

## Tipografía:

- font-family: Puede ser un str, o una lista separada por comas de fuentes a utilizar. Es buena práctica utilizar una lista de fuentes separadas por coma, ya que así se tienen diversas opciones en caso de que alguna no esté disponible.

- font-size: Cambia el tamaño de la letra
- font-weight: Cambia lo negrita de la letra
- text-align: Alinea el texto que esta dentro de un elemento

## Image Height and Width

Si no se quiere perder las proporciones de la imágen original, se debe utilizar un height de **auto** y un width que se varia

```
img {
    height: auto;
    width: 500px;
}
```

Es buena práctica declarar explicitamente estas propiedades, aunque NO se vaya a cambiar el aspecto de la imágen. Esto, ya que reserva espacio para la imágen, y se evita el cambio drástico de la página cuando una imágen carga.

# Especificidad de selectores:

Hay veces donde hay elementos que entran en conflictos unos con otros. En este caso, para decidir el empate, se toman en cuenta los siguientes factores:

- Especificidad: Mayor especificidad, mayor prioridad en la elección. Selectores ID > Selectores Clase > Selectores Tipo

- Cantidad: Si dos selectores tienen la misma específicidad, ganara el que tenga más cantidad de selectores.

```
<!-- index.html -->

<div class="main">
  <div class="list subsection"></div>
</div>

/* rule 1 */
.subsection {
  color: blue;
}

/* rule 2 */
.main .list {
  color: red;
}
```

En este caso, para el elemento div anidado, existen dos selectores que le hacen referencia. Ambos selectores tienen la misma especificidad, por lo tanto, es imposible decidir sólo con la regla de especificdad. Sin embargo, el segundo selector tiene una mayor cantidad de selectores de tipo clase, por lo que se utiliza este para dar el estilo al elemento div. 

```
#subsection .list {
  background-color: yellow;
  color: blue;
}

/* rule 2 */
#subsection .main .list {
  color: red;
}

```

En este caso, se toma la segunda regla PARA LA PROPIEDAD COLOR SOLAMENTE, ya que tiene una mayor cantidad de selectores de clases. Ya que CSS es en cascada, de la primera propiedad se aplica background-color: yellow!.

Los simbolos (+, " ", >, ~) no agregan nada a la especificidad.

.class.lel = .class > .lel = .class .lel ...

- Herencia:

Hay propiedades que son heredadas por los elementos descendientes de un pariente. Por ejemplo, las propiedades de tipografía son heredadas por los hijos (color, font-size, font-family, etc)

Ahora, aplicar una propiedad directamente a un hijo SIEMPRE vencera a una propiedad heredada!.

- Cascada:

Si todo lo anterior fue considerado, y aun así hay conflictos, entonces se quedará la última propiedad aplicada.


# Linkear un CSS a un HTML

Hay 3 formas de hacerlo!

- **Método Externo:** Se crea un archivo solamente para los CSS, y eso se linkea al archivo HTML.

Para hacer el link, dentro del tag head, se agrega el tag link!

```
<head>
  <link href="styles.css" rel="stylesheet">

</head>
```

- **Método Interno:** En este método, se agrega un tag <style></style> dentro de <head></head>. Dentro del tag style se agrega todo el CSS. Esto permite estilizar una única página de HTML!

```
<head>
  <style>
    div {
      color: white;
      background-color: black;
    }

    p {
      color: red;
    }
  </style>
</head>
<body>...</body>
```

- **Método Inline:** Esto permite agregar CSS a un único elemento HTML. No se recomienda para nada. Este método tiene prioridad por sobre los otros métodos de CSS.

```
<body>
  <div style="color: white; background-color: black;">...</div>
</body>
```

"Helvetica Neue" ocupa The Odin Project, es bonita esa letra.

Knowledge Check

1. What are the main differences between external, internal, and inline CSS?

Se diferencian en dónde se posiciona el CSS utilizado. En el external se deja en un archivo aparte al HTML. En el internal se deja en el tag head, dentro de un tag style. En el inlin se deja dentro de el opening tag de un elemento

2. What is the syntax for class and ID selectors?
. y #, respectivamente

3. How would you apply a single rule to two different selectors?
Con una lista separada por comas

4. Given an element that has an id of title and a class of primary, how would you use both attributes for a single rule?
Con un selector sin espacio (#title.primary)

5. What does the descendant combinator do?
Selecciona todos los elementos que si o si contengan al/los selectores padres.

6. Between a rule that uses one class selector and a rule that uses three type selectors, which rule has the higher specificity?
El class selector!