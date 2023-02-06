from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score

def separar_vector_objetivo_e_indep(df, vector_objetivo):
    '''Funcion que permite separar un DataFrame en sus variables independientes y vector objetivo

    :param df: Es el DataFrame que se quiere separar en vars independientes y vector objetivo
    :type df: pd.DataFrame

    :param vector_objetivo: Es la variable dependiente o vector objetivo que se utilizara en un
    modelo predictivo
    :type vector_objetivo: str

    :returns: Una tulpa de DataFrames con las variables dependientes y una serie del vector
    objetivo
    :rtype: tuple
    '''
    X = df.drop(columns=vector_objetivo)
    y = df[vector_objetivo]

    return X, y

def calcular_roc_cross_val(regresor, cv, scoring, df, vector_objetivo):
    '''Función que calcula una métrica de desempeño para un cálculo de K-Folds de un regresor
    indicado por el usuario. Previo al cálculo de los K-Folds, las variables independientes se
    estandarizan.

    :param regresor: Es el modelo que se quiere utilizar para predecir el vector_objetivo
    :type regresor: Cualquier tipo de modelo/regresor estadístico

    :param cv: Es la cantidad de K-Folds que se quieren hacer para realizar la validación cruzada
    :type cv: int

    :param scoring: Es la métrica que se quiere utilizar para medir el desempeño de los modelos
    creados durante los K-Folds
    :type scoring: str

    :param df: Es el DataFrame que contiene las variables independientes y el vector objetivo
    que se quieren modelar
    :type df: pd.DataFrame

    :param vector_objetivo: Es la variable dependiente que se quiere predecir con el regresor/modelo
    estadístico. Debe estar presente en el parámetro df
    :type vector_objetivo: str

    :returns: Una lista con el desempeño de cada modelo en cada K-Fold realizado.
    :rtype: list
    '''
    X, y = separar_vector_objetivo_e_indep(df, vector_objetivo)
    X_escalado = StandardScaler().fit_transform(X)

    roc_acumulado = cross_val_score(regresor, X=X_escalado, y=y, cv=cv, 
                                    scoring=scoring)
    
    return roc_acumulado

