import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.metrics import classification_report
from sklearn.model_selection import GridSearchCV

sns.set_style()
plt.rcParams["figure.figsize"] = (12, 6)


# Función para obtener la información de valor del atributo
def calculate_iv(df, target):
    """
    Calculate the information value (IV) of a feature in a dataset.

    Parameters:
    df (pandas.DataFrame): the dataset
    target (str): the name of the target variable to calculate IV for

    Returns:
    float: the information value (IV) of the feature
    """
    valores, item, diferencia = [], [], []
    lista = {}

    # Revisión del target y sus valores en 1 y 0
    for i in range(len(df[target].value_counts())):
        if df[target].dtypes != "int64":
            valores.append(df[target].value_counts("%")[i])
            diferencia.append(1 - df[target].value_counts("%")[i])
            item.append(df[target].unique()[i])

            # Crear lista y posterior DataFrame para manipular la data
            lista = {"1": valores, "0": diferencia, target: item}
            df_values = pd.DataFrame(lista)

            # Obtener los valores de la división y el log por separado y almacenarlos
            df_values["DIVISION"] = df_values["1"] / df_values["0"]
            df_values["LOG"] = df_values["DIVISION"].map(lambda x: log(x))

            # Obtener valores de cada atributo
            df_values["VALUE"] = (df_values["1"] - df_values["0"]) * df_values["LOG"]

            # Obtener IV
            iv = df_values["VALUE"].sum()
        else:
            iv = 0

    return iv


# Función para la categorización del valor
def categorize_iv(iv):
    """
    Categorize the information value (IV) of a feature based on commonly used cut-off values.

    Parameters:
    iv (float): the information value (IV) of a feature

    Returns:
    str: the category of the IV value (e.g., 'weak', 'moderate', 'strong')
    """
    if iv < 0.02:
        return "not useful"
    elif iv < 0.1:
        return "weak"
    elif iv < 0.3:
        return "moderate"
    elif iv < 0.5:
        return "strong"
    else:
        return "suspicious"


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
    plt.show()


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
    tmp = tmp.drop(columns=["CATEGORIA", "SUBCATEGORIA", "CODIGO_COMUNA", "ID_CASO"])

    # Paso 3: Categorizar la edad en rangos etarios
    tmp["RANGO_ETARIO"] = pd.cut(
        tmp["EDAD"],
        [-np.inf, 1, 4, 14, 64, np.inf],
        labels=["Menores 1 anio", "1 a 4 anios", "5 a 14 anios", "15 a 64 anios", "65 y mas anios"],
    )
    tmp = tmp.drop(columns=["EDAD"])

    # Paso 4: Filtrar filas con al menos 1 examen
    columnas_examenes = ["CT", "CN", "CM", "PT", "PN", "PM"]
    tmp = tmp.dropna(subset=columnas_examenes, how="all")

    # Paso 5: Eliminar columnas de fechas
    columnas_fechas = ["FECHA_DIAGNOSTICO", "FECHA_DEFUNCION", "FECHA_INICIO_TTO", "FECHA_FIN_TTO"]
    for columna in columnas_fechas:
        tmp[columna] = pd.to_datetime(tmp[columna], yearfirst=True)

    tmp["DIAS_TTO"] = (tmp["FECHA_FIN_TTO"] - tmp["FECHA_INICIO_TTO"]).dt.days
    tmp["PROYECCION_DIAS"] = (tmp["FECHA_DEFUNCION"] - tmp["FECHA_DIAGNOSTICO"]).dt.days

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
    tmp = tmp.fillna("SO")

    # Paso 8: Convertir todas las columnas a variables indicadoras (one-hot encoding)
    # tmp = pd.get_dummies(tmp, drop_first=True)

    return tmp


# Función para gráficos para ver distribución de c/variable
def plot_variables(df):
    num_cols = df.select_dtypes(include=["float", "int"]).columns
    cat_cols = df.select_dtypes(include=["object"]).columns

    # Paleta de colores asociada al cáncer de mamas
    breast_cancer_palette = ["#D61A46", "#00AEEF", "#8A7967", "#7B1FA2", "#FF7F00", "#70AD47"]
    sns.set_palette(breast_cancer_palette)

    # Gráficos para variables numéricas
    for col in num_cols:
        plt.figure(figsize=(8, 6))
        sns.histplot(data=df, x=col, kde=True)
        plt.title(f"Distribución de {col}")
        plt.show()

    # Gráficos para variables categóricas
    for col in cat_cols:
        plt.figure(figsize=(8, 6))
        sns.countplot(data=df, x=col)
        plt.title(f"Distribución de {col}")
        plt.xticks(rotation=45)
        plt.show()
