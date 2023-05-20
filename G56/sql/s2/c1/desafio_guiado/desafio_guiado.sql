SELECT *
FROM cancion
WHERE artista = (
	SELECT nombre_artista
FROM artista
WHERE nacionalidad = 'Estadounidense'
AND fecha_de_nacimiento > '1992-01-01'
LIMIT 1)
AND numero_del_track = 4;