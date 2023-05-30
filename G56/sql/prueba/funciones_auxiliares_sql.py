"""
This module provides functions for working with CSV files, training machine learning models,
and evaluating their performance.

Functions:
- insertar_csv_a_tabla_postgres(ruta_csv, nombre_tabla_destino, cursor): Inserts the contents
  of a CSV file into a PostgreSQL table.
- entrenar_modelos_en_tanda(vectores_objetivo, modelos_a_entrenar, df_train): Trains multiple
  machine learning models on a given training dataset.
- reportar_metricas_machine_learning(metricas_machine_learning, y_true, y_pred): Prints the
  evaluation metrics for machine learning models.
- testear_modelos_en_tanda(vectores_objetivos, dict_modelos_entrenados, df_test, dict_metricas):
  Evaluates multiple machine learning models on a given test dataset.
"""
import csv


def insertar_csv_a_tabla_postgres(ruta_csv, nombre_tabla_destino, cursor):
    """
    Inserts the contents of a CSV file into a PostgreSQL table.

   :param ruta_csv: The path to the CSV file.
   :type ruta_csv: str

   :param nombre_tabla_destino: The name of the destination table.
   :type nombre_tabla_destino: str

   :param cursor: The cursor object used to execute the SQL query.
   :type cursor: psycopg2.extensions.cursor
    """
    with open(ruta_csv, encoding="utf-8") as file:
        reader = csv.reader(file)
        header = next(reader)

        valores_a_insertar = ["%s" for i in range(len(header))]
        valores_a_insertar = ", ".join(valores_a_insertar)

        query = f"INSERT INTO {nombre_tabla_destino} VALUES({valores_a_insertar})"

        for row in reader:
            cursor.execute(query, row)


def entrenar_modelos_en_tanda(vectores_objetivo, modelos_a_entrenar, df_train):
    """
    Trains multiple machine learning models on a given training dataset.

   :param vectores_objetivo: A list of target variables to predict.
   :type vectores_objetivo: list

   :param modelos_a_entrenar: A dictionary mapping model names to their corresponding training 
   functions.
   :type modelos_a_entrenar: dict

   :param df_train: The training dataset as a pandas DataFrame.
   :type df_train: pandas.DataFrame

   :return: A dictionary containing the trained models for each target variable.
   :rtype: dict
    """
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
    """
    Prints the evaluation metrics for machine learning models.

   :param metricas_machine_learning: A dictionary mapping metric names to their corresponding 
   metric functions.
   :type metricas_machine_learning: dict

   :param y_true: The true values of the target variable.
   :type y_true: array-like

   :param y_pred: The predicted values of the target variable.
   :type y_pred: array-like
   """
    print("--------------------------------------------")
    for nombre_metrica, metrica in metricas_machine_learning.items():
        print(f"{nombre_metrica}: {metrica(y_true, y_pred)}")
    print("--------------------------------------------")


def testear_modelos_en_tanda(vectores_objetivos, dict_modelos_entrenados, df_test, dict_metricas):
    """
    Evaluates multiple machine learning models on a given test dataset.

   :param vectores_objetivos: A list of target variables to predict.
   :type vectores_objetivos: list

   :param dict_modelos_entrenados: A dictionary mapping target variables to a dictionary of 
   trained models.
   :type dict_modelos_entrenados: dict

   :param df_test: The test dataset as a pandas DataFrame.
   :type df_test: pandas.DataFrame

   :param dict_metricas: A dictionary mapping metric names to their corresponding metric functions.
   :type dict_metricas: dict

   :return: A dictionary containing the predicted values for each model and target variable.
   :rtype: dict
   """
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
