import random

random.seed(1)

DICCIONARIO_REEMPLAZO = {
    "worry": 0,
    "happiness": 1,
    "sadness": 0,
    "love": 1,
    "surprise": 1,
    "fun": 1,
    "relief": 1,
    "hate": 0,
    "empty": 0,
    "enthusiasm": 1,
    "boredom": 0,
    "anger": 0,
}


def codificar_sentimientos(vector_objetivo):
    vector_objetivo_codificado = vector_objetivo.replace(DICCIONARIO_REEMPLAZO)
    neutrales = vector_objetivo_codificado[vector_objetivo_codificado == "neutral"]
    neutrales = neutrales.apply(lambda x: random.choice([0, 1]))
    vector_objetivo_codificado.iloc[neutrales.index] = neutrales
    vector_objetivo_codificado = vector_objetivo_codificado.astype(int)

    return vector_objetivo_codificado


def resumir_resultados_grid_cv(diccionario_resultados):
    df_resultados = pd.DataFrame(diccionario_resultados)
    df_resultados["params_str"] = df_resultados["params"].astype(str)

    return df_resultados


def graficar_resultados_grid_cv(resultado_df):
    sns.lineplot(data=resultado_df, x="params_str", y="mean_test_score", marker="o")
    plt.tick_params(axis="x", labelrotation=90)


def analizar_resultados_grid_cv(diccionario_resultados):
    df_resultados = resumir_resultados_grid_cv(diccionario_resultados)
    graficar_resultados_grid_cv(df_resultados)

    return df_resultados


def entrenar_y_obtener_desempeno_modelo_en_grilla(modelo_grilla, X_train, X_test, y_train, y_test):
    modelo_grilla.fit(X_train, y_train)
    print(f"\n\n--------------Resultados Conjunto de Entrenamiento-----------------")
    print("Los resultados en la busqueda de hiperparametros son:")
    resultados_grilla = analizar_resultados_grid_cv(modelo_grilla.cv_results_)
    plt.show()
    print(f"Los mejores parametros fueron: {modelo_grilla.best_params_}")
    print(f"El mejor desempeno fue: {modelo_grilla.best_score_}")

    print(f"\n\n--------------Resultados Conjunto de Validacion-----------------")
    yhat = modelo_grilla.predict(X_test)
    roc = roc_auc_score(y_test, yhat)
    print("Los resultados en el conjunto de validacion son:")
    print(classification_report(y_test, yhat))
    print(f"El ROC fue de: {roc}")

    print(f"---------------------------------------------------------------------")

    return modelo_grilla, resultados_grilla
