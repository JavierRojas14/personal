

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


def obtener_mitad_casos_df(largo_df):
    """Funcion para obtener el 50% de los indices de un pandas dataframe. Los indices se eligen
    de forma aleatoria

    :param largo_df: Es el largo (len) del dataframe que se quiere obtener su 50% de registros
    :type largo_df: int

    :return: Retorna una lista de indices aleatorios 
    :rtype: list
    """
    # Primero seria obtener el rango de indexes del df
    # Después sería obtener cuantos elementos se requieren
    # Después sería obtener la cantidad de elementos, pero sin repetirse
    cincuenta_porciento_casos = int(round(largo_df / 2, 0))
    indices_a_elegir = (random.sample(
        range(largo_df), cincuenta_porciento_casos))
    return indices_a_elegir


def obtener_submuestra(df):
    """Funcion para obtener una submuestra de un dataframe. La muestra contiene el 50% de los
    registros originales del dataframe, y se eligen de forma aleatoria

    :param df: Dataframe de donde se quiere obtener una submuestra
    :type df: pd.DataFrame

    :return: Submuestra del Dataframe original, que contiene el 50% de los registros
    :rtype: pd.DataFrame
    """
    random.seed(SEMILLA_PSEUDOALEATORIA)

    columnas_a_utilizar = ['undp_hdi', 'ccodealp', 'ht_region', 'gle_cgdpc',
                           'imf_pop'] + COLUMNAS_SALUD

    casos_a_obtener = obtener_mitad_casos_df(df.shape[0])
    df_cincuenta_casos = df.iloc[casos_a_obtener]
    df_cincuenta_columnas_a_utilizar = df_cincuenta_casos[columnas_a_utilizar]

    df_cincuenta_columnas_a_utilizar['ht_region'] = df_cincuenta_columnas_a_utilizar['ht_region'].replace(
        DICCIONARIO_REGIONES)

    return df_cincuenta_columnas_a_utilizar



def analizar_variable_continua(serie_variable, titulo_grafico):
    sns.histplot(serie_variable)
    plt.title(titulo_grafico)
    plt.show()

def obtener_descripciones_variables(df_a_describir):
    """Funcion para mostrar los descriptores estadisticos de tendencia central de las variables
    continuas, ademas de las frecuencias de los valores de variables discretas de un Dataframe

    :param df_a_describir: Dataframe que se quiere describir
    :type df_a_describir: pd.DataFrame

    :return: Nada
    :rtype: None
    """
    descripcion_variables_continuas = df_a_describir.describe()
    display(descripcion_variables_continuas)

    variables_continuas = descripcion_variables_continuas.columns
    variables_discretas = set(df_a_describir.columns) - \
        set(variables_continuas)
    
    for variable_continua in variables_continuas:
        analizar_variable_continua(df_a_describir[variable_continua], variable_continua)

    for variable_discreta in variables_discretas:
        print(f'> Var: {variable_discreta}')
        analizar_variable_discreta(df_a_describir[variable_discreta], False)


def calcular_observaciones_perdidas(dataframe, var, print_list=False):
    """Funcion que retorna la cantidad y el porcentaje de datos faltantes en una columna de un
    DataFrame. Ademas, puede retornar una lista detallada de la frecuencia/porcentaje de los valores
    de la columna a analizar

    :param dataframe: Dataframe en donde se quiere observar la cantidad de valores faltantes
    :type dataframe: pd.DataFrame

    :param var: Nombre de la columna que se quiere analizar dentro del DataFrame
    :type var: str

    :param print_list: Booleano que indica si es que se quiere imprimir la frecuencia de valores
    de la columna var
    :type print_list: Bool

    :return: Una tupla con la cantidad de valores faltanes, el porcentaje de valores faltantes y,
    opcionalemnte, la lista de valores de la columna var
    :rtype: tuple
    """
    cantidad_lista_nan = dataframe[var].value_counts(dropna=False)
    porcentaje_lista_nan = dataframe[var].value_counts('%', dropna=False)

    if np.nan in cantidad_lista_nan.index:
        cantidad_nan = cantidad_lista_nan[np.nan]
        porcentaje_nan = porcentaje_lista_nan[np.nan]

    else:
        cantidad_nan = 0
        porcentaje_nan = 0

    if print_list:
        registros_faltantes = dataframe[dataframe[var].isna()]
        lista_paises_faltantes = registros_faltantes['ccodealp'].unique()
        return cantidad_nan, porcentaje_nan, lista_paises_faltantes

    else:
        return cantidad_nan, porcentaje_nan


def graficar_histograma(sample_df, full_df, var, true_mean, sample_mean=False):
    """Funcion que grafica la distribucion de datos de una columna presente en un DataFrame obtenido
    desde un DataFrame mas grande

    :param sample_df: Muestra de full_df que se grafica en el histograma
    :type sample_df: pd.DataFrame

    :param full_df: Dataframe completo de donde se obtiene sample_df 
    :type full_df: pd.DataFrame

    :param var: Columna de sample_df que se quiere graficar su distribucion
    :type var: str

    :param true_mean: Valor booleano que indica si se quiere graficar la media 
    de la columna var en full_df
    :type true_mean: Bool

    :param true_mean: Valor booleano que indica si se quiere graficar la media 
    de la columna var en sample_df
    :type true_mean: Bool

    :return: Nada
    :rtype: None
    """
    plt.hist(sample_df[var])

    if sample_mean:
        plt.axvline(sample_df[var].mean(), color='yellow')

    if true_mean:
        plt.axvline(full_df[var].mean(), color='red')

    plt.show()


def graficar_dotplot_variable(dataframe, plot_var, plot_by, statistic='mean', global_stat=False):
    """Funcion que grafica la media/mediana de una variable, luego de haber agrupado un DataFrame
    por el parametro plot_by

    :param dataframe: DataFrame que contiene los datos que se quieren graficar
    :type dataframe: pd.DataFrame

    :param plot_var: Variable que se quiere graficar, que esta presente en dataframe
    :type plot_var: str

    :param plot_by: Columna que se utilizara para agrupar el dataframe y que correspondera al eje x
    del grafico 
    :type plot_by: str

    :param statistic: Valor estadistico que se quiere graficar. Puede ser mean o median
    :type statistic: str

    :param global_stat: Valor booleano que indica si se quiere graficar la media global de la
    variable plot_var en dataframe previo a la agrupacion
    :type global_stat: Bool

    :return: Nada
    :rtype: None
    """
    df_agrupado = dataframe.groupby(plot_by)[plot_var]

    if statistic == 'mean':
        df_agrupado = df_agrupado.mean()
        medida_global = dataframe[plot_var].mean()

    elif statistic == 'median':
        df_agrupado = df_agrupado.median()
        medida_global = dataframe[plot_var].median()

    plt.plot(df_agrupado, 'o')
    plt.xticks(rotation=90)
    plt.ylabel(statistic)
    plt.title(
        f'Statistic: {statistic}\nVariable: {plot_var}\nAgrupado por: {plot_by}')

    if global_stat:
        plt.axhline(medida_global)

    plt.show()
