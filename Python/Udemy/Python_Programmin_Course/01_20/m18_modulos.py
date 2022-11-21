""" Importar modulos en Python """
# impotar modulo
import math

# importar funcion de modulo renombrando funcion importada
#from random import randint as azar
# importar todas las funciones de un modulo, no es buena practica
from random import *

def proceso():
    """ Proceso """
    # importar parte de un modulo
    # from math import sqrt
    numero = int(input("Ingresa un numero y te dire su raiz cuadrada: "))
    print(f"La raiz cuadrada de {numero} es {math.sqrt(numero)}")
    continua = "s"
    while continua == "s":
        lanza_dado = randint(0, 100)
        print(f"El numero aleatorio es {lanza_dado}")
        continua = input("Deseas continuar? s/n: ")
        if continua == "n":
            print("Hasta la proxima")
            break

proceso()
