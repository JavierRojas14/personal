# Axes

Flexbox tiene 2 direcciones para situar los objetos, esta puede ser horizontal (row)
o vertical (column).

Para cambiar la dirección se utiliza:

item {
    flex-direction: row;
}

Cada flexbox tiene una main axis (definida por la direccion) y una cross axis (eje perpendicular).

Cuando se utiliza la dirección de flex-direction: column;, flex basis toma como default (en caso de que se use auto) el height del objeto, en vez del width!.

How do you make flex items arrange themselves vertically instead of horizontally?
flex-direction: column;

In a column flex-container, what does flex-basis refer to?
Refiere al height en vez del width!

In a row flex-container, what does flex-basis refer to?
Refiere al width en vez del height

Why do the previous two questions have different answers?
Porque en este caso se cambió el main axis, por lo que los elementos se agregan de forma distina.