import os

import numpy as np
import pandas as pd


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
    dataframe = pd.DataFrame(incomplete_data, index=filas, columns=columnas)
    print(f"Data frame con valores NaN :\n\
        {dataframe}")
    sin_na_dataframe = dataframe.dropna(axis=1)
    print(f"Data frame sin valores NaN (elimina columnas enteras si axis=1):\n\
        {sin_na_dataframe}")
    fill_na_dataframe = dataframe.fillna(value=90)
    print(f"Data frame sin valores NaN rellenados con 90:\n\
        {fill_na_dataframe}")
    media = dataframe.mean()
    print(f"La media es igual a:\n{media}")
    avgfill_na_dataframe = dataframe.fillna(value=media)
    print(f"Dataframe donde Nan son rellenos con el promedio por columna:\n\
        {avgfill_na_dataframe}")
    dataframe = avgfill_na_dataframe

    separador()
    data1 = dataframe.copy()
    data2 = dataframe.copy()
    print(f"df1:\n{data1}")
    print(f"df2:\n{data2}")
    data_join_axis0 = pd.concat([data1, data2], axis=0)
    data_join_axis1 = pd.concat([data1, data2], axis=1)
    print(f"df join axis 0 or to the column:\n{data_join_axis0}")
    print(f"df join axis 1 or to the row:\n{data_join_axis1}")

    separador()
    print(f"{dataframe}")
    print(f"Valores unicos en columna ['articulo1'] :\n\
    {dataframe['articulo1'].unique()}")
    print(f"frecuencias de valores en columna ['articulo1'] :\n\
    {dataframe['articulo1'].value_counts()}")

    separador()
    print(f"{data_join_axis0}")
    data_join_axis0= data_join_axis0.apply(lambda x: x*3)
    print(f"DF con operador lambda x: x*3:\n\
        {data_join_axis0}")

    separador()
    print(f"{data_join_axis0}")
    print(f"Columnas del DF:\n{data_join_axis0.columns}")
    print(f"Indices del DF:\n{data_join_axis0.index}")
    print(f"DF ordenada por valor de 'articulo3':\n{data_join_axis0.sort_values(['articulo3'])}")
    print(f"Descripción del DF:\n{data_join_axis0.describe()}")

    separador()
    script_path= os.path.abspath(os.path.dirname(__file__))
    csv_file= script_path + "/m61_dataTotal.csv"
    print(f"Script path es:{script_path}")
    print(f"Escribiendo a path es:{csv_file}")
    data_join_axis0.to_csv(csv_file)
    print(f"Escritura hecha con exito")
    new_dataframe = pd.read_csv(csv_file)
    print(f"DF desde archivo {csv_file} :\n{new_dataframe}")


proceso()
