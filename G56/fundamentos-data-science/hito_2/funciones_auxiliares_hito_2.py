import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

import missingno as msno

REEMPLAZO_OCCUPATION = {
    'white-collar': ['Prof-specialty', 'Exec-managerial', 'Adm-clerical', 'Sales', 'Tech-support'],
    'blue-collar':
    ['Craft-repair', 'Machine-op-inspct', 'Transport-moving', 'Handlers-cleaners',
     'Farming-fishing', 'Protective-serv', 'Priv-house-serv'],
    'others': ['Other-service', 'Armed-Forces']}

REEMPLAZO_WORKCLASS = {'federal-gov': ['Federal-gov'],
                       'state-level-gov': ['State-gov', 'Local-gov'],
                       'self-employed': ['Self-emp-inc', 'Self-emp-not-inc'],
                       'unemployed': ['Never-worked', 'Without-pay']}

REEMPLAZO_EDUCATION = {'preschool': ['Preschool'],
                       'elementary-school': ['1st-4th', '5th-6th'],
                       'high-school': ['7th-8th', '9th', '10th', '11th', '12th', 'HS-grad'],
                       'college': ['Assoc-voc', 'Assoc-acdm', 'Some-college'],
                       'university': ['Bachelors', 'Masters', 'Prof-school', 'Doctorate']}

REEMPLAZO_MARITAL = {
    'married': ['Married-civ-spouse', 'Married-spouse-absent', 'Married-AF-spouse'],
    'divorced': ['Divorced'],
    'separated': ['Separated'],
    'widowed': ['Widowed']}

REEMPLAZO_COUNTRY = {'america': ["United-States", "Mexico", "Puerto-Rico", "Canada", "El-Salvador",
                                 "Cuba", "Jamaica", "Dominican-Republic", "Guatemala", "Columbia",
                                 "Haiti", "Nicaragua", "Peru", "Ecuador", "Trinadad&Tobago",
                                 "Outlying-US(Guam-USVI-etc)"],
                     'asia': ["Philippines", "India", "China", "Japan", "Vietnam", "Taiwan",
                              "Iran", "Hong", "Thailand", "Cambodia", "Laos"],
                     'europe': ["Germany", "England", "Italy", "Poland", "Portugal", "Greece",
                                "France", "Ireland", "Yugoslavia", "Scotland", "Honduras",
                                "Hungary", "Holand-Netherlands"],
                     'oceania': [],
                     'africa': ["South"]}

REEMPLAZO_INCOME = {0: ['<=50K'], 1: ['>50K']}
REEMPLAZO_GENDER = {0: ['Male'], 1: ['Female']}

CAMBIO_HITO_1 = {'occupation': REEMPLAZO_OCCUPATION,
                 'workclass': REEMPLAZO_WORKCLASS,
                 'education': REEMPLAZO_EDUCATION,
                 'marital-status': REEMPLAZO_MARITAL,
                 'native-country': REEMPLAZO_COUNTRY,
                 'income': REEMPLAZO_INCOME,
                 'gender': REEMPLAZO_GENDER}


def analizar_vector_objetivo_discreto(serie_variable):
    '''Esta función permite ver la frecuencia, distribución y cantidad de valores faltantes
    de un vector objetivo discreto

    :param serie_variable: Es el pandas Series del vector objetivo discreto
    :type serie_variable: pd.Series
    '''
    frecuencias = serie_variable.value_counts()
    porcentajes = serie_variable.value_counts('%')
    total = pd.DataFrame({'Frecuencia': frecuencias,
                         'Porcentaje': porcentajes}, index=frecuencias.index)
    display(total)

    sns.histplot(serie_variable)
    plt.show()

    numero_faltantes = serie_variable.isnull().sum()
    print(f'La variable presentó {numero_faltantes} valores faltantes')
    msno.matrix(pd.DataFrame(serie_variable))
    plt.show()


def separar_df_a_numericas_categoricas(df):
    '''Esta funcion permite separar un DataFrame en sus variables categoricas (que están en formato
    string u object) y las variables numéricas (que estén en algún formato numérico como int o
    float)

    :param df: Es el DataFrame que se quiere separar
    :type df: pd.DataFrame

    :returns: Una tupla con las variables numericas y categoricas
    :rtype: tuple
    '''
    numericas = df.select_dtypes('number')
    categoricas = df.select_dtypes('object')
    return numericas, categoricas


