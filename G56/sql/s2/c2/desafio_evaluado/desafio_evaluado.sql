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

-- Antes de realizar cualquier normalizacion, se separara la tabla en 4 subtablas. Luego,
-- estas 4 subtablas seran normalizadas

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

-- 1era forma normal. Este cambio se realizara solo a la tabla PersonalEmpresa. Se obviaran
las demas tablas, ya que cumplen la primera forma normal.

-- PersonalEmpresa(#rut_vendedor, vendedor) pasara a PersonalEmpresa(#rut_vendedor, nombre_vendedor,
sobrenombre_vendedor)




