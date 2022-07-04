"""Prepara datos para pronóstico.

Cree el archivo data_lake/business/features/precios-diarios.csv. Este
archivo contiene la información para pronosticar los precios diarios de la
electricidad con base en los precios de los días pasados. Las columnas
correspoden a las variables explicativas del modelo, y debe incluir,
adicionalmente, la fecha del precio que se desea pronosticar y el precio
que se desea pronosticar (variable dependiente).

En la carpeta notebooks/ cree los notebooks de jupyter necesarios para
analizar y determinar las variables explicativas del modelo.

Desde la ruta data_lake/business/ se crea una copia del archivo precios-diarios.csv 
en la ruta data_lake/business/features/ con el nombre precios_diarios.csv incluyendo 
la fecha y el precio que se desea pronosticar (variable dependiente).

"""
import shutil


def make_features():
    try:
        shutil.copy('data_lake/business/precios-diarios.csv',
                    'data_lake/business/features/precios_diarios.csv')
    except:
        raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    make_features()