def graficar_distribucion_variable_numerica(serie_numerica, nombre_grafico):
    '''Esta funcion permite graficar la distribución de una variable numérica con un histograma
    y un gráfico de cajas y bigotes. Además, muestra la media en el histograma

    :param serie_numerica: Es la Serie o el conjunto de datos de la variable numérica que se quiere
    graficar
    :type serie_numerica: pd.Series

    :param nombre_grafico: Es el nombre que se le quiere poner al gráfico
    :type nombre_grafico: str
    '''
    fig, axis = plt.subplots(1, 2)
    sns.histplot(data=serie_numerica, ax=axis[0])
    axis[0].axvline(serie_numerica.mean(), color='tomato')
    sns.boxplot(data=serie_numerica, ax=axis[1])

    plt.title(nombre_grafico)
    plt.show()


def analizar_distr_todas_las_variables_numericas(df_numericas):
    '''Función que permite iterar en todas las variables numéricas de un DataFrame para graficar
    su distribución. Además, muestra las medidas de tendencia central.

    :param df_numericas: Es el DataFrame que contiene todas las variables numéricas a analizar
    :type df_numericas: pd.DataFrame
    '''
    print('Analizando todas las variables numericas \n')
    display(df_numericas.describe())

    for columna_numerica, serie_numerica in df_numericas.items():
        graficar_distribucion_variable_numerica(
            serie_numerica, columna_numerica)


def graficar_distribucion_variable_categorica(serie_categorica, nombre_grafico):
    '''Funcion que permite analizar la distribución y frecuencia de cada categoria dentro de una
    variable categorica. Además, genera un gráfico de barras con la frecuencia y el valor de la
    categoria en la variable. Este gráfico esta ordenado descendientemente.

    :param serie_categorica: Es la pd.Series o conjunto de datos categoricos que se quieren analizar
    :type serie_categorica: pd.Series

    :param nombre_grafico: Es el título que se le quiere poner al gráfico
    :type nombre_grafico: str
    '''
    serie_conteo = serie_categorica.value_counts()
    print(nombre_grafico)
    print(serie_conteo)

    sns.countplot(y=serie_categorica, order=serie_conteo.index)
    plt.title(nombre_grafico)
    plt.show()


def analizar_dist_todas_las_variables_categoricas(df_categoricas):
    '''Función que permite iterar en todas las variables categóricas de un DataFrame para graficar
    su distribución.

    :param df_numericas: Es el DataFrame que contiene todas las variables categóricas a analizar
    :type df_numericas: pd.DataFrame
    '''
    print('Analizando todas las variables categoricas \n')
    for columna_categorica, serie_categorica in df_categoricas.items():
        graficar_distribucion_variable_categorica(
            serie_categorica, columna_categorica)


def analizar_valores_faltantes(variables_a_analizar):
    '''Función que permite cuantificar la cantidad de valores faltantes en un DataFrame que se
    quiera analizar. Muestra la cantidad y el porcentaje de valores faltantes por columna/variable
    presente en la base de datos

    :param variables_a_analizar: Es el conjunto de variables que se quieren analizar
    :type variables_a_analizar: pd.DataFrame
    '''
    valores_faltantes = variables_a_analizar.isnull().sum()
    porcentaje_faltantes = round(
        valores_faltantes * 100 / len(variables_a_analizar), 2)

    faltantes_resumen = pd.DataFrame({
        'cantidad_na': valores_faltantes,
        'porcentaje_na': porcentaje_faltantes})
    display(faltantes_resumen)

    msno.matrix(variables_a_analizar)


def analizar_variables_indpendientes(df_independientes):
    '''Función que permite analizar las variables independientes elegidas para un modelo de
    predicción. Esta función clasifica y separa las variables en numéricas y categóricas. Luego,
    analiza y grafica la distribución de ambos tipos de variables y finalmente analiza la cantidad
    de valores faltantes.

    :param df_independientes: Es la base de datos que contiene todas las variables independientes
    a ser utilizadas en el modelo predictivo
    :type df_independientes: pd.DataFrame
    '''
    numericas, categoricas = separar_df_a_numericas_categoricas(
        df_independientes)
    analizar_distr_todas_las_variables_numericas(numericas)
    analizar_dist_todas_las_variables_categoricas(categoricas)
    analizar_valores_faltantes(df_independientes)


def mostrar_perdida_de_datos(df_completa):
    '''Función que cuantifica la cantidad y el porcentaje de datos perdidos cuando se utiliza
    .dropna() en una base de datos de forma global.

    :param df_completa: Base de datos que se quiere saber cuánto cambia cuando se utiliza
    .dropna() de forma global.
    :type df_completa: pd.DataFrame
    '''
    cantidad_valores_originales = len(df_completa)
    cantidad_valores_droppeados = len(df_completa.dropna())
    porcentaje_droppeo = (cantidad_valores_droppeados /
                          cantidad_valores_originales)
    cambio = round((1 - porcentaje_droppeo) * 100, 2)

    print(f'Al droppear todos los valores faltantes en la DataFrame se pierde el {cambio}% '
          f'de los datos totales')


