import preproc_nyc_sqf as pre


def preprocesar_vectores_objetivos(df):
    df_suitable, _, _ = pre.create_suitable_dataframe(df)
    df_suitable["arstmade"] = df_suitable["arstmade"].replace({"N": 0, "Y": 1})

    mask = (
        (df_suitable["pf_hands"] == "Y")
        | (df_suitable["pf_wall"] == "Y")
        | (df_suitable["pf_grnd"] == "Y")
        | (df_suitable["pf_drwep"] == "Y")
        | (df_suitable["pf_ptwep"] == "Y")
        | (df_suitable["pf_baton"] == "Y")
        | (df_suitable["pf_hcuff"] == "Y")
        | (df_suitable["pf_pepsp"] == "Y")
        | (df_suitable["pf_other"] == "Y")
    )

    df_suitable["violent"] = mask * 1

    return df_suitable
