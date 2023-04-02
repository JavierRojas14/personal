import pandas as pd
from sklearn.metrics import mean_absolute_error, r2_score

METRICAS_REGRESION = {'MAE': mean_absolute_error,
                      'R2': r2_score}


def calcular_metricas_regresion(modelo, X_test, y_test):
    yhat = modelo.predict(X_test)
    desempenos = {}

    for nombre_metrica, funcion_metrica in METRICAS_REGRESION.items():
        metrica_calculada = funcion_metrica(y_test, yhat)
        desempenos[nombre_metrica] = metrica_calculada

    desempenos = pd.DataFrame(desempenos.values(), index=desempenos.keys(),
                              columns=['valores'])

    return desempenos


def reportar_metricas_regresion(modelo, X_test, y_test):
    tabla_metricas_calculadas = calcular_metricas_regresion(
        modelo, X_test, y_test)
    print(tabla_metricas_calculadas.to_markdown())
