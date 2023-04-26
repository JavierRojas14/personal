import random


import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer

from sklearn.metrics import classification_report, roc_auc_score

random.seed(1)

DICCIONARIO_REEMPLAZO = {
    "worry": 0,
    "happiness": 1,
    "sadness": 0,
    "love": 1,
    "surprise": 1,
    "fun": 1,
    "relief": 1,
    "hate": 0,
    "empty": 0,
    "enthusiasm": 1,
    "boredom": 0,
    "anger": 0,
}


lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()

STOPWORDS_INGLES = set(stopwords.words("english"))


def preprocesar_texto_lema(texto):
    tokens = texto.split()
    filtro_stop_words = [palabra for palabra in tokens if palabra not in STOPWORDS_INGLES]
    lematizacion = [lemmatizer.lemmatize(palabra, "v") for palabra in filtro_stop_words]

    texto_juntado = " ".join(lematizacion)

    return texto_juntado


def preprocesar_texto_stem(texto):
    tokens = texto.split()
    filtro_stop_words = [palabra for palabra in tokens if palabra not in STOPWORDS_INGLES]
    stemmizacion = [stemmer.stem(palabra, "v") for palabra in filtro_stop_words]

    texto_juntado = " ".join(stemmizacion)

    return texto_juntado


def obtener_100_palabras_mas_frecuentes(serie_textos):
    """Funcion que permite obtener las 100 palabras mas frecuentes de una lista de
    textos

    :param serie_palabras: Array de textos a analizar
    :type serie_palabras: pd.Series

    :returns: Las 100 palabras mas frecuentes para el array de textos
    :rtype: pd.DataFrame
    """
    count_vectorizer = CountVectorizer(stop_words="english")
    count_vectorizer_fit = count_vectorizer.fit_transform(serie_textos)
    words = count_vectorizer.get_feature_names_out()
    words_freq = count_vectorizer_fit.toarray().sum(axis=0)

    conteo_palabras = pd.DataFrame(words_freq, index=words, columns=["conteo"])
    conteo_palabras = conteo_palabras.sort_values("conteo", ascending=False)
    conteo_palabras = conteo_palabras.reset_index(names="palabra")

    return conteo_palabras


def codificar_sentimientos(vector_objetivo):
    vector_objetivo_codificado = vector_objetivo.replace(DICCIONARIO_REEMPLAZO)
    neutrales = vector_objetivo_codificado[vector_objetivo_codificado == "neutral"]
    neutrales = neutrales.apply(lambda x: random.choice([0, 1]))
    vector_objetivo_codificado.iloc[neutrales.index] = neutrales
    vector_objetivo_codificado = vector_objetivo_codificado.astype(int)

    return vector_objetivo_codificado


def resumir_resultados_grid_cv(diccionario_resultados):
    df_resultados = pd.DataFrame(diccionario_resultados)
    df_resultados["params_str"] = df_resultados["params"].astype(str)

    return df_resultados


def graficar_resultados_grid_cv(resultado_df):
    sns.lineplot(data=resultado_df, x="params_str", y="mean_test_score", marker="o")
    plt.tick_params(axis="x", labelrotation=90)


def analizar_resultados_grid_cv(diccionario_resultados):
    df_resultados = resumir_resultados_grid_cv(diccionario_resultados)
    graficar_resultados_grid_cv(df_resultados)

    return df_resultados


def entrenar_y_obtener_desempeno_modelo_en_grilla(modelo_grilla, X_train, X_test, y_train, y_test):
    modelo_grilla.fit(X_train, y_train)
    print("\n\n--------------Resultados Conjunto de Entrenamiento-----------------")
    print("Los resultados en la busqueda de hiperparametros son:")
    resultados_grilla = analizar_resultados_grid_cv(modelo_grilla.cv_results_)
    plt.show()
    print(f"Los mejores parametros fueron: {modelo_grilla.best_params_}")
    print(f"El mejor desempeno fue: {modelo_grilla.best_score_}")

    print("\n\n--------------Resultados Conjunto de Validacion-----------------")
    yhat = modelo_grilla.predict(X_test)
    roc = roc_auc_score(y_test, yhat)
    print("Los resultados en el conjunto de validacion son:")
    print(classification_report(y_test, yhat))
    print(f"El ROC fue de: {roc}")

    print("---------------------------------------------------------------------")

    return modelo_grilla, resultados_grilla
