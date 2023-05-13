CREATE DATABASE spotify2018;

CREATE TABLE Artista(
    nombre_artista TEXT,
    fecha_de_nacimiento DATE,
    nacionalidad TEXT,
    PRIMARY KEY(nombre_artista)
);

CREATE TABLE Cancion(
    titulo_cancion TEXT,
    artista TEXT,
    album TEXT,
    numero_del_track INT,
    FOREIGN KEY (artista)
    REFERENCES Artista(nombre_artista)
);

CREATE TABLE Album(
    titulo_album TEXT,
    artista TEXT,
    anio INT,
    FOREIGN KEY (artista)
    REFERENCES Artista(nombre_artista)
);

COPY Artista
FROM 'C:\Users\Pc\Documents\personal\G56\sql\s1\c2\desafio_evaluado\input\Artista.csv'
DELIMITER ','
ENCODING 'LATIN-1'
CSV HEADER;

COPY Cancion
FROM 'C:\Users\Pc\Documents\personal\G56\sql\s1\c2\desafio_evaluado\input\Cancion.csv'
DELIMITER ','
ENCODING 'LATIN-1'
CSV HEADER;

COPY Album
FROM 'C:\Users\Pc\Documents\personal\G56\sql\s1\c2\desafio_evaluado\input\Album.csv'
DELIMITER ','
ENCODING 'LATIN-1'
CSV HEADER;