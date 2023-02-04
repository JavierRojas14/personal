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

def separar_vector_objetivo_e_indep(df, vector_objetivo):
    X = df.drop(columns='income')
    y = df['income']

    return X, y

def calcular_roc_cross_val(df, vector_objetivo, cantidad_folds):
    X, y = separar_vector_objetivo_e_indep(df, vector_objetivo)
    X_escalado = StandardScaler().fit_transform(X)

    roc_acumulado = cross_val_score(LogisticRegression(), X=X_escalado, y=y, cv=cantidad_folds, 
                                    scoring='roc_auc')
    
    return roc_acumulado

