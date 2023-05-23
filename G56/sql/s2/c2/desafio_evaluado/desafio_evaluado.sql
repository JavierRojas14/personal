CREATE DATABASE inventario;

CREATE TABLE tabla(
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

COPY tabla
FROM 'C:\Users\javie\OneDrive\Documents\programacion\personal\G56\sql\s2\c2\desafio_evaluado\articulo.csv'
DELIMITER ','
CSV HEADER;

SELECT * FROM tabla;



-- TABLA(codigo_producto,
-- producto,
-- local,
-- precio,
-- existencia,
-- stock,
-- ubicacion,
-- numero_bodega,
-- vendedor,
-- rut_vendedor,
-- numero_boleta,
-- cantidad_vendida,
-- rut_cliente,
-- nombre_cliente)

-- Para realizar la normalización a la primera forma normal, se separararán las tablas de la siguiente
forma:

-- Articulos(#codigo_producto,
-- producto,
-- local,
-- precio,
-- existencia,
-- stock,
-- ubicacion,
-- numero_bodega)

-- PersonalEmpresa(#rut_vendedor,
-- vendedor)

-- ClientesEmpresa(#rut_cliente,
-- nombre_cliente)

-- Transacciones(#numero_boleta, rut_vendedor, rut_cliente, codigo_producto, cantidad_vendida)

-- Esto permitirá que cada tabla tenga una llave primaria.
-- Además, la tabla PersonalEmpresa(#rut_vendedor, vendedor) pasara a PersonalEmpresa(#rut_vendedor, nombre_vendedor,
sobrenombre_vendedor) para cumplir con la atomicidad de datos.

CREATE TABLE Articulos AS
SELECT codigo_producto, producto, local, precio, existencia, stock, ubicacion, numero_bodega
FROM tabla;

ALTER TABLE Articulos
ADD PRIMARY KEY (codigo_producto);

CREATE TABLE PersonalEmpresa AS
SELECT rut_vendedor, split_part(vendedor, ',', 1) AS nombre_vendedor, split_part(vendedor, ',', 2) AS sobrenombre_vendedor
FROM tabla;

ALTER TABLE PersonalEmpresa
ADD PRIMARY KEY (rut_vendedor);

CREATE TABLE ClientesEmpresa AS
SELECT rut_cliente, nombre_cliente
FROM tabla;

ALTER TABLE ClientesEmpresa
ADD PRIMARY KEY (rut_cliente);

CREATE TABLE Transacciones AS
SELECT numero_boleta, rut_vendedor, rut_cliente, codigo_producto, cantidad_vendida
FROM tabla;

ALTER TABLE Transacciones
ADD PRIMARY KEY (numero_boleta);

-- 2da forma normal. Se quieren eliminar las dependencias parciales!. Este cambio se realizara
solo a la tabla Articulos. Se obviaran las demas tablas, ya que cumplen con la segunda forma normal.

-- Articulos(#codigo_producto,
-- producto,
-- local,
-- precio,
-- existencia,
-- stock,
-- ubicacion,
-- numero_bodega) pasara a MaestroArticulos(#codigo_producto, producto, precio, local, ubicacion, numero_bodega)
-- y DisponbilidadArticulos(#codigo_producto, )




