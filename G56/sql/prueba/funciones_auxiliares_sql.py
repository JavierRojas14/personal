import csv


def insertar_csv_a_tabla_postgres(ruta_csv, nombre_tabla_destino, cursor):
    with open(ruta_csv) as file:
        reader = csv.reader(file)
        header = next(reader)

        valores_a_insertar = ["%s" for i in range(len(header))]
        valores_a_insertar = ", ".join(valores_a_insertar)

        query = f"INSERT INTO {nombre_tabla_destino} VALUES({valores_a_insertar})"

        for row in reader:
            cursor.execute(query, row)


def entrenar_modelos_en_tanda(vectores_objetivo, modelos_a_entrenar, df_train):
    resultados_modelos = {}

    for vector_objetivo in vectores_objetivo:
        modelos_entrenados = []
        for funcion_modelo in modelos_a_entrenar:
            modelo = funcion_modelo()
            X_train = df_train.drop(columns=vector_objetivo)
            y_train = df_train[vector_objetivo]

            modelo_entrenado = modelo.fit(X_train, y_train)
            modelos_entrenados.append(modelo_entrenado)

        resultados_modelos[vector_objetivo] = modelos_entrenados

    return resultados_modelos
