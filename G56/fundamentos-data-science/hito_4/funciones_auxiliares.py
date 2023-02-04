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

def calcular_perdida_de_datos(df_completa):
    cantidad_valores_originales = len(df_completa)
    cantidad_valores_droppeados = len(df_completa.dropna())
    return round(1 - (cantidad_valores_droppeados / cantidad_valores_originales), 2)

REEMPLAZO_OCCUPATION = {'white-collar': ['Prof-specialty', 'Exec-managerial', 'Adm-clerical', 'Sales',
                                         'Tech-support'],
                        'blue-collar': ['Craft-repair', 'Machine-op-inspct', 'Transport-moving',
                                        'Handlers-cleaners', 'Farming-fishing', 'Protective-serv',
                                        'Priv-house-serv'],
                        'others': ['Other-service', 'Armed-Forces']}

REEMPLAZO_WORKCLASS = {'federal-gov': ['Federal-gov'],
                       'state-level-gov': ['State-gov', 'Local-gov'],
                       'self-employed': ['Self-emp-inc', 'Self-emp-not-inc'],
                       'unemployed': ['Never-worked', 'Without-pay']}

REEMPLAZO_EDUCATION = {'preschool': ['Preschool'],
                       'elementary-school': ['1st-4th', '5th-6th'],
                       'high-school': ['7th-8th', '9th', '10th','11th', '12th', 'HS-grad'],
                       'college': ['Assoc-voc', 'Assoc-acdm', 'Some-college'],
                       'university': ['Bachelors', 'Masters', 'Prof-school', 'Doctorate']}

REEMPLAZO_MARITAL = {'married': ['Married-civ-spouse', 'Married-spouse-absent','Married-AF-spouse'],
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
REEMPLAZO_SEX = {0: ['Male'], 1: ['Female']}

RECODIFICACION_ENUNCIADO_1 = [REEMPLAZO_OCCUPATION, REEMPLAZO_WORKCLASS, REEMPLAZO_EDUCATION,
                              REEMPLAZO_MARITAL, REEMPLAZO_COUNTRY, REEMPLAZO_INCOME, REEMPLAZO_SEX]

def recodificar_variable(df, diccionario_cambio):
    tmp = df.copy()
    for valor_nuevo, valores_antiguos in diccionario_cambio.items():
        tmp = tmp.replace(valores_antiguos, valor_nuevo)

    return tmp

def recodificar_enunciado_uno(df):
    recodificada = df.copy()
    for dict_recod in RECODIFICACION_ENUNCIADO_1:
        recodificada = recodificar_variable(recodificada, dict_recod)
    
    return recodificada

def codificar_a_one_hot(df, nombre_columna, serie_columna):
    tmp = df.copy()

    df_unida = tmp.join(pd.get_dummies(serie_columna, drop_first=True))
    df_unida = df_unida.drop(columns=nombre_columna)
    
    return df_unida

def one_hot_todas_las_categoricas(df):
    tmp = df.copy()

    _, categoricas = separar_df_a_numericas_categoricas(df)
    for nombre_columna, serie_columna in categoricas.items():
        tmp = codificar_a_one_hot(tmp, nombre_columna, serie_columna)
    
    return tmp
