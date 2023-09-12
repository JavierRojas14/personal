Se hacen con el tag

<table></table>


Para hacer una fila se hace con el tag <tr></tr>
Para insertar un dato en una fila se <td></td>
Para hacer un header se hace con el tag <th></th>. Un table header es como un table data, pero identifica un header. Para saber si es un header de una columna o una file se puede utilizar el atributo scope. Si el header abarca mas de 1 celda, entonces se puede ocupar: scope="colgroup" o "rowgroup" en vez de "col" o "row"

Se puede ocupar los atributos colspan o rowspan para hacer que una celda abarque mas de una celda.

What is a table?
It is a figure that organizes data in rows and columns.

Why is it a bad idea to use HTML Tables for page layout?
Because they're meant for layout. Styling and layout works weird in tables.

What are caption elements useful for?
To summarize the content of a table without having to read every cell of it.

What is the scope attribute?
It is an attribute of header cells that tells if the header is header for a row or a column