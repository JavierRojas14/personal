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
REEMPLAZO_SEX = {0: ['Male'], 1: ['Female']}

RECODIFICACION_ENUNCIADO_1 = [REEMPLAZO_OCCUPATION, REEMPLAZO_WORKCLASS, REEMPLAZO_EDUCATION,
                              REEMPLAZO_MARITAL, REEMPLAZO_COUNTRY, REEMPLAZO_INCOME, REEMPLAZO_SEX]


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
    sns.histplot(data=serie_numerica, ax=axis[0])
    axis[0].axvline(serie_numerica.mean(), color='tomato')
    sns.boxplot(data=serie_numerica, ax=axis[1])

    plt.title(nombre_grafico)
    plt.show()


def analizar_distr_todas_las_variables_numericas(df_numericas):
    print('Analizando todas las variables numericas \n')
    display(df_numericas.describe())

    for columna_numerica, serie_numerica in df_numericas.items():
        graficar_distribucion_variable_numerica(
            serie_numerica, columna_numerica)


def graficar_distribucion_variable_categorica(serie_categorica, nombre_grafico):
    serie_conteo = serie_categorica.value_counts()
    print(nombre_grafico)
    print(serie_conteo)

    sns.countplot(y=serie_categorica, order=serie_conteo.index)
    plt.title(nombre_grafico)
    plt.show()


def analizar_dist_todas_las_variables_categoricas(df_categoricas):
    print('Analizando todas las variables categoricas \n')
    for columna_categorica, serie_categorica in df_categoricas.items():
        graficar_distribucion_variable_categorica(
            serie_categorica, columna_categorica)


def analizar_valores_faltantes(variables_a_analizar):
    valores_faltantes = variables_a_analizar.isnull().sum()
    porcentaje_faltantes = round(valores_faltantes * 100 / len(variables_a_analizar), 2)

    faltantes_resumen = pd.DataFrame({'columna': variables_a_analizar.columns,
                                      'cantidad_na': valores_faltantes,
                                      'porcentaje_na': porcentaje_faltantes})
    display(faltantes_resumen)

    msno.matrix(variables_a_analizar)


def analizar_variables_indpendientes(df_independientes):
    numericas, categoricas = separar_df_a_numericas_categoricas(df_independientes)
    analizar_distr_todas_las_variables_numericas(numericas)
    analizar_dist_todas_las_variables_categoricas(categoricas)
    analizar_valores_faltantes(df_independientes)


def mostrar_perdida_de_datos(df_completa):
    cantidad_valores_originales = len(df_completa)
    cantidad_valores_droppeados = len(df_completa.dropna())
    porcentaje_droppeo = (cantidad_valores_droppeados / cantidad_valores_originales)
    cambio = round((1 - porcentaje_droppeo) * 100, 2)

    print(f'Al droppear todos los valores faltantes en la DataFrame se pierde el {cambio}% '
          f'de los datos totales')


def analizar_correlacion_todas_las_variables(df_variables):
    corr = df_variables.corr()
    sns.heatmap(corr, cmap='Blues', annot=True)
    plt.show()


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

    tmp = tmp.join(pd.get_dummies(serie_columna, drop_first=True), rsuffix=f'_{nombre_columna}')
    tmp = tmp.drop(columns=nombre_columna)

    return tmp


def one_hot_vars_categoricas(df):
    tmp = df.copy()

    _, categoricas = separar_df_a_numericas_categoricas(df)
    for nombre_columna, serie_columna in categoricas.items():
        tmp = codificar_a_one_hot(tmp, nombre_columna, serie_columna)

    return tmp

def preprocesar_y_recodificar_enunciado_uno(df):
    tmp = df.copy()

    tmp = tmp.replace('?', np.nan)
    tmp = tmp.dropna()
    tmp = recodificar_enunciado_uno(tmp)
    tmp = one_hot_vars_categoricas(tmp)
    tmp.columns = tmp.columns.str.replace('-', '_')

    return tmp

############################ Enunciado 2

def corregir_var_numerica_con_comillas(serie_semi_numerica):
    return serie_semi_numerica.str.replace('"', '').astype(float)

def reasginar_variables_numericas(df):
    tmp = df.copy()

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

    vars_erroneas = ['age', 'goout', 'health']
    for variable_erronea in vars_erroneas:
        tmp[variable_erronea] = corregir_var_numerica_con_comillas(tmp[variable_erronea])

    return tmp

REEMPLAZO_SCHOOL = {0: ['GP'], 1: ['MS']}
REEMPLAZO_SEX = {0: ['F'], 1: ['M']}
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
                 'sex': REEMPLAZO_SEX,
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

def recodificar_vars_binarias_enunciado_2(df):
    tmp = df.copy()

    for variable, dict_reemplazo in CAMBIO_HITO_2.items():
        tmp[variable] = recodificar_variable(tmp[variable], dict_reemplazo)
    
    return tmp

def preprocesar_y_recodificar_enunciado_dos(df):
    tmp = df.copy()

    tmp = tmp.replace(['nulidade', 'sem validade', 'zero'], np.nan)
    tmp = cambiar_vars_numericas_en_string(tmp)
    tmp = reasginar_variables_numericas(tmp)
    tmp = recodificar_vars_binarias_enunciado_2(tmp)
    tmp = one_hot_vars_categoricas(tmp)

    return tmp
    