def analizar_correlacion_todas_las_variables(df_variables):
    '''Funcion que calcula y grafica la correlacion entre variables en una base de datos

    :param df_variables: Es la base de datos que contiene las variables a analizar
    :type df_variables: pd.DataFrame
    '''
    corr = df_variables.corr()
    sns.heatmap(corr, cmap='Blues', annot=True)
    plt.show()


def cambiar_valores_en_variable(serie, diccionario_cambio):
    '''Funcion que permite reemplazar los valores de una serie basado en un diccionario. El
    diccionario de cambio tiene el formato {valor_nuevo, valores_a_reemplazar}

    :param serie: Conjunto de datos que se les quiere cambiar/reemplazar alguna imputación
    :type serie: pd.Series

    :param diccionario_cambio: Diccionario que especifica el valor nuevo que se quiere ingresar
    en la serie de datos, y los valores antiguos a reemplazar

    :returns: Una copia del conjunto de datos con los valores reemplazados según el diccionario
    :rtype: pd.Series
    '''
    tmp = serie.copy()
    for valor_nuevo, valores_antiguos in diccionario_cambio.items():
        tmp = tmp.replace(valores_antiguos, valor_nuevo)

    return tmp


def recodificar_variables(df, diccionario_var_a_cambiar):
    '''Funcion que itera en un diccionario de variables a cambiar dentro de un DataFrame. Luego,
    reemplaza los valores presentes en cada variable según lo indicado en el diccionario presente
    para cada variable.

    :param df: Es el DataFrame que contiene las variables que quieren ser recodificadas
    :type df: pd.DataFrame

    :param diccionario_var_a_cambiar: Es un diccionario que contiene el nombre de la variable a
    cambiar como llave, y que tiene como valor el diccionario de cambio específico para la variable.
    :type diccionario_var_a_cambiar: dict

    :returns: El DataFrame con todas las variables estipuladas en diccionario_var_a_cambiar
    modificadas
    :rtype: pd.DataFrame
    '''
    tmp = df.copy()

    for variable, dict_reemplazo in diccionario_var_a_cambiar.items():
        tmp[variable] = cambiar_valores_en_variable(
            tmp[variable], dict_reemplazo)

    return tmp


def codificar_a_one_hot(df, nombre_columna, serie_columna):
    '''Funcion que codifica una variable categorica no binaria a formato Leave-One-Out Encoding.
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
    '''
    tmp = df.copy()

    tmp = tmp.join(pd.get_dummies(serie_columna, drop_first=True),
                   rsuffix=f'_{nombre_columna}')
    tmp = tmp.drop(columns=nombre_columna)

    return tmp


def unir_codificacion_one_hot_vars_categoricas(df):
    '''Función que itera en todas las variables categóricas presentes en un DataFrame para llevarlas
    a formato Leave-One-Out Encoding.

    :param df: Es el DataFrame que contiene nuestras variables categoricas a codificar
    :type df: pd.DataFrame

    :returns: El DataFrame con todas las variables categóricas codificadas a Leave-One-Out Encoding
    :rtype: pd.DataFrame
    '''
    tmp = df.copy()

    _, categoricas = separar_df_a_numericas_categoricas(df)
    for nombre_columna, serie_columna in categoricas.items():
        tmp = codificar_a_one_hot(tmp, nombre_columna, serie_columna)

    return tmp


def preprocesar_y_recodificar_enunciado_uno(df):
    '''Función específica que engloba el preprocesamiento y trata de valores faltantes para el
    enunciado 1 de la prueba de Fundamentos de Data Science de Desafios Latam.

    :param df: DataFrame sin modificar del enunciado 1 prueba de Fundamentos de Data Science 
    de Desafios Latam
    :type df: pd.DataFrame

    :returns: El DataFrame completamente preprocesado y sin valores faltantes
    :rtype: pd.DataFrame
    '''
    tmp = df.copy()

    tmp = tmp.replace('?', np.nan)
    tmp = tmp.dropna()
    tmp = tmp.drop(columns='educational-num')
    tmp = recodificar_variables(tmp, CAMBIO_HITO_1)
    tmp = unir_codificacion_one_hot_vars_categoricas(tmp)
    tmp.columns = tmp.columns.str.replace('-', '_')

    return tmp

