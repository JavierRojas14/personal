SELECT nombre_artista
FROM artista
WHERE nacionalidad = 'Estadounidense' AND fecha_de_nacimiento > '1992-01-01'
LIMIT 1;