from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score

def separar_vector_objetivo_e_indep(df, vector_objetivo):
    X = df.drop(columns=vector_objetivo)
    y = df[vector_objetivo]

    return X, y

def calcular_roc_cross_val(regresor, cv, scoring, df, vector_objetivo):
    X, y = separar_vector_objetivo_e_indep(df, vector_objetivo)
    X_escalado = StandardScaler().fit_transform(X)

    roc_acumulado = cross_val_score(regresor, X=X_escalado, y=y, cv=cv, 
                                    scoring=scoring)
    
    return roc_acumulado

