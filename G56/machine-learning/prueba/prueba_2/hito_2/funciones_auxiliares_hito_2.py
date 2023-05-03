import preproc_nyc_sqf as pre
import pandas as pd


def preprocesar_vectores_objetivos(df):
    df_suitable, _, _ = pre.create_suitable_dataframe(df)
    df_suitable["arstmade"] = df_suitable["arstmade"].replace({"N": 0, "Y": 1})

    mask = (
        (df_suitable["pf_hands"] == "Y")
        | (df_suitable["pf_wall"] == "Y")
        | (df_suitable["pf_grnd"] == "Y")
        | (df_suitable["pf_drwep"] == "Y")
        | (df_suitable["pf_ptwep"] == "Y") 
        | (df_suitable["pf_baton"] == "Y")
        | (df_suitable["pf_hcuff"] == "Y")
        | (df_suitable["pf_pepsp"] == "Y")
        | (df_suitable["pf_other"] == "Y")
    )

    df_suitable["violent"] = mask * 1

    return df_suitable


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


def codificar_a_one_hot(df, nombre_columna, serie_columna):
    """Funcion que codifica una variable categorica no binaria a formato Leave-One-Out Encoding.
    Ademas, une esta codificacion al DataFrame y elimina la variable original.
    :param df: Es el DataFrame que contiene la variable que se quiere codificar
    :type df: pd.DataFrame
    :param nombre_columna: Es el nombre de la variable que se quiere codificar
    :type nombre_columna: str
    :param serie_columna: Es el conjunto de datos de la variable que se quiere codificar
    :type serie_columna: pd.Series
    :returns: Retorna el DataFrame con la variable codificada según el formato Leave-One-Out Encoding.
    Además, sin la variable original
    :rtype: pd.DataFrame
    """
    tmp = df.copy()

    tmp = tmp.join(pd.get_dummies(serie_columna, drop_first=True, prefix=nombre_columna))
    tmp = tmp.drop(columns=nombre_columna)

    return tmp


def unir_codificacion_one_hot_vars_categoricas(df):
    """Función que itera en todas las variables categóricas presentes en un DataFrame para llevarlas
    a formato Leave-One-Out Encoding.
    :param df: Es el DataFrame que contiene nuestras variables categoricas a codificar
    :type df: pd.DataFrame
    :returns: El DataFrame con todas las variables categóricas codificadas a Leave-One-Out Encoding
    :rtype: pd.DataFrame
    """
    tmp = df.copy()

    _, categoricas = separar_df_a_numericas_categoricas(df)
    for nombre_columna, serie_columna in categoricas.items():
        tmp = codificar_a_one_hot(tmp, nombre_columna, serie_columna)

    return tmp
