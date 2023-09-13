En este capitulo se ven las unidades de medidas, en especifico px, em y rem.

1. px: Altura/Ancho de un punto que puede ser visto por el ojo humano sin molestia a una distancia de un brazo. Es una medida absoluta.

2. em: Medida relativa al tamaño de la letra del elemento contenedor. Ej: font-size de contenedor: 16px, entonces 2em sería 32px.

3. rem: Medida relativ aal tamaño de la letra del elemento raíz (html)

¿Cuándo ocupar una medida absoluta o relativa?

- Si se tiene en mente la accesibilidad del sitio (Ej: Hacer zoom en una página), entonces relativa. Aunque igual con una medida absoluta se hará zoom correctamente a las letras.

Sugerencias

- Ocupar rem para el tamaño de las letras. También settear el font-size del elemento HTML.
- Ocupar px para todo lo demas (height, width, paddings, etc)

Para width:

- Es mejor ocupar ch (que es el largo del caracter 0 de cualquier letra). Esto es util, ya que se sabe que un párrafo es mucho más legible cuando tiene máximo 75 carácteres. Entonces, si uno settea a 75ch, entonces tendrá aproximadamente 75 carácteres por línea.

Para height:

Primero, totalmente debo poner una height? Si es que totalmente lo necesito, es mejor poner min-height y ocupar rem.

Para padding y margin:

Ocupar em o rem.

También existe Viewport Height (vh) y Viewport Width (vw), que es una medida relativa al tamaño de la ventana del navegador.

Why would you want to use em or rem for font-size instead of px?
Cuando se quiere respetar la decisión del usuario de agrandar la página. En otras palabras, cuando se quiere priorizar la accesibilidad del sitio

What are some instances where you might want to use vh and vw?
Cuando se quiere cambiar el tamaño de los elementos relativo a la ventana del navegador

What are some instances where you might want to use px instead of a relative unit?
Cuando se quiere mantener el tamaño de alguna cosa de la página estática, independiente de cómo el usuario cambie la página.