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
FROM 'C:\Users\estadistica\Downloads\input\articulos.csv'
DELIMITER ','
CSV HEADER;

SELECT * FROM tabla;

-- Primera forma normal. Obtener valores atomicos y atributos no repetidos.

CREATE TABLE primera_forma_normal AS
SELECT codigo_producto, producto, local, precio, 
       existencia, stock, ubicacion, numero_bodega, 
	   split_part(vendedor, ',', 1) AS nombre_vendedor, 
	   split_part(vendedor, ',', 2) AS sobrenombre_vendedor, rut_vendedor, numero_boleta,
	   cantidad_vendida, rut_cliente, nombre_cliente
FROM tabla;

SELECT * FROM primera_forma_normal;

-- En este punto, se tiene una tabla en primera forma normal.

-- Segunda forma normal. Obtener la tabla en primera forma normal. Los atributos deben
-- depender de toda la clave primaria, y no de una parte de ella.

-- La base de datos indica la transaccion de un articulo entre un cliente y un vendedor. La base
-- se puede separar en: Informacion Articulos, Stock de un Articulo,
-- Localizacion de la Transaccion, Informacion del Vendedor, Informacion del Cliente e Informacion de la Transaccion.

-- Todas las entidades anteriores seran modeladas de la siguiente forma:

-- InformacionArticulos(#codigo_producto, producto, precio). Indicando que un producto tiene un codigo, producto y precio unico.
-- StockArticulo(#codigo_producto (FK), #numero_bodega, stock). Indicando que puede haber un unico registro de un articulo en una bodega, con un unico stock. Tambien
-- indicando que un mismo articulo puede estar en distintas bodegas.
-- LocalizacionTransaccion(#local, ubicacion). Indicando que un local tiene una unica ubicacion
-- InformacionVendedor(#rut_vendedor, nombre_vendedor, sobrenombre_vendedor).
-- InformacionCliente (#rut_cliente, nombre_cliente)
-- Transacciones(#numero_boleta, local (FK), rut_vendedor (FK), rut_cliente (FK), codigo_producto (FK), numero_bodega (FK), cantidad_vendida)

-- Esta modelacion permite que ninguna entidad presente una dependencia parcial.

CREATE TABLE InformacionArticulos AS
SELECT DISTINCT codigo_producto, producto, precio
FROM primera_forma_normal;

ALTER TABLE InformacionArticulos
ADD PRIMARY KEY (codigo_producto);

CREATE TABLE StockArticulo AS
SELECT DISTINCT codigo_producto, numero_bodega, stock
FROM primera_forma_normal;

ALTER TABLE StockArticulo
ADD PRIMARY KEY (codigo_producto, numero_bodega),
ADD CONSTRAINT fk_codigo_producto FOREIGN KEY (codigo_producto) REFERENCES InformacionArticulos (codigo_producto);

CREATE TABLE LocalizacionTransaccion AS
SELECT DISTINCT local, ubicacion
FROM primera_forma_normal;

ALTER TABLE LocalizacionTransaccion
ADD PRIMARY KEY (local);

CREATE TABLE InformacionVendedor AS
SELECT DISTINCT rut_vendedor, nombre_vendedor, sobrenombre_vendedor
FROM primera_forma_normal;

ALTER TABLE InformacionVendedor
ADD PRIMARY KEY (rut_vendedor);

CREATE TABLE InformacionCliente AS
SELECT DISTINCT rut_cliente, nombre_cliente
FROM primera_forma_normal;

ALTER TABLE InformacionCliente
ADD PRIMARY KEY (rut_cliente);

CREATE TABLE Transacciones AS
SELECT numero_boleta, local, rut_vendedor, rut_cliente, codigo_producto, numero_bodega, cantidad_vendida
FROM primera_forma_normal;

ALTER TABLE Transacciones
ADD PRIMARY KEY (numero_boleta),
ADD CONSTRAINT fk_local FOREIGN KEY (local) REFERENCES LocalizacionTransaccion (local),
ADD CONSTRAINT fk_rut_vendedor FOREIGN KEY (rut_vendedor) REFERENCES InformacionVendedor (rut_vendedor),
ADD CONSTRAINT fk_rut_cliente FOREIGN KEY (rut_cliente) REFERENCES InformacionCliente (rut_cliente),
ADD CONSTRAINT fk_stock FOREIGN KEY (codigo_producto, numero_bodega) REFERENCES StockArticulo (codigo_producto, numero_bodega);

-- En este punto, todas las tablas estan en la segunda forma normal

SELECT * FROM InformacionArticulos;
SELECT * FROM StockArticulo;
SELECT * FROM LocalizacionTransaccion;
SELECT * FROM InformacionVendedor;
SELECT * FROM InformacionCliente;
SELECT * FROM Transacciones;

-- Tercera forma normal. Se debe cumplir la segunda forma normal, y toda entidad debe depender
-- directamente de la clave primaria.

-- En este punto todas las tablas cumplen la tercera forma normal, ya que:
--  -  Para InformacionArticulos, producto y precio dependen de codigo_producto. Ademas, producto
--  y precio no dependen entre si.

--  - Para StockArticulo: El stock depende del codigo y del numero de la bodega.
--  - Para LocalizacionTransaccion: Ubicacion depende solamente del local
--  - Para Informacion Vendedor: El nombre y el sobrenombre del vendedor depende solamente del rut
--  - Para Informacion Cliente: El nombre del cliente depende unicamente de su rut
--  - Para Transacciones: Todos los atributos dependen del numero de la boleta, y ninguno depende
--  entre si.

-- Por lo tanto, se ha normalizado la base de datos. Solamente queda eliminar la tabla inicial y la tabla
-- intermedia (primera_forma_normal)

DROP TABLE primera_forma_normal;
DROP TABLE tabla;
