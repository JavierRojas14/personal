import pandas as pd
from sklearn.metrics import mean_absolute_error, r2_score, classification_report

METRICAS_REGRESION = {'MAE': mean_absolute_error,
                      'R2': r2_score}

METRICAS_CLASIFICACION = {'classification_report': classification_report}


def calcular_metricas_clasificacion(modelo, X_test, y_test):
    yhat = modelo.predict(X_test)

    for nombre_metrica, funcion_metrica in METRICAS_CLASIFICACION.items():
        


def calcular_metricas_regresion(modelo, X_test, y_test):
    '''Funcion que calcula metricas para un modelo de regresion. Las metricas a calculcar
    estan definidas en la variable global METRICAS_REGRESION

    :param modelo: Es el modelo de regresion ya entrenado
    :type modelo: sklearn

    :param X_test: Es el conjunto de datos de validacion de las variables independientes
    :type X_test: pd.DataFrame

    :param y_test: Es el conjunto de datos de validacion del vector objetivo
    :type y_test: pd.DataFrame

    :returns: Retorna una tabla resumen con todas las metricas calculadas
    :rtype: pd.DataFrame 
    '''
    yhat = modelo.predict(X_test)
    desempenos = {}

    for nombre_metrica, funcion_metrica in METRICAS_REGRESION.items():
        metrica_calculada = funcion_metrica(y_test, yhat)
        desempenos[nombre_metrica] = metrica_calculada

    desempenos = pd.DataFrame(desempenos.values(), index=desempenos.keys(),
                              columns=['valores'])

    return desempenos


def reportar_metricas_regresion(modelo, X_test, y_test):
    '''Funcion que reporta e imprime las metricas para un modelo de regresion.

    :param modelo: Es el modelo de regresion ya entrenado
    :type modelo: sklearn

    :param X_test: Es el conjunto de datos de validacion de las variables independientes
    :type X_test: pd.DataFrame

    :param y_test: Es el conjunto de datos de validacion del vector objetivo
    :type y_test: pd.DataFrame
    '''
    tabla_metricas_calculadas = calcular_metricas_regresion(
        modelo, X_test, y_test)
    print(tabla_metricas_calculadas.to_markdown())
