El script de JavaScript se pone en el tag body de un HTML.

```
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Page Title</title>
</head>
<body>
  <script>
    // Your JavaScript goes here!
    console.log("Hello, World!")
  </script>
</body>
</html>
```

Sin embargo, también se puede hacer un archivo externo para linkear el script de JavaScript, muy al estilo del archivo CSS.


```
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Page Title</title>
</head>
<body>
  <script src="javascript.js"></script>
</body>
</html>
```

# Variables en JavaScript

En JavaScript las variables se declaran y se asignan!

Para declarar una variable, existen var y let.

Se recomienda utilizar **let!**

```
let variable;
```

Posteriormente, se puede asignar un valor a la variable ya declara

```
let variable;
variable = "Soy un string";
```

Ahora, ambos pasos se pueden unir y hacerlo todo en una línea.

```
let variable = "Soy un string";
```

# Ahora solamente se utiliza **let** para declarar variables! Luego veremos para que existía var. 

Con let se puede reasginar el valor de una variable cuantas veces se quiera!

```
let message;
message = "Hello";
message = "Bye";
```
Ahora, NO se puede volver a declarar una misma variable!

```
let message = "This";
let message = "That";
```

Esto genera una excepción!

# Nombre de variables

1. Se utiliza camelCase para variables que tienen más de una palabra.

# Declaración const

Hay otra forma de declarar una variable, y es con la keyword **const**. Este tipo de variable solamente se puede declarar una vez (igual que let), y no se puede reasignar (distinto a let). 

```
const myBirthday = '18.04.1902';
myBirthday = '22.2.2222';
```

Esto generaría un error!

- UPPERCASE constants: Son constantes que se sabe su valor antes de ejecutar el programa. Ej: 

```
const COLOR_ORANGE = "#FF7F00";
```

En este caso, son const que deben ir (o la convención es que) en mayúsculas y con snake case. 

- lowercase constants: Son valores constantes que no cambian, pero que se calculan durante la ejecución del programa.

```
const pageLoadTime = /* time taken by a webpage to load */;
```

# Declaración de variables - Buenas prácticas

Crear una nueva variable no genera problemas de performance, por esto es mejor declarar muchas, a ocupar una y reasignarla constantemente!.

Deben ser descriptivas