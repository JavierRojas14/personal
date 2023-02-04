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

def crear_formula_econometria(df, vector_objetivo):
    variables_independientes = ' + '.join(df.drop(columns=vector_objetivo).columns)
    formula_final = f'income ~ {variables_independientes}'

    return formula_final

def crear_modelo_logistico(df, vector_objetivo):
    formula = crear_formula_econometria(df, vector_objetivo)
    modelo = smf.logit(formula, df).fit()

    return modelo



