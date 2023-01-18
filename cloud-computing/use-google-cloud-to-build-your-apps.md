# Google Cloud Functions

Permite correr un codigo cuando ocurra un cierto evento. Este evento puede ser por ej: Cuando se suba una foto. Se corre solamente 1 funcion! de forma asincronica/sincronica (si se configura).

En este caso es innecesario tener un server para correr la funcion.

Las funciones puedes ser escritas en Node.js (JavaScript), Python o Go.

Las Google Cloud Functions permiten conectar diversos servicios/programas que ya estan en Google Cloud.

## Eventos de las Cloud Functions

Los eventos son sucesos que ocurren dentro del ambiente de la nube, por ejemplo: Que se ingrese un dato, que se cree una maquina virtual, que se suba un archivo, etc. Estos eventos ocurren en todo momento, con o sin google functions. Lo que permite escuchar estos eventos y fijarse si es que estan ocurriendo o no son los **triggers**. Hay toda una seccion para events y triggers

## Serverless

Ya que las funciones estan dentro de la nube, es innecesario alocar manualmente recursos e infraestrctura. Ademas, se escalan automaticamente (por ej: Si antes se lanzaba 1 vez al dia, y luego se lanza 1 vez cada segundo)