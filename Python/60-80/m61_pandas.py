import pandas as pd
import numpy as np


def separador():
    print("")
    print("-" * 80)
    print("░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print("")

def proceso():
    separador()
    labels = ['a','b','c','d','e']
    data = np.arange(4,9)

    series=pd.Series(data,index=labels)
    print("Serie de datos con etiquestas")
    print(series)
    #acceder valor
    separador()
    print("Mostrar valor de la serie usando indice etiquetado")
    print(series['c'])

    separador()
    #datos distinto tipo
    data=['Jose',49,'Mar',46]
    series=pd.Series(data)
    print("Nueva serie agregando datos de distinto tipo, sin indice, creados con etiquetas enteras desde el 0 en adelante")
    print(series)
    #datos directos
    print("Nueva serie con datos etiquetados, las etiquetas son Strings")
    series=pd.Series([1000,500,1200,700],['Emp01','Emp02','Emp03','Empe4'])
    print(series)

    series=pd.Series([1000,500,1200,700],['Emp01','Emp02','Emp03','Empe4'])

proceso()
