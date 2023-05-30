import csv
import pandas as pd


def insertar_csv_a_tabla_postgres(ruta_csv, nombre_tabla_destino, cursor):
    with open(ruta_csv, encoding="utf-8") as file:
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
        modelos_entrenados = {}
        for nombre_modelo, funcion_modelo in modelos_a_entrenar.items():
            modelo = funcion_modelo()
            X_train = df_train.drop(columns=vector_objetivo)
            y_train = df_train[vector_objetivo]

            modelo_entrenado = modelo.fit(X_train, y_train)
            modelos_entrenados[nombre_modelo] = modelo_entrenado

        resultados_modelos[vector_objetivo] = modelos_entrenados

    return resultados_modelos


def reportar_metricas_machine_learning(metricas_machine_learning, y_true, y_pred):
    print("--------------------------------------------")
    for nombre_metrica, metrica in metricas_machine_learning.items():
        print(f"{nombre_metrica}: {metrica(y_true, y_pred)}")
    print("--------------------------------------------")


def testear_modelos_en_tanda(vectores_objetivos, dict_modelos_entrenados, df_test, dict_metricas):
    dfs_resultado = {}
    for vector_objetivo in vectores_objetivos:
        dfs_predichas_por_modelo = {}
        modelos_entrenados = dict_modelos_entrenados[vector_objetivo]

        X_test = df_test.drop(columns=vector_objetivo)
        y_test = df_test[vector_objetivo]

        for nombre_modelo, modelo_entrenado in modelos_entrenados.items():
            yhat = modelo_entrenado.predict(X_test)

            print(f"{vector_objetivo} - {nombre_modelo}")
            reportar_metricas_machine_learning(dict_metricas, y_test, yhat)
            print()

            df_predicha = df_test.copy()
            df_predicha[f'yhat_{vector_objetivo}'] = yhat

            dfs_predichas_por_modelo[nombre_modelo] = df_predicha

        dfs_resultado[vector_objetivo] = dfs_predichas_por_modelo

    return dfs_resultado
