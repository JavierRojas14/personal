"""Funciones auxiliares para analizar la distribucion de datos en un DataFrame. Puede:

- Analizar la distribucion de variables categoricas y numericas
- Analizar valores faltantes
"""

import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

import missingno as msno


def separar_df_a_numericas_categoricas(df):
    """Esta funcion permite separar un DataFrame en sus variables categoricas (que están en formato
    string u object) y las variables numéricas (que estén en algún formato numérico como int o
    float)

    :param df: Es el DataFrame que se quiere separar
    :type df: pd.DataFrame

    :returns: Una tupla con las variables numericas y categoricas
    :rtype: tuple
    """
    numericas = df.select_dtypes("number")
    categoricas = df.select_dtypes("object")
    return numericas, categoricas


def graficar_distribucion_variable_numerica(serie_numerica, nombre_grafico):
    """Esta funcion permite graficar la distribución de una variable numérica con un histograma
    y un gráfico de cajas y bigotes. Además, muestra la media en el histograma

    :param serie_numerica: Es la Serie o el conjunto de datos de la variable numérica que se quiere
    graficar
    :type serie_numerica: pd.Series

    :param nombre_grafico: Es el nombre que se le quiere poner al gráfico
    :type nombre_grafico: str
    """
    fig, axis = plt.subplots(1, 2)
    print('-----------------------------------------')
    sns.histplot(data=serie_numerica, ax=axis[0])
    axis[0].axvline(serie_numerica.mean(), color="tomato")
    sns.boxplot(data=serie_numerica, ax=axis[1])

    plt.title(nombre_grafico)
    plt.show()
    print('-----------------------------------------')


def analizar_distr_todas_las_variables_numericas(df_numericas):
    """Función que permite iterar en todas las variables numéricas de un DataFrame para graficar
    su distribución. Además, muestra las medidas de tendencia central.

    :param df_numericas: Es el DataFrame que contiene todas las variables numéricas a analizar
    :type df_numericas: pd.DataFrame
    """
    if not(df_numericas.empty):
        print("Analizando todas las variables numericas \n")
        display(df_numericas.describe())

        for columna_numerica, serie_numerica in df_numericas.items():
            graficar_distribucion_variable_numerica(serie_numerica, columna_numerica)


def graficar_distribucion_variable_categorica(serie_categorica, nombre_grafico):
    """Funcion que permite analizar la distribución y frecuencia de cada categoria dentro de una
    variable categorica. Además, genera un gráfico de barras con la frecuencia y el valor de la
    categoria en la variable. Este gráfico esta ordenado descendientemente.

    :param serie_categorica: Es la pd.Series o conjunto de datos categoricos que se quieren analizar
    :type serie_categorica: pd.Series

    :param nombre_grafico: Es el título que se le quiere poner al gráfico
    :type nombre_grafico: str
    """
    frecuencias = serie_categorica.value_counts()
    porcentajes = serie_categorica.value_counts("%")
    total = pd.DataFrame(
        {"Frecuencia": frecuencias, "Porcentaje": porcentajes}, index=frecuencias.index
    )
    print('-----------------------------------------')
    display(total)

    sns.countplot(y=serie_categorica, order=frecuencias.index)
    plt.title(nombre_grafico)
    plt.show()
    print('-----------------------------------------')


def analizar_dist_todas_las_variables_categoricas(df_categoricas):
    """Función que permite iterar en todas las variables categóricas de un DataFrame para graficar
    su distribución.

    :param df_numericas: Es el DataFrame que contiene todas las variables categóricas a analizar
    :type df_numericas: pd.DataFrame
    """
    print("Analizando todas las variables categoricas \n")
    for columna_categorica, serie_categorica in df_categoricas.items():
        graficar_distribucion_variable_categorica(serie_categorica, columna_categorica)


def analizar_valores_faltantes(variables_a_analizar):
    """Función que permite cuantificar la cantidad de valores faltantes en un DataFrame que se
    quiera analizar. Muestra la cantidad y el porcentaje de valores faltantes por columna/variable
    presente en la base de datos

    :param variables_a_analizar: Es el conjunto de variables que se quieren analizar
    :type variables_a_analizar: pd.DataFrame
    """
    valores_faltantes = variables_a_analizar.isnull().sum()
    porcentaje_faltantes = round(valores_faltantes * 100 / len(variables_a_analizar), 2)

    faltantes_resumen = pd.DataFrame(
        {"cantidad_na": valores_faltantes, "porcentaje_na": porcentaje_faltantes}
    )
    display(faltantes_resumen)

    msno.matrix(variables_a_analizar)


def analizar_distribucion_y_faltantes_variables(df):
    """Función que permite analizar la distribucion de variables en un DataFrame. Esta función
    clasifica y separa las variables en numéricas y categóricas. Luego, analiza y grafica la
    distribución de ambos tipos de variables y finalmente analiza la cantidad
    de valores faltantes.

    :param df: Es la base de datos que contiene todas las variables que se quiere observar su
    distribucion y valores faltantes
    :type df: pd.DataFrame
    """
    numericas, categoricas = separar_df_a_numericas_categoricas(df)
    analizar_distr_todas_las_variables_numericas(numericas)
    analizar_dist_todas_las_variables_categoricas(categoricas)
    analizar_valores_faltantes(df)


def mostrar_perdida_de_datos(df_completa):
    """Función que cuantifica la cantidad y el porcentaje de datos perdidos cuando se utiliza
    .dropna() en una base de datos de forma global.

    :param df_completa: Base de datos que se quiere saber cuánto cambia cuando se utiliza
    .dropna() de forma global.
    :type df_completa: pd.DataFrame
    """
    cantidad_valores_originales = len(df_completa)
    cantidad_valores_droppeados = len(df_completa.dropna())
    porcentaje_droppeo = cantidad_valores_droppeados / cantidad_valores_originales
    cambio = round((1 - porcentaje_droppeo) * 100, 2)

    print(
        f"Al droppear todos los valores faltantes en la DataFrame se pierde el {cambio}% "
        f"de los datos totales"
    )


def analizar_correlacion_todas_las_variables(df_variables):
    """Funcion que calcula y grafica la correlacion entre variables en una base de datos

    :param df_variables: Es la base de datos que contiene las variables a analizar
    :type df_variables: pd.DataFrame
    """
    corr = df_variables.corr()
    sns.heatmap(corr, cmap="Blues", annot=True)
    plt.show()
