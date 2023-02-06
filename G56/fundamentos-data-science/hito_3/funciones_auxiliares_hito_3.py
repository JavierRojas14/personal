import warnings

import pandas as pd

import statsmodels.formula.api as smf


def crear_formula_econometria(df, vector_objetivo):
    '''Funcion para crear automáticamente la fórmula del modelo predictivo basado en la econometría

    :param df: Es el DataFrame que contiene las variables independientes a utilizar y el vector
    objetivo a predecir
    :type df: pd.DataFrame

    :param vector_objetivo: Es la variable dependiente que se quiere utilizar en el modelo 
    predictivo
    :type vector_objetivo: str

    :returns: La fórmula escrita para imputar en el modelo de statsmodels
    :rtype: str
    '''
    variables_independientes = ' + '.join(
        df.drop(columns=vector_objetivo).columns)
    formula_final = f'{vector_objetivo} ~ {variables_independientes}'

    return formula_final


def crear_modelo_logistico(df, vector_objetivo):
    '''Crea un modelo logístico, imputando automáticamente la fórmula a utilizar y ajustandolo
    inmediatamente

    :param df: Es el DataFrame que contiene las variables independientes a utilizar y el vector
    objetivo a predecir
    :type df: pd.DataFrame

    :param vector_objetivo: Es la variable dependiente que se quiere utilizar en el modelo 
    predictivo
    :type vector_objetivo: str

    :returns: El modelo entrenado con los datos entregados
    :rtype: statsmodels.BinaryResultWrapper
    '''
    formula = crear_formula_econometria(df, vector_objetivo)
    modelo = smf.logit(formula, df).fit()

    return modelo


def crear_modelo_lineal(df, vector_objetivo):
    '''Crea un modelo lineal, imputando automáticamente la fórmula a utilizar y ajustandolo
    inmediatamente

    :param df: Es el DataFrame que contiene las variables independientes a utilizar y el vector
    objetivo a predecir
    :type df: pd.DataFrame

    :param vector_objetivo: Es la variable dependiente que se quiere utilizar en el modelo 
    predictivo
    :type vector_objetivo: str
    '''
    formula = crear_formula_econometria(df, vector_objetivo)
    modelo = smf.ols(formula, df).fit()

    return modelo


def extraer_tabla_modelos(resumen_modelo):
    '''Extrae la tabla de coeficientes de un resumen de un modelo de statsmodels

    :param resumen_modelo: Es un objeto Summary de statsmodels (obtenido de la función .summary()
    de un modelo de statsmodels)
    :type resumen_modelo: statsmodels.Summary()
    
    :returns: La tabla de coeficientes en formato pd.DataFrame
    :rtype: pd.DataFrame
    '''
    return pd.read_html(resumen_modelo.tables[1].as_html(), header=0, index_col=0)[0]


def obtener_tabla_factores_significativos(resumen_modelo, threshold):
    '''Extrae la tabla de coeficientes de un resumen de un modelo de statsmodels. Además, filtra
    esta tabla según un p-value < threshold

    :param resumen_modelo: Es un objeto Summary de statsmodels (obtenido de la función .summary()
    de un modelo de statsmodels)
    :type resumen_modelo: statsmodels.Summary()

    :param threshold: Es el valor que se quiere utilizar para filtrar por p-value
    :type threshold: float
    
    :returns: La tabla de coeficientes en formato pd.DataFrame, filtrada por p-value
    :rtype: pd.DataFrame
    '''
    tabla_coeficientes = extraer_tabla_modelos(resumen_modelo)
    p_menor_a = tabla_coeficientes[tabla_coeficientes['P>|z|'] < threshold]

    return p_menor_a


def mostrar_valores_significativos(resumen_modelo, threshold):
    '''Muestra las variables independientes que tienen un valor de p-value < threshold. Además,
    ordena la tabla según el valor del coeficiente de cada variable. Finalmente, si la tabla
    de resultados corresponde a la de un modelo logístico, entonces se calcula la interpretación
    lineal de los coeficientes del modelo
    
    :param resumen_modelo: Es un objeto Summary de statsmodels (obtenido de la función .summary()
    de un modelo de statsmodels)
    :type resumen_modelo: statsmodels.Summary()

    :param threshold: Es el valor que se quiere utilizar para filtrar por p-value
    :type threshold: float
    '''
    menores_a_threshold = obtener_tabla_factores_significativos(
        resumen_modelo, threshold)
    menores_a_threshold['interpretacion_coef'] = menores_a_threshold['coef'] / 4
    menores_a_threshold = menores_a_threshold[['coef', 'interpretacion_coef']]
    menores_a_threshold = menores_a_threshold.sort_values(by='coef')

    print(f'Los valores que afectan significativamente (p < {threshold}) a la variable dependiente '
          f'son: \n{menores_a_threshold.to_markdown()}')
