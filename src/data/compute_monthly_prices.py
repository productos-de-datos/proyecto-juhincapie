def compute_monthly_prices():
    """Compute los precios promedios mensuales.

    Usando el archivo data_lake/cleansed/precios-horarios.csv, compute el prcio
    promedio mensual. Las
    columnas del archivo data_lake/business/precios-mensuales.csv son:

    * fecha: fecha en formato YYYY-MM-DD

    * precio: precio promedio mensual de la electricidad en la bolsa nacional



    """
    import pandas as pd
    df = pd.read_csv("data_lake/cleansed/precios-horarios.csv",
                     index_col=None, header=0)
    df["fecha"] = pd.to_datetime(df["fecha"])
    df['año_mes'] = ((df['fecha'].dt.year).astype(int)).astype(
        str)+"-"+((df['fecha'].dt.month).astype(int)).astype(str)

    dfm = df[["año_mes", "precio"]]

    compute_month_prices = dfm.groupby(
        "año_mes").mean({"precio_promedio": "precio"})
    compute_month_prices.reset_index(inplace=True)
    dfa = df[["fecha", "año_mes"]]
    compute_month_prices = pd.merge(
        dfa, compute_month_prices, on="año_mes", how="left")
    compute_month_prices = compute_month_prices[["fecha", "precio"]]
    compute_month_prices.to_csv(
        "data_lake/business/precios-mensuales.csv", index=None, header=True)
    #raise NotImplementedError("Implementar esta función")
    return


compute_monthly_prices()


if __name__ == "__main__":
    import doctest

    doctest.testmod()
