# Hay 3 tipos de modelos para la versión de control

1. La versión local: Donde se tiene el registro en un computador local de la historia de un archivo. Se registran las diferencias entre archivos, y de esta forma dse puede reconstruir la historia de un archivo.

2. La versión de server: Un computador (el server) tiene todo el historial de archivos con sus diferencias. Los clientes pueden descargar este registro y modificarlo. El gran problema de este modelo es que si el server muere, todo el historial de archivos muere con el.

3. La versión de server distribuido. En este caso, el computador server, y sus clientes contienen todo el historial de archivos en sus repositorios. Por lo tanto, si muere el server, no muere toda la info.