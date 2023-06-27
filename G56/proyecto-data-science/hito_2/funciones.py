import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.metrics import classification_report
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import OneHotEncoder


# Función para entrenar modelos
def entrenar_ensamble_de_modelos_gridcv(
    grilla_gridcv_con_modelos, X_train, X_test, y_train, y_test
):
    """
     Entrena un conjunto de modelos utilizando GridSearchCV y muestra los resultados de desempeño en
     un conjunto de prueba.

    :param grilla_gridcv_con_modelos: Una lista que contiene información sobre los modelos,
    parámetros de búsqueda y nombre del modelo.
    :type grilla_gridcv_con_modelos: list of dictionaries
    :param X_train: Variables independientes del conjunto de entrenamiento.
    :type X_train: array-like
    :param X_test: Variables independientes del conjunto de prueba.
    :type X_test: array-like
    :param y_train: Variable dependiente del conjunto de entrenamiento.
    :type y_train: array-like
    :param y_test: Variable dependiente del conjunto de prueba.
    :type y_test: array-like

    :returns: None
    """
    for model_info in grilla_gridcv_con_modelos:
        print("Training", model_info["nombre"], "...")
        model = model_info["modelo"]
        param_grid = model_info["param_grid"]

        grid_search = GridSearchCV(model, param_grid, cv=5, n_jobs=-1)
        grid_search.fit(X_train, y_train)
        model_info["modelo"] = grid_search

        obtener_desempeno_modelo_en_grilla(grid_search, X_test, y_test)


def resumir_resultados_grid_cv(diccionario_resultados):
    """
    Toma un diccionario de resultados de GridSearchCV y genera un DataFrame resumido con los
    resultados.

    :param diccionario_resultados: Diccionario de resultados devuelto por el atributo `cv_results_`
    de GridSearchCV.
    :type diccionario_resultados: dictionary
    :returns: pandas DataFrame
    """
    df_resultados = pd.DataFrame(diccionario_resultados)
    df_resultados["params_str"] = df_resultados["params"].astype(str)

    return df_resultados


def graficar_resultados_grid_cv(resultado_df):
    """
    Grafica los resultados de GridSearchCV en un gráfico de líneas.

    :param resultado_df: DataFrame que contiene los resultados de GridSearchCV.
    :type resultado_df: pandas DataFrame
    :returns: None
    """
    sns.lineplot(data=resultado_df, x="params_str", y="mean_test_score", marker="o")
    plt.tick_params(axis="x", labelrotation=90)


def analizar_resultados_grid_cv(diccionario_resultados):
    """
    Toma un diccionario de resultados de GridSearchCV, resume los resultados y los grafica en un
    gráfico de líneas.

    :param diccionario_resultados: Diccionario de resultados devuelto por el atributo `cv_results_`
    de GridSearchCV.
    :type diccionario_resultados: dictionary
    :returns: pandas DataFrame
    """
    df_resultados = resumir_resultados_grid_cv(diccionario_resultados)
    graficar_resultados_grid_cv(df_resultados)

    return df_resultados


def obtener_desempeno_modelo_en_grilla(modelo_grilla, X_test, y_test):
    """
    Muestra el desempeño de un modelo entrenado con GridSearchCV en un conjunto de prueba.

    :param modelo_grilla: Modelo entrenado con GridSearchCV.
    :type modelo_grilla: GridSearchCV object
    :param X_test: Variables independientes del conjunto de prueba.
    :type X_test: array-like
    :param y_test: Variable dependiente del conjunto de prueba
    :type y_test: array-like
    :returns: pandas DataFrame
    """
    print("--------------Resultados Conjunto de Entrenamiento-----------------")
    print("Los resultados en la busqueda de hiperparametros son:")
    resultados_grilla = analizar_resultados_grid_cv(modelo_grilla.cv_results_)
    plt.show()
    print(f"Los mejores parametros fueron: {modelo_grilla.best_params_}")
    print(f"El mejor desempeno fue: {modelo_grilla.best_score_}")

    print("\n\n--------------Resultados Conjunto de Validacion-----------------")
    yhat = modelo_grilla.predict(X_test)
    print("Los resultados en el conjunto de validacion son:")
    print(classification_report(y_test, yhat))

    print("---------------------------------------------------------------------")

    return resultados_grilla


def obtener_desempeno_variables(modelo_entrenado):
    try:
        importancias = modelo_entrenado.feature_importances_

    except AttributeError:
        importancias = modelo_entrenado.coef_[0]

    features = modelo_entrenado.feature_names_in_
    resumen = pd.DataFrame({"vars": features, "importancia": importancias}).sort_values(
        "importancia", ascending=False
    )

    return resumen


def convertir_a_probabilidad(x):
    return (np.exp(abs(x))) / (1 + np.exp(abs(x)))


def preprocesar_dataset_cancer_mama(df):
    """
    Preprocesa un dataset de cáncer de mama.

    :param df: El dataset a preprocesar.
    :type df: pandas DataFrame
    :returns: pandas DataFrame

    """

    # Paso 1: Crear una copia del dataframe original
    tmp = df.copy()

    # Paso 2: Eliminar columnas redundantes o sin mayor información
    tmp = tmp.drop(columns=["CATEGORIA", "SUBCATEGORIA", "CODIGO_COMUNA"])

    # Paso 3: Categorizar la edad en rangos etarios
    tmp["RANGO_ETARIO"] = pd.cut(
        tmp["EDAD"],
        [0, 14, 29, 59, np.inf],
        labels=["Niños", "Jovenes", "Adultos", "Adulto mayor"],
    )
    tmp = tmp.drop(columns=["EDAD"])

    # Paso 4: Filtrar filas con al menos 1 examen
    columnas_examenes = ["CT", "CN", "CM", "PT", "PN", "PM"]
    tmp = tmp.dropna(subset=columnas_examenes, how="all")

    # Paso 5: Eliminar columnas de fechas
    columnas_fechas = ["FECHA_DIAGNOSTICO", "FECHA_DEFUNCION", "FECHA_INICIO_TTO", "FECHA_FIN_TTO"]
    # for columna in columnas_fechas:
    #     tmp[columna] = pd.to_datetime(tmp[columna], yearfirst=True)

    # tmp["DIAS_TTO"] = (tmp["FECHA_FIN_TTO"] - tmp["FECHA_INICIO_TTO"]).dt.days
    # tmp["PROYECCION_DIAS"] = (tmp["FECHA_DEFUNCION"] - tmp["FECHA_DIAGNOSTICO"]).dt.days

    tmp = tmp.drop(columns=columnas_fechas)

    # Paso 6: Crear el vector objetivo "STATUS" a partir de la columna "ESTADIO"
    reemplazar_estadio = {
        "0": 1,
        "I": 1,
        "II": 2,
        "III": 3,
        "IV": 3,
    }

    tmp["STATUS"] = tmp["ESTADIO"].replace(reemplazar_estadio)
    tmp = tmp.drop(columns=["ESTADIO"])

    # Paso 7: Rellenar valores faltantes con "SO" (Sin Observacion)
    tmp = tmp.fillna("NO DEFINIDO")

    # Paso 8: Eliminar registros duplicados y contar la cantidad de terapias
    pacientes_unicos = tmp.drop(columns="TTO_FALP_SUBCATEGORIA").drop_duplicates()
    conteo_terapias = pd.crosstab(tmp["ID_CASO"], tmp["TTO_FALP_SUBCATEGORIA"]).add_prefix(
        "TTO_FALP_SUBCATEGORIA_"
    )
    tmp = pd.merge(pacientes_unicos, conteo_terapias, how="inner", on="ID_CASO")

    # Paso 9: Elimina ID_CASO
    tmp = tmp.drop(columns="ID_CASO")

    return tmp


def obtener_vars_indicadoras(df, encoder=None):
    cols_categoricas = df.select_dtypes(exclude="number")
    cols_numericas = df.select_dtypes(include="number")

    if not encoder:
        encoder = OneHotEncoder(drop="first", sparse=False, handle_unknown="ignore")
        encoder.fit(cols_categoricas)

    cols_categoricas_dummies = encoder.transform(cols_categoricas)
    df_cols_categoricas_dummies = pd.DataFrame(
        cols_categoricas_dummies, columns=encoder.get_feature_names_out()
    )

    matriz_final = pd.concat([cols_numericas, df_cols_categoricas_dummies], axis=1)

    return matriz_final, encoder


# Función para gráficos para ver distribución de c/variable
def plot_variables(df):
    num_cols = df.select_dtypes(include=["float", "int"]).columns
    cat_cols = df.select_dtypes(include=["object"]).columns

    # sns.set(font_scale=0.6)  # Decrease font scale for all text elements

    num_plots = len(num_cols) + len(cat_cols)
    rows = (num_plots + 2) // 3
    cols = 3
    fig, axes = plt.subplots(rows, cols, figsize=(15, rows * 5))
    fig.tight_layout(pad=4.0, h_pad=8)  # Increase vertical spacing between plots

    plot_index = 0

    for col in num_cols:
        ax = axes[plot_index // cols, plot_index % cols]
        plt.sca(ax)
        sns.histplot(data=df, x=col, kde=True)
        plt.title(f"Distribución de {col}")
        plot_index += 1

    for col in cat_cols:
        ax = axes[plot_index // cols, plot_index % cols]
        plt.sca(ax)
        sns.countplot(data=df, x=col)
        plt.title(f"Distribución de {col}")
        plt.xticks(rotation=45)
        plot_index += 1

    # Hide empty subplots if any
    if num_plots % cols != 0:
        for i in range(plot_index, rows * cols):
            axes[i // cols, i % cols].axis("off")

    plt.show()


def grafico_VPYT(mama):
    variables_PYT = ["CT", "CN", "CM", "PT", "PN", "PM"]
    num_variables = len(variables_PYT)
    num_filas = 2
    num_columnas = 3

    fig, axes = plt.subplots(num_filas, num_columnas, figsize=(10, 6))

    for i, variable in enumerate(variables_PYT):
        fila = i // num_columnas
        columna = i % num_columnas

        # Cuenta la frecuencia de cada categoría, incluyendo los valores perdidos
        frecuencia = mama[variable].value_counts(dropna=False)

        # Crea el gráfico de torta en el subgráfico correspondiente
        axes[fila, columna].pie(frecuencia.values, labels=frecuencia.index, autopct="%1.1f%%")
        axes[fila, columna].set_title(f"Distribución de {variable}")

    # Ajusta los espacios entre subgráficos
    plt.tight_layout()

    # Muestra los gráficos
    plt.show()
