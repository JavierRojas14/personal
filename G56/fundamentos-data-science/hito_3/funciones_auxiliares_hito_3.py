import warnings

import pandas as pd

import statsmodels.formula.api as smf


def crear_formula_econometria(df, vector_objetivo):
    variables_independientes = ' + '.join(
        df.drop(columns=vector_objetivo).columns)
    formula_final = f'{vector_objetivo} ~ {variables_independientes}'

    return formula_final


def crear_modelo_logistico(df, vector_objetivo):
    formula = crear_formula_econometria(df, vector_objetivo)
    modelo = smf.logit(formula, df).fit()

    return modelo


def crear_modelo_lineal(df, vector_objetivo):
    formula = crear_formula_econometria(df, vector_objetivo)
    modelo = smf.ols(formula, df).fit()

    return modelo


def extraer_tabla_modelos(resumen_modelo):
    return pd.read_html(resumen_modelo.tables[1].as_html(), header=0, index_col=0)[0]


def obtener_tabla_factores_significativos(resumen_modelo, threshold):
    tabla_coeficientes = extraer_tabla_modelos(resumen_modelo)
    p_menor_a = tabla_coeficientes[tabla_coeficientes['P>|z|'] < threshold]

    return p_menor_a


def mostrar_valores_significativos(resumen_modelo, threshold):
    menores_a_threshold = obtener_tabla_factores_significativos(
        resumen_modelo, threshold)
    menores_a_threshold['interpretacion_coef'] = menores_a_threshold['coef'] / 4
    menores_a_threshold = menores_a_threshold[['coef', 'interpretacion_coef']]
    menores_a_threshold = menores_a_threshold.sort_values(by='coef')

    print(f'Los valores que afectan significativamente (p < {threshold}) a la variable dependiente '
          f'son: \n{menores_a_threshold.to_markdown()}')
