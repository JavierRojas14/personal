import warnings

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

import missingno as msno

import statsmodels.api as sm
import statsmodels.formula.api as smf

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn.metrics import roc_curve, roc_auc_score


def analizar_vector_objetivo_discreto(serie_variable):
    frecuencias = serie_variable.value_counts()
    porcentajes = serie_variable.value_counts('%')
    total = pd.DataFrame({'Frecuencia': frecuencias,
                         'Porcentaje': porcentajes}, index=frecuencias.index)
    display(total)

    sns.histplot(serie_variable)
    plt.show()

    msno.matrix(pd.DataFrame(serie_variable))
    plt.show()


def separar_df_a_numericas_categoricas(df):
    numericas = df.select_dtypes('number')
    categoricas = df.select_dtypes('object')
    return numericas, categoricas


def graficar_distribucion_variable_numerica(serie_numerica, nombre_grafico):
    fig, axis = plt.subplots(1, 2)
    sns.histplot(serie_numerica, ax=axis[0])
    axis[0].axvline(serie_numerica.mean(), color='tomato')
    sns.boxplot(serie_numerica, ax=axis[1])

    plt.title(nombre_grafico)
    plt.show()


def analizar_distribucion_variables_numericas(df_numericas):
    display(df_numericas.describe())

    for columna_numerica, serie_numerica in df_numericas.items():
        graficar_distribucion_variable_numerica(
            serie_numerica, columna_numerica)


def analizar_distribucion_variables_categoricas(df_categoricas):
    for columna_categorica, serie_categorica in df_categoricas.items():
        graficar_distribucion_variable_categorica(
            serie_categorica, columna_categorica)


def graficar_distribucion_variable_categorica(serie_categorica, nombre_grafico):
    serie_conteo = serie_categorica.value_counts()
    print(nombre_grafico)
    print(serie_conteo)

    sns.countplot(y=serie_categorica, order=serie_conteo.index)
    plt.title(nombre_grafico)
    plt.show()


def analizar_valores_faltantes(variables_a_analizar):
    valores_faltantes = variables_a_analizar.isnull().sum()
    porcentaje_faltantes = round(valores_faltantes * 100 / len(variables_a_analizar), 2)

    faltantes_resumen = pd.DataFrame({'columna': variables_a_analizar.columns,
                                      'cantidad_na': valores_faltantes,
                                      'porcentaje_na': porcentaje_faltantes})
    display(faltantes_resumen)

    msno.matrix(variables_a_analizar)
