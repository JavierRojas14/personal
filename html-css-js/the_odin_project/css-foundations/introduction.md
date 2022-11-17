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

Hay veces donde hay elementos que califican para más de un selector.

Ej:

```
.subsection {
  color: blue;
}

.main .list {
  color: red;
}
```

Si un elemento 


# Linkear un CSS a un HTML

Se hace en el Tag <heas></head>, con el tag <link>.

```
<head>
  <link href="styles.css" rel="stylesheet">

</head>
```

