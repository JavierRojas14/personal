#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report
from sklearn.metrics import roc_curve, auc, f1_score, precision_score, recall_score


def plot_classification_report(y_true, y_hat):
    """
    plot_classification_report: Genera una visualización de los puntajes reportados con la función `sklearn.metrics.classification_report`.

    Parámetros de ingreso:
        - y_true: Un vector objetivo de validación.
        - y_hat: Un vector objetivo estimado en función a la matriz de atributos de validación y un modelo entrenado.

    Retorno:
        - Un gráfico generado con matplotlib.pyplot

    """
    # process string and store in a list
    f1_score_value_0 = f1_score(y_true=y_true, y_pred=y_hat, pos_label=0)
    precision_score_value_0 = precision_score(y_true=y_true, y_pred=y_hat, pos_label=0)
    recall_score_value_0 = recall_score(y_true=y_true, y_pred=y_hat, pos_label=0)

    f1_score_value_1 = f1_score(y_true=y_true, y_pred=y_hat, pos_label=1)
    precision_score_value_1 = precision_score(y_true=y_true, y_pred=y_hat, pos_label=1)
    recall_score_value_1 = recall_score(y_true=y_true, y_pred=y_hat, pos_label=1)

    f1_score_value_avg = np.mean([f1_score_value_0, f1_score_value_1])
    precision_score_value_avg = np.mean([precision_score_value_0, precision_score_value_1])
    recall_score_value_avg = np.mean([recall_score_value_0, recall_score_value_1])

    colors = ["dodgerblue", "tomato", "purple", "orange"]

    plt.yticks([1.0, 2.0, 3.0], ["Precision", "Recall", "f1"])
    plt.xlim(0, 1)

    plt.plot(precision_score_value_0, [1], marker="x", color=colors[0])
    plt.plot(recall_score_value_0, [2], marker="x", color=colors[0], label=f"Class: {0}")
    plt.plot(f1_score_value_0, [3], marker="x", color=colors[0])

    plt.plot(precision_score_value_1, [1], marker="x", color=colors[1])
    plt.plot(recall_score_value_1, [2], marker="x", color=colors[1], label=f"Class: {1}")
    plt.plot(f1_score_value_1, [3], marker="x", color=colors[1])

    plt.plot(precision_score_value_avg, [1], marker="o", color="forestgreen")
    plt.plot(recall_score_value_avg, [2], marker="o", color="forestgreen", label="Avg")
    plt.plot(f1_score_value_avg, [3], marker="o", color="forestgreen")


def grid_plot_batch(df, cols, plot_type):
    """
    grid_plot_batch: Genera una grilla matplotlib para cada conjunto de variables.

    Parámetros de ingreso:
        - df: un objeto pd.DataFrame
        - cols: cantidad de columnas en la grilla.
        - plot_type: tipo de gráfico a generar. Puede ser una instrucción genérica de matplotlib o seaborn.

    Retorno:
        - Una grilla generada con plt.subplots y las instrucciones dentro de cada celda.

    """
    # calcular un aproximado a la cantidad de filas
    rows = int(np.ceil(df.shape[1] / cols))
    # para cada columna

    for index, (colname, serie) in enumerate(df.iteritems()):
        plt.subplot(rows, cols, index + 1)
        plot_type(x=serie)
        plt.tight_layout()


def identify_high_correlations(df, threshold=0.7):
    """
    identify_high_correlations: Genera un reporte sobre las correlaciones existentes entre variables, condicional a un nivel arbitrario.

    Parámetros de ingreso:
        - df: un objeto pd.DataFrame, por lo general es la base de datos a trabajar.
        - threshold: Nivel de correlaciones a considerar como altas. Por defecto es .7.

    Retorno:
        - Un pd.DataFrame con los nombres de las variables y sus correlaciones
    """

    # extraemos la matriz de correlación con una máscara booleana
    tmp = df.corr().mask(abs(df.corr()) < threshold, df)
    # convertimos a long format
    tmp = pd.melt(tmp)
    # agregamos una columna extra que nos facilitará los cruces entre variables
    tmp["var2"] = list(df.columns) * len(df.columns)
    # reordenamos
    tmp = tmp[["variable", "var2", "value"]].dropna()
    # eliminamos valores duplicados
    tmp = tmp[tmp["value"].duplicated()]
    # eliminamos variables con valores de 1
    return tmp[tmp["value"] < 1.00]


def plot_roc(model, y_true, X_test, model_label=None):
    """TODO: Docstring for plot_roc.

    :model: TODO
    :y_true: TODO
    :X_test: TODO
    :model_label: TODO
    :returns: TODO

    """
    class_pred = model.predict_proba(X_test)[:1]
    false_positive_rates, true_positive_rates, _ = roc_curve(y_true, class_pred)
    store_auc = auc(false_positive_rates, true_positive_rate)

    if model_label is not None:
        tmp_label = f"{model_label}: {round(store_auc, 3)}"
    else:
        tmp_label = None
    plt.plot(false_positive_rates, true_positive_rates, label=tmp_label)
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
