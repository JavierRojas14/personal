# Regularización

## Regularización Paramétrica

- Normas L1 y L2

## Conceptos básicos en Machine Learning

Se puede dividir en 4 grandes pasos:

1. Dividir:
    - Corresponde en:
        1. Dividir en vectores predictivos y vector objetivo
        2. Dividir en datos de entrenamiento y datos para testear el modelo
        - Por lo tanto, se generan 4 subconjuntos de datos.
2. Entrenar:
    - Corresponde a definir que funcion matemática/algoritmo queremos utilizar para hacer nuestro modelo predictivo
    - Con los datos de entrenamiento, se entrena a nuestro modelo

3. Predicir:
    - Una vez entrenado nuestro modelo, procedemos a hacer predicciones
    - En este caso, se utilizan los vectores predictivos del set de testeo para hacer las predicciones

4. Evaluar:
    - Cuando ya realizamos nuestra predicciones, procedemos a hacer la evaluación de nuestro modelo. Esto se realiza contrastando el vector objetivo del set de testeo, y las predicciones realizadas previamente
    - Para variables continuas, se puede utilizar el Mean Squared Error
    - Para variables categoricas, se puede utilizar una matriz de confusion