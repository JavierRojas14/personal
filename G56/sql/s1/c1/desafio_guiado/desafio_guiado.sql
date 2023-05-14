CREATE DATABASE Biblioteca;

CREATE TABLE Libro(
    id_libro INT PRIMARY KEY,
    nombre_libro TEXT,
    autor TEXT,
    genero TEXT
);

INSERT INTO Libro
VALUES (1, 'Sapo y Sepo', 'Pepe', 'Aventuras');

INSERT INTO Libro
VALUES (2, 'La Metamorfosis', 'Juanito', 'Misterio');

CREATE TABLE Prestamo(
    id_prestamo INT PRIMARY KEY,
    id_libro INT,
    nombre_persona TEXT,
    fecha_inicio DATE,
    fecha_termina DATE,
    FOREIGN KEY (id_libro)
    REFERENCES Libro(id_libro)
)

ALTER TABLE Libro
ADD COLUMN prestado BOOLEAN;

UPDATE Libro
SET prestamo = TRUE
WHERE id_libro = 1;

UPDATE Libro
SET prestamo = FALSE
WHERE id_libro = 2;

INSERT INTO Prestamo
VALUES (1, 1, 'Javier', '2022-02-01', '2022-02-03');

INSERT INTO Prestamo
VALUES (2, 1, 'Javier', '2022-02-04', '2022-02-05');

INSERT INTO Prestamo
VALUES (3, 1, 'Carlos', '2022-02-10', '2022-02-20');

INSERT INTO Prestamo
VALUES (4, 1, 'Pepe', '2022-02-21', '2022-02-22');

INSERT INTO Prestamo
VALUES (5, 1, 'John', '2022-02-27', '2022-03-01');

INSERT INTO Prestamo
VALUES (6, 2, 'Javier', '2022-02-01', '2022-02-03');

INSERT INTO Prestamo
VALUES (7, 2, 'Javier', '2022-02-04', '2022-02-05');

INSERT INTO Prestamo
VALUES (8, 2, 'Carlos', '2022-02-10', '2022-02-20');

INSERT INTO Prestamo
VALUES (9, 2, 'Pepe', '2022-02-21', '2022-02-22');

INSERT INTO Prestamo
VALUES (10, 2, 'John', '2022-02-27', '2022-03-01');
