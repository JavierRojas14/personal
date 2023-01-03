import random
import numpy as np
import matplotlib.pyplot as plt

DICCIONARIO_REGIONES = {1: 'EastEurope',
                        2: 'LatAm',
                        3: 'NorthAfrica',
                        4: 'SubSaharian',
                        5: 'WesternDem',
                        6: 'EastAsia',
                        7: 'SouthEastAsia',
                        8: 'SouthAsia',
                        9: 'Pacific',
                        10: 'Caribbean'}

SEMILLA_PSEUDOALEATORIA = '0115'
COLUMNAS_SALUD = ['wef_imort', 'who_alc2000', 'who_tobt', 'wdi_exph']


def obtener_mitad_casos_df(df_largo):
    # Primero seria obtener el rango de indexes del df
    # Después sería obtener cuantos elementos se requieren
    # Después sería obtener la cantidad de elementos, pero sin repetirse
    cincuenta_porciento_casos = int(round(df_largo / 2, 0))
    indices_a_elegir = (random.sample(
        range(df_largo), cincuenta_porciento_casos))
    return indices_a_elegir


def obtener_submuestra(df):
    random.seed(SEMILLA_PSEUDOALEATORIA)

    columnas_a_utilizar = ['undp_hdi', 'ccodealp', 'ht_region', 'gle_cgdpc',
                           'imf_pop'] + COLUMNAS_SALUD

    casos_a_obtener = obtener_mitad_casos_df(df.shape[0])
    df_cincuenta_casos = df.iloc[casos_a_obtener]
    df_cincuenta_columnas_a_utilizar = df_cincuenta_casos[columnas_a_utilizar]

    df_cincuenta_columnas_a_utilizar['ht_region'] = df_cincuenta_columnas_a_utilizar['ht_region'].replace(
        DICCIONARIO_REGIONES)

    return df_cincuenta_columnas_a_utilizar


def obtener_descripciones_variables(objeto):
    descripcion_variables_continuas = objeto.describe()
    print(descripcion_variables_continuas)

    variables_continuas = descripcion_variables_continuas.columns
    variables_discretas = set(objeto.columns) - set(variables_continuas)

    for variable_discreta in variables_discretas:
        print(objeto[variable_discreta].value_counts())


def calcular_observaciones_perdidas(dataframe, var, print_list=False):
    cantidad_lista_nan = dataframe[var].value_counts(dropna=False)
    porcentaje_lista_nan = dataframe[var].value_counts('%', dropna=False)

    if np.nan in cantidad_lista_nan.index:
        cantidad_nan = cantidad_lista_nan[np.nan]
        porcentaje_nan = porcentaje_lista_nan[np.nan]

    else:
        cantidad_nan = 0
        porcentaje_nan = 0

    if print_list:
        return cantidad_nan, porcentaje_nan, porcentaje_lista_nan

    else:
        return cantidad_nan, porcentaje_nan


def graficar_histograma(sample_df, full_df, var, true_mean, sample_mean=False):
    plt.hist(sample_df[var])

    if sample_mean:
        plt.axvline(sample_df[var].mean(), color='yellow')

    if true_mean:
        plt.axvline(full_df[var].mean(), color='red')

    plt.show()