# Enunciado 2


REEMPLAZO_SCHOOL = {0: ['GP'], 1: ['MS']}
REEMPLAZO_GENDER = {0: ['F'], 1: ['M']}
REEMPLAZO_ADDRESS = {0: ['U'], 1: ['R']}
REEMPLAZO_FAMSIZE = {0: ['GT3'], 1: ['LE3']}
REEMPLAZO_PSTATUS = {0: ['T'], 1: ['A']}
REEMPLAZO_SCHOOLSUP = {0: ['no'], 1: ['yes']}
REEMPLAZO_FAMSUP = {0: ['yes'], 1: ['no']}
REEMPLAZO_PAID = {0: ['no'], 1: ['yes']}
REEMPLAZO_ACTIVITIES = {0: ['yes'], 1: ['no']}
REEMPLAZO_NURSERY = {0: ['yes'], 1: ['no']}
REEMPLAZO_HIGHER = {0: ['yes'], 1: ['no']}
REEMPLAZO_INTERNET = {0: ['yes'], 1: ['no']}
REEMPLAZO_ROMANTIC = {0: ['no'], 1: ['yes']}

CAMBIO_HITO_2 = {'school': REEMPLAZO_SCHOOL,
                 'sex': REEMPLAZO_GENDER,
                 'address': REEMPLAZO_ADDRESS,
                 'famsize': REEMPLAZO_FAMSIZE,
                 'Pstatus': REEMPLAZO_PSTATUS,
                 'schoolsup': REEMPLAZO_SCHOOLSUP,
                 'famsup': REEMPLAZO_FAMSUP,
                 'paid': REEMPLAZO_PAID,
                 'activities': REEMPLAZO_ACTIVITIES,
                 'nursery': REEMPLAZO_NURSERY,
                 'higher': REEMPLAZO_HIGHER,
                 'internet': REEMPLAZO_INTERNET,
                 'romantic': REEMPLAZO_ROMANTIC}


def corregir_var_numerica_con_comillas(serie_semi_numerica):
    '''Funcion que permite corregir el formato de columnas numericas interpretadas como strings.
    La columna debe tener los numeros entre comillas (")

    :param serie_semi_numerica: Es el conjunto de datos numericos, que estan erroneamente imputados
    y presenta comillas
    :type serie_semi_numerica: pd.Series

    :returns: El conjunto de datos correctamente interpretados como valores flotantes
    :rtype: pd.Series
    '''
    return serie_semi_numerica.str.replace('"', '').astype(float)


def corregir_variables_numericas(df):
    '''Corrige las variables numericas presentes en el enunciado_2 de la prueba de Fundamentos
    de Data Science de Desafios Latam

    :param df: Es el DataFrame que contiene las variables numericas mal imputadas
    :type df: pd.DataFrame

    :returns: Retorna el dataFrame con las variables numericas corregidas en formato float
    :rtype: pd.DataFrame
    '''
    tmp = df.copy()

    vars_erroneas = ['age', 'goout', 'health']
    for variable_erronea in vars_erroneas:
        tmp[variable_erronea] = corregir_var_numerica_con_comillas(
            tmp[variable_erronea])

    variables_numericas = ['Dalc',
                           'Fedu',
                           'G1',
                           'G2',
                           'G3',
                           'Medu',
                           'Walc',
                           'absences',
                           'age',
                           'failures',
                           'famrel',
                           'freetime',
                           'goout',
                           'health',
                           'studytime',
                           'traveltime']

    tmp[variables_numericas] = tmp[variables_numericas].astype(float)

    return tmp


def preprocesar_y_recodificar_enunciado_dos(df):
    '''Función específica que engloba el preprocesamiento y trata de valores faltantes para el
    enunciado 2 de la prueba de Fundamentos de Data Science de Desafios Latam.

    :param df: DataFrame sin modificar del enunciado 2 prueba de Fundamentos de Data Science 
    de Desafios Latam
    :type df: pd.DataFrame

    :returns: El DataFrame completamente preprocesado y sin valores faltantes
    :rtype: pd.DataFrame
    '''
    tmp = df.copy()

    tmp = tmp.replace(['nulidade', 'sem validade', 'zero'], np.nan)
    tmp = tmp.dropna()
    tmp = tmp.drop(columns='Unnamed: 0')
    tmp = corregir_variables_numericas(tmp)
    tmp = recodificar_variables(tmp, CAMBIO_HITO_2)
    tmp = unir_codificacion_one_hot_vars_categoricas(tmp)

    return tmp
