from tkinter.ttk import Separator
import pandas as pd
import numpy as np


def separador():
    print("")
    print("-" * 80)
    print("░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print("")


def proceso():
    separador()
    labels = ['a', 'b', 'c', 'd', 'e']
    data = np.arange(4, 9)

    series = pd.Series(data, index=labels)
    print("Serie de datos con etiquestas")
    print(series)
    # acceder valor
    separador()
    print("Mostrar valor de la serie usando indice etiquetado")
    print(series['c'])

    separador()
    # datos distinto tipo
    data = ['Jose', 49, 'Mar', 46]
    series = pd.Series(data)
    print("Nueva serie agregando datos de distinto tipo, sin indice, \
        creados con etiquetas enteras desde el 0 en adelante")
    print(series)
    # datos directos
    print("Nueva serie con datos etiquetados, las etiquetas son Strings")
    series = pd.Series([1000, 500, 1200, 700], [
                       'Emp01', 'Emp02', 'Emp03', 'Empe4'])
    print(series)

    separador()
    series1 = pd.Series([1000, 500, 1200, 700], [
                        'Emp01', 'Emp02', 'Emp03', 'Empe4'])
    series2 = pd.Series([1050, 1500, 2200, 700], [
                        'Emp01', 'Emp02', 'Emp03', 'Empe4'])
    print(f"Serie 1:\n{series1}")
    print(f"Serie 2:\n{series2}")
    series3 = series1+series2
    print(f"Serie 3 es Serie 1 + Serie 2:\n{series3}")

    separador()
    print("Dataframes")
    filas = ['tienda1', 'tienda2', 'tienda3', 'tienda4']
    print(f"Filas:\n{filas}")
    columnas = ['articulo1', 'articulo2', 'articulo3']
    print(f"Columnas :\n{columnas}")
    datos = [[124, 100, 200], [200, 100, 300],
             [300, 100, 400], [400, 100, 500]]
    print(f"Datos :\n{datos}")
    dataframe = pd.DataFrame(datos, index=filas, columns=columnas)
    print(f"dataframe Producto filas x columnas x datos\n{dataframe}")
    separador()
    print(f"Seleccionar fila en indice asociado a etiqueta ['tienda2']\n\
        {dataframe.loc['tienda2']}")
    separador()
    print(f"Seleccionar 2 filas asociado a etiquetas [['tienda2','tienda3']]\n\
        {dataframe.loc[['tienda2','tienda3']]}")
    separador()
    print(f"Seleccionar columna asociada a etiquetas ['articulo3']\n\
        {dataframe['articulo3']}")
    print(f"Seleccionar celda especifica con coordenadas ['tienda2','articulo3']\n\
        {dataframe.loc['tienda2','articulo3']}")

    separador()
    print(f"Asignar un valor a toda una columna")
    dataframe['articulo4'] = 25
    print(dataframe)

    separador()
    print(f"Agregar nueva columna en base a valores derivados (total) del Dataframe")
    dataframe['total'] = dataframe['articulo1'] +\
        dataframe['articulo2'] +\
        dataframe['articulo3'] +\
        dataframe['articulo4']
    print(dataframe)

    separador()
    print(f"Eliminar columna (axis=1), sin persistir el cambio:\n\
        {dataframe.drop(['total'], axis=1)}")
    print(f"{dataframe}")
    separador()
    print(f"{dataframe}")
    dataframe.drop(['total'], axis=1, inplace=True)
    print(f"Eliminar columna (axis=1), persisitiendo el cambio:\n{dataframe}")

    separador()
    condition = dataframe > 200
    print(f"Filtrar dataframe con matrix de condiciones a nivel de celda (dataframe > 200)\n\
        {dataframe[condition]}")
    separador()
    condition = (dataframe['articulo1'] >= 200) & \
        (dataframe['articulo2'] >= 100)
    print(f"Filtrar dataframe con matrix de condiciones aplicadas a las filas\n\
        {dataframe[condition]}")

    separador()
    new_column = '1 2 3 4'.split()
    dataframe['indices'] = new_column
    print(f"Se agrega nueva columna :\n\
        {dataframe}")
    dataframe = dataframe.set_index('indices')
    print(f"Se cambia la estructura de indices desde una columna etiquetada:\n\
        {dataframe}")

    separador()
    incomplete_data = [[np.nan, 100, 200], [np.nan, 100, 300],
                       [300, np.nan, 400], [400, 100, 500]]
    dataframe = incomplete_data
    print(f"Data frame con valores NaN :\n\
        {dataframe}")
    

proceso()
