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

-- 1era forma normal. Se separara la tabla en 4 subtablas, permitiendo que cada una
-- tenga una llave primaria, y que contengan valores atomicos.

CREATE TABLE Articulos AS
SELECT DISTINCT codigo_producto, producto, local, precio, existencia, stock, ubicacion, numero_bodega
FROM tabla;

ALTER TABLE Articulos
ADD PRIMARY KEY (codigo_producto);

SELECT * FROM Articulos;
--

CREATE TABLE PersonalEmpresa AS
SELECT DISTINCT rut_vendedor, split_part(vendedor, ',', 1) AS nombre_vendedor, split_part(vendedor, ',', 2) AS sobrenombre_vendedor
FROM tabla;

ALTER TABLE PersonalEmpresa
ADD PRIMARY KEY (rut_vendedor);

SELECT * FROM PersonalEmpresa;

--
CREATE TABLE ClientesEmpresa AS
SELECT rut_cliente, nombre_cliente
FROM tabla;

ALTER TABLE ClientesEmpresa
ADD PRIMARY KEY (rut_cliente);

SELECT * FROM ClientesEmpresa;
--
CREATE TABLE Transacciones AS
SELECT numero_boleta, rut_vendedor, rut_cliente, codigo_producto, cantidad_vendida
FROM tabla;

ALTER TABLE Transacciones
ADD PRIMARY KEY (numero_boleta);

ALTER TABLE Transacciones
ADD CONSTRAINT fk_rut_vendedor FOREIGN KEY (rut_vendedor) REFERENCES PersonalEmpresa (rut_vendedor);

ALTER TABLE Transacciones
ADD CONSTRAINT fk_rut_cliente FOREIGN KEY (rut_cliente) REFERENCES ClientesEmpresa (rut_cliente);

ALTER TABLE Transacciones
ADD CONSTRAINT fk_codigo_producto FOREIGN KEY (codigo_producto) REFERENCES Articulos (codigo_producto);

SELECT * FROM Transacciones;
-- 2da forma normal. Aqui solamente se cambiara la tabla Articulos, ya que la columna ubicacion es parcialmente
-- dependiente de local. Ademas, se eliminara la columna existencia, ya que es redundante (si stock > 0, entonces existe el articulo).


CREATE TABLE MaestroArticulos AS
SELECT codigo_producto, producto, local, precio, stock, numero_bodega
FROM Articulos;

ALTER TABLE MaestroArticulos
ADD PRIMARY KEY (codigo_producto);

CREATE TABLE Destinos AS
SELECT DISTINCT local, ubicacion
FROM Articulos;

ALTER TABLE Destinos
ADD PRIMARY KEY (local);

ALTER TABLE MaestroArticulos
ADD CONSTRAINT fk_local FOREIGN KEY (local) REFERENCES Destinos (local);

-- 3era forma normal. Se deben eliminar las relaciones transitivas. 
SELECT * FROM ClientesEmpresa;
SELECT * FROM PersonalEmpresa;
SELECT * FROM MaestroArticulos;
SELECT * FROM Destinos;
SELECT * FROM Transacciones;

-- Si se ve cada una de las tablas resultantes, se puede ver que todas cumplen la 3era forma normal.
-- Esto, ya que todos los atributos de cada tabla dependen unicamente de la llave primaria. Ademas,
-- ninguna columna no llave presenta una relacion entre si.

-- Por lo tanto, la base de datos se encuentra normalizada. Solamente queda eliminar las tablas intermedias
-- y la tabla inicial.

DROP TABLE tabla;
DROP TABLE articulos CASCADE;

-- Debido a que se elimino la relacion de llave foranea en la tabla transacciones, es necesario redeclararla
-- con la tabla de maestro articulos

SELECT * FROM MaestroArticulos;

ALTER TABLE Transacciones
ADD CONSTRAINT fk_codigo_producto FOREIGN KEY (codigo_producto) REFERENCES MaestroArticulos (codigo_producto);
