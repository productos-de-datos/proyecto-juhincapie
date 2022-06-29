def load_data(input):
    import pandas as pd
    file = pd.read_csv(input, index_col=None, header=0)
    return file


def average_daily_price(file):
    import pandas as pd
    subset_file = file[["fecha", "precio"]]
    subset_file["fecha"] = pd.to_datetime(subset_file["fecha"])
    compute_daily_prices = subset_file.groupby(
        "fecha").mean({"precio": "precio"})
    compute_daily_prices.reset_index(inplace=True)

    return compute_daily_prices


def save_data(compute_daily_prices, output):
    compute_daily_prices.to_csv(output, index=None, header=True)


def compute_daily_prices():
    """Compute los precios promedios diarios.

    Usando el archivo data_lake/cleansed/precios-horarios.csv, compute el prcio
    promedio diario (sobre las 24 horas del dia) para cada uno de los dias. Las
    columnas del archivo data_lake/business/precios-diarios.csv son:

    * fecha: fecha en formato YYYY-MM-DD

    * precio: precio promedio diario de la electricidad en la bolsa nacional

    """
    input = "data_lake/cleansed/precios-horarios.csv"
    output = "data_lake/business/precios-diarios.csv"
    file = load_data(input)
    compute_daily_prices = average_daily_price(file)
    save_data(compute_daily_prices, output)

    #raise NotImplementedError("Implementar esta función")


def test_values_compute_daily_prices():
    input = "data_lake/cleansed/precios-horarios.csv"
    output = "data_lake/business/precios-diarios.csv"
    file = load_data(input)

    assert average_daily_price(file).fecha.astype(str).head().tolist() == [
        "1995-07-20",
        "1995-07-21",
        "1995-07-22",
        "1995-07-23",
        "1995-07-24",
    ]
    assert average_daily_price(file).precio.head().tolist() == [
        1.4094347826086957,
        4.924333333333333,
        1.2695,
        0.9530833333333333,
        4.305916666666667,
    ]


if __name__ == "__main__":

    import doctest

    doctest.testmod()
    compute_daily_prices()
