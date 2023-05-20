CREATE DATABASE inventario;

CREATE TABLE articulos(
    codigo_producto INT,
    producto TEXT,
    local TEXT,
    precio INT,
    existencia TEXT,
    stock INT,
    ubicacion TEXT,
    numero_bodega INT,
    vendedor TEXT,
    rut_vendedor INT,
    numero_boleta INT,
    cantidad_vendida INT,
    rut_cliente INT,
    nombre_cliente TEXT
);

COPY articulos
FROM 'C:\Users\javie\OneDrive\Documents\programacion\personal\G56\sql\s2\c2\desafio_evaluado\articulo.csv'
DELIMITER ','
CSV HEADER;

SELECT * FROM articulos;