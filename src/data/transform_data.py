def transform_data():
    """Transforme los archivos xls a csv.

    Transforme los archivos data_lake/landing/*.xls a data_lake/raw/*.csv. Hay
    un archivo CSV por cada archivo XLS en la capa landing. Cada archivo CSV
    tiene como columnas la fecha en formato YYYY-MM-DD y las horas H00, ...,
    H23.

    """
    import pandas as pd

    def transformar_xls_a_csv(año, encabezado, extension):
        read_file = pd.read_csv(
            "data_lake/landing/{}.{}".format(año, extension), header=encabezado)
        read_file = read_file.iloc[:, 0:25]
        read_file.columns = ['Fecha', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                             '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']
        read_file.to_csv("data_lake/raw/{}.csv".format(año), index=None)

        return

    for año in range(1995, 2022):
        if año in range(1995, 2000):
            transformar_xls_a_csv(año, 3, "xlsx")
        elif(año in range(2000, 2016)):
            transformar_xls_a_csv(año, 2, "xlsx")
        elif(año in range(2016, 2018)):
            transformar_xls_a_csv(año, 2, "xls")
        else:
            transformar_xls_a_csv(año, 0, "xlsx")
    return

    #raise NotImplementedError("Implementar esta función")


transform_data()
if __name__ == "__main__":
    import doctest

    doctest.testmod()
