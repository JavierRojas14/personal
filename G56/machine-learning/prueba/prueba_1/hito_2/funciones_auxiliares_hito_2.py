import random

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


def codificar_sentimientos(vector_objetivo):
    vector_objetivo_codificado = vector_objetivo.replace(DICCIONARIO_REEMPLAZO)
    neutrales = vector_objetivo_codificado[vector_objetivo_codificado == "neutral"]
    neutrales = neutrales.apply(lambda x: random.choice([0, 1]))
    vector_objetivo_codificado.iloc[neutrales.index] = neutrales
    vector_objetivo_codificado = vector_objetivo_codificado.astype(int)

    return vector_objetivo_codificado
