
# Elementos **Block **e **Inline**

Los block se apilan unos sobre otros, y crean nuevas lineas (p, h1, etc).
Los inline estan unos al lado del otro, sin crear una nueva linea cuando son agregados (a, por ejemplo).

Es mejor evitar agregar padding-margin a elementos del tipo inline, ya que se comportan de forma extraña

Hay otro tipo de display que es inline-block. Que son elementos de tipo inline, pero que su padding-margin se comporta como los elementos block (normal). Sin embargo, es mejor utilizar flexbox en esos casos.

# Divs y Spans

Ambos son contenedores sin contenido alguno. Son cajas vacias. 

Div es del tipo block. Usualmente se utiliza como contenedor para otros elementos.
Span es del tipo inline. Solamente se utiliza cuando no hay otro tag semántico disponible.

El tamaño de elementos block se expande hasta abarcar todo el tamaño de su contenedor.
El tamaño de elementos inline es igual al de su contenido. Por esta misma razon es que no se puede cambiar su height y width, ya que siempre serán del tamaño de su contenido (excepto imágenes).

# Normal Layout Flow
Los elementos block se posicionan de arriba a abajo, generando una nueva linea cada vez que son puestos.

Los elementos inline se posicionan de izquierda a derecha. Dos o más elementos inline se posicionan contiguamente, y se posicionan hasta que llenan el espacio disponible en su contenedor. Si superan el largo de su contenedor, entonces ahí si generarán una nueva línea.

Si dos elementos se están tocando margenes, entonces los márgenes colapsaran. Eso significa que el margen más grande será el que separa ambos elementos. Esto es sólo relevante para margenes verticales (elementos block)

# Inline vs Inline-block

Con inline-block se puede utilizar las propiedades width, height. Además, con este tipo de display se respetan los margin y paddings.

-> La única diferencia entre block e inline-block es que en block se inserta una nueva línea después del elemento. En el caso de inline-block no. 

What is the difference between a block element and an inline element?
La forma en que se muestras en una página. Los elementos block toman todo el espacio disponible en una línea e insertan una nueva línea. Por lo tanto, estos tipos de elementos se apilan verticalmente.

Los elementos inline tienen un tamaño igual a su contenido, y no se puede cambiar (height, width, padding y margin no funcionan). Además, no insertan una nueva linea cuando son agregados, por lo que se pueden apilar horizontalmente

What is the difference between an inline element and an inline-block element?
Los elementos inline-block respetan height, width, margin y paddings. Por otro lado, los inline element no lo hacen.

Is an h1 block or inline?
Block

Is button block or inline?
Inline

Is div block or inline?
Block

Is span block or inline?
Inline