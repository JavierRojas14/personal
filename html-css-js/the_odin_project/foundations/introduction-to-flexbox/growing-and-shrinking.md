# Declaración Flex

La propiedad flex es una propiedad CSS que se puede aplicar a los items flexbox. Esta propiedad es una abreviación de 3 propiedades distintas.

La propiedad flex es una abreviación de:

flex-grow
flex-shrink
flex-basis

Si se utiliza flex: 1;, entonces las 3 propiedades anteriores se definen como:

flex-grow: 1;
flex-shrink: 1;
flex-basis: 0;


## flex-grow:

Esta propiedad espera solamente 1 valor. Indica el tamaño PROPORCIONAL del elemento flex. Por ejemplo, si todos los elementos de un flexbox tienen flex-grow 1, entonces todos tendran el mismo tamaño. Ahora, si uno de ellos tiene flex-grow: 2, entonces su tamaño será el doble de la de los otros objetos.

## flex-shrink:

Es similar a flex-grow, pero especifica el factor para achicar los objetos. Este solamente se utiliza cuando el tamaño de todos los objetos es mayor que el de su contenedor. Si todos los objetos tienen flex-shrink, entonces todos se achicaran a la misma proporcion. Sin embargo, si uno tiene un flex-shrink mayor, entonces estos objetos se achicaran más. Si se utiliza un flex-shrink, entonces ese objeto NO se achicara.

Algo importante, es que NO siempre se respetara el width especificado. En caso de que el contenedor tenga más espacio, y el objeto se pueda estirar, entonces lo hará y tendrá un width mayor al especificado. Lo mismo con el flex shrink. Si el contenedor tiene menos espacio, y el el width es mayor al brindado por el flex shrink, entonces el objeto respetará flex shrink y NO width. 

## flex-basis

Indica el tamaño inicial desde donde se quere flex-growear o flex-shrinkear. Con flex-basis: auto; el tamaño inicial está dado por width. Cuando se utiliza flex: 1, el valor de flex-basis es 0%, lo que significa que se ignorará el wdith y todo se hará igual de chico. 

-> Lo que más se utiliza es flex: 1; (flex-grow: 1; flex-shrink: 1; flex-basis: 0)
-> o flex: auto; (flex-grow: 1; flex-shrink: 1; flex-basis: auto; (para respetar el width))

Al final, flexbox se utiliza para cambiar el tamaño de sus elementos hijos para estirarlos cuando sean más chicos que el contenedor, o achicarlos para evitar el overflow del contenedor.

Valores de flex comúnes:

flex: initial; (flex: 0 1 auto;) O sea, que es un elemento que NO se estira para llenar el espacio libre, y que se achica manteniendo su width. Además, respeta el width.

flex: auto; (flex: 1 1 auto;) O sea, que es un elemento que se estira/achica para mantenerse dentro de su contenedor. Respeta el width.

flex: none; (flex: 0 0 auto;). O sea, es un elemento que NO se estira NI se achica. Respeta width.

flex: <positive number>; (flex positive_number 1 0)

Con flex-basis: 100px; El elemento tiene un width inicial de 100px. 

flex: 0 0 100px; Es un elemento que tendrá 100 de width y shá está.
flex: 1 0 100px; Es un elemento que tendrá 100 de width, que se estirará en un contenedor con espacio, y que NO se achicará.


What are the 3 values defined in the shorthand flex property (e.g. flex: 1 1 auto)?
flex-grow
flex-shrink
flex-basis

What are the 3 defined values for the flex shorthand flex:auto?
1 1 auto;