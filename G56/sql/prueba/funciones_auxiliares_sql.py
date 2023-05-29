import csv

def insertar_csv_a_tabla_postgres(ruta_csv, nombre_tabla_destino, cursor):
    with open(ruta_csv) as file:
        reader = csv.reader(file)
        header = next(reader)

        valores_a_insertar = ['%s' for i in range(len(header))]
        valores_a_insertar = ', '.join(valores_a_insertar)

        query = f"INSERT INTO {nombre_tabla_destino} VALUES({valores_a_insertar})"

        for row in reader:
            cursor.execute(query, row)