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


def graficar_variable_numerica(serie_numerica, nombre_grafico):
    sns.histplot(serie_numerica)
    plt.axvline(serie_numerica.mean(), color='tomato')
    plt.title(nombre_grafico)
    plt.show()

def analizar_variables_numericas(df_numericas):
    display(df_numericas.describe())

    for columna_numerica, serie_numerica in df_numericas.items():
        graficar_variable_numerica(serie_numerica, columna_numerica)

    
