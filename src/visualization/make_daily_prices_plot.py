"""Crea un grafico de lines que representa los precios promedios diarios.

Usando el archivo data_lake/business/precios-diarios.csv, crea un grafico de
lines que representa los precios promedios diarios.

El archivo se debe salvar en formato PNG en data_lake/business/reports/figures/daily_prices.png.

"""
import pandas as pd
import matplotlib.pyplot as plt


def load_data(in_file, name_column_date):
    datos = pd.read_csv(in_file, index_col=None, sep=',', header=0)
    datos[name_column_date] = pd.to_datetime(datos["fecha"])
    return datos


def create_plot(datos, out_file):
    x = datos.fecha
    y = datos.precio

    plt.figure(figsize=(15, 6))
    plt.plot(x, y, 'b', label='Promedio Diario')
    plt.title('Promedio Diario')
    plt.xlabel('Fecha')
    plt.ylabel('Precio')
    plt.legend()
    plt.xticks(rotation="vertical")
    plt.savefig(out_file)


def make_daily_prices_plot():
    try:
        in_file = r'data_lake/business/precios-diarios.csv'
        name_column_date = 'fecha'
        out_file = "data_lake/business/reports/figures/daily_prices.png"
        datos = load_data(in_file, name_column_date)
        create_plot(datos, out_file)

    except:
        raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":

    import doctest

    doctest.testmod()
    make_daily_prices_plot()
