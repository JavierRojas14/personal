CREATE DATABASE Biblioteca;

CREATE TABLE Biblioteca.Libro(
    id_libro INT PRIMARY KEY,
    nombre_libro TEXT,
    autor TEXT,
    genero TEXT
);

INSERT INTO Biblioteca.Libro
VALUES (1, "Sapo y Sepo", "Pepe", "Aventuras");

INSERT INTO Biblioteca.Libro
VALUES (2, "La Metamorfosis", "Juanito", "Misterio");

CREATE TABLE Biblioteca.Prestamo(
    id_prestamo INT PRIMARY KEY,
    id_libro 
)