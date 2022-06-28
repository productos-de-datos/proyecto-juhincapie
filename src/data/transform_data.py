def ruta(year, extension):
    ruta = "data_lake/landing/{}.{}".format(year, extension)
    return ruta


def load_data(ruta, encabezado):
    import pandas as pd
    read_file = pd.read_excel(ruta(), header=encabezado)
    read_file = read_file.iloc[:, 0:25]
    read_file.columns = ['Fecha', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                         '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']
    return read_file


def save_data(read_file, year):
    read_file.to_csv("data_lake/raw/{}.csv".format(year), index=None)


def transform_data():
    """Transforme los archivos xls a csv.

    Transforme los archivos data_lake/landing/*.xls a data_lake/raw/*.csv. Hay
    un archivo CSV por cada archivo XLS en la capa landing. Cada archivo CSV
    tiene como columnas la fecha en formato YYYY-MM-DD y las horas H00, ...,
    H23.

    """
    for year in range(1995, 2022):
        if year in range(1995, 2000):
            file = load_data(year, 3, "xlsx")
            save_data(file)
        elif(year in range(2000, 2016)):
            file = load_data(year, 2, "xlsx")
            save_data(file)
        elif(year in range(2016, 2018)):
            file = load_data(year, 2, "xls")
            save_data(file)
        else:
            file = load_data(year, 0, "xlsx")
            save_data(file)


def test_answer():
    assert ruta('2021', "xlsx") == "data_lake/landing/2021.xlsx"

    # return

    #raise NotImplementedError("Implementar esta función")


# transform_data()
if __name__ == "__main__":
    import doctest

    doctest.testmod()
    transform_data()
