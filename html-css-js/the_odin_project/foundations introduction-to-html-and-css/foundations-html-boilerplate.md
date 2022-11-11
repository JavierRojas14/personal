El archivo HTML de una página SIEMPRE se debe llamar index.html. Esto, ya que los web servers (computadores servidores que contienen diversas web pages) siempre buscarán por el archivo index.html. 

**- DOCTYPE:** Es una declaración que permite indicar la versión de HTML que está ocupando la página. 

```<!DOCTYPE html>``` -> Para ocupar HTML5 (último)

**- HTML:** Es un elemento raíz. Indica que todos los demás elementos son descendientes de este elemento. Es importante para la utilización con JavaScript.

```<html lang="en"></html>```

lang es un atributo que permite mejorar la accesibilidad a la página para, por ejemplo, lectores de pantalla (permiten identificar que la página está en inglés y adaptar el acento de lectura)

**- Head:** Es un elemento que contiene todos los elementos descriptivos de la página (meta). Además, JAMAS contiene elementos visibles en la página.

 - **Charset Meta:** Es un elemento que permite mostrar correctamente la utilización de carácteres especiales.

 ```<meta charset="utf-8"/>```
 - **Title Element:** Cambia el titulo de la página web.


- **Body:** Contiene todos los elementos visibles en una página web

VSCODE TIENE UN ATAJO PARA AGREGAR TODOS ESTOS ELEMENTOS AUTOMÁTICAMENTE. SIMPLEMENTE HAY QUE AGREGAR ! A UN ARCHIVO .HTML Y ENTER Y BOILAA.

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
</body>
</html>
```

What is the purpose of the doctype declaration?

Permite declarar la versión de HTML que se está usando en la página.

What is the HTML element?

Es un elemento raíz, que permite indicar que todos los demás elementos son descendientes de este. Útil cuando se utiliza JS.

What is the purpose of the head element?

Permite contener todos los meta-elementos de la página (que la describen de alguna forma) y que NO se ven en este.

What is the purpose of the body element?

Contiene todos los elementos visibles de una página.