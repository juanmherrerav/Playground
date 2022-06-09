""" Numpy exercises """

import sys
import numpy as np


def separador():
    print("")
    print("-" * 80)
    print("░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print("")


def proceso():
    """
    Test code for Numpy
    """
    print(sys.version)
    print("hola")

    print("Crear lista Python y convertir en Numpy array lineal")
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    array1 = np.array(list1)
    print(f"Lista original :{list1}")
    print(f"Tipo Lista original:{type(list1)}")
    print(f"Arreglo Numpy  :{array1}")
    print(f"Tipo Lista original:{type(array1)}")

    separador()

    print("Crear lista bidimensional (matriz) Numpy o composicion de listas")
    list2 = [[1, 2, 4], [2, 5, 3], [3, 4, 5]]
    array2 = np.array(list2)
    print(array2)
    print(f"Tipo :{type(array2)}")

    separador()
    print("Crear lista Numpy usando arange o por generacion de rengos simple")
    # -> np.arange(0,6,1) start por  defecto es 0, step por defecto es 1
    arr = np.arange(6)
    print(arr)
    print(f"Tipo :{type(arr)}")

    separador()
    print("Crear lista Numpy usando arange o por generacion de rengos con salto")
    arr = np.arange(2, 15, 2)
    print(arr)
    print(f"Tipo :{type(arr)}")

    separador()

    print("Numpy matrix with zeroes")
    zero_matrix = np.zeros((4, 5))
    print(zero_matrix)
    print(f"Tipo :{type(zero_matrix)}")

    separador()

    print("matrix of ones")
    ones_matrix = np.ones((4, 5))
    print(ones_matrix)

    separador()
    print("matrix with linearly spaced values")
    matrix = np.linspace(2, 6, 40)
    print(matrix)

    separador()

    print("identity matrix, function is called numpy.eye to avoid confusion with i from imaginary numbers")
    identity_matrix = np.eye(7)
    print(identity_matrix)

    separador()

    print("Matrix with random values using Uniform distribution between [0,1]")
    # uniform distribution [0,1]
    random_matrix = np.random.rand(4, 5)
    print(random_matrix)

    separador()

    print("Matrix with random values using Standard Normal distribution (mean=0, stdev=1).")
    print("filled with random floats sampled from a standard normal distribution of mean 0 and variance 1")
    # Standard Normal distribution (mean=0, stdev=1).
    random_matrix_standard_normal = np.random.randn(30)
    print(random_matrix_standard_normal)
    # _ = plt.hist(random_matrix_standard_normal, bins = 25)

    separador()

    print("Return random integers from the \"discrete uniform\" distribution of the specified dtype in the \"half-open\" ")
    print(
        "interval [low, high). If high is None (the default), then results are from [0, low)")
    # Standard Normal distribution (mean=0, stdev=1).
    random_matrix_integers = np.random.randint(1, 51, 20)
    print(random_matrix_integers)


    separador()

    print("Reshape list from 1 dimension to 2 dimensions, but size of list and new dimension items size must fit")
    array = np.random.randint(1,201,30)
    print(array)
    #reshape changes the array/matrix dimensions
    matrix = array.reshape(5,6)
    print(matrix)


    separador()

    array = np.random.randint(1,901,200)
    print(f"new list of 200 items : \n{array}")
    #max returns the maximum value of an array
    print(f"Max value is {array.max()}")
    #argmax returns the index of the maximum value in an array
    print(f"Max value index is {array.argmax()}")
    #min returns the minimun value of an array
    print(f"Min value is {array.min()}")
    #argmax returns the index of the minimun value in an array
    print(f"Min value index is {array.argmin()}")

    separador()

    print("Show elements using indexes")
    array = np.arange(0,100)
    print(f"{array}")
    print("-"*90)
    print(f"Single element at index  2:\n{array[2]}")
    print(f"All elements from index  5:\n{array[5:]}")
    print(f"All elements befor index 6:\n{array[:6]}")

    separador()

    print("Copy Array ")
    array2 = array.copy()
    print(f" array   :\n{array}")
    print(f" array2  :\n{array2}")
    print("Array2 Change ")
    array2[4]=99999
    print(f" array   :\n{array}")
    print(f" array2  :\n{array2}")

    separador()
    print("Matrix Operations ")
    print(f"Full Matrix:\n{matrix}")
    print(f"Select 0th row:\n{matrix[0]}")
    print(f"Select all rows before 2th row (0 and 1):\n{matrix[:2]}")
    print(f"Select item at row 1 and column 2:\n{matrix[1][2]}")
    print(f"Select all columns, but only at row index 1, it gets actually a list:\n{matrix[:,1]}")
    print(f"Select all columns, but all columns up to the column index 1, it is still a matrix:\n{matrix[:,:1]}")

    separador()
    print(f"Matrix scalar operations")
    print(f"Full Matrix:\n{matrix}")
    print(f"Add 10 to matrix:\n{matrix+10}")
    print(f"Add matrix to itself:\n{matrix+matrix}")
    print(f"multiply matrix with 10:\n{matrix*10}")
    print(f"multiply matrix with itself:\n{matrix*matrix}")

    separador()
    print(f"Select with condition that every ites is greater than n:")
    print(f"Full Matrix:\n{matrix}")
    condition = matrix > 10 
    print(f"Condition over Matrix (boolean result by item):\n{condition}")
    print(f"Selection of items that fulfills condition:\n{matrix[condition]}")
    print(f"New condition for odd numbers")
    odd_condition = (matrix % 2 !=0)
    print(f"Selection of items that fulfills condition of odd numbers:\n{matrix[odd_condition]}")

    separador()
    #ejercicio
    lista=np.arange(5,41)
    print("Mostrando lista dimension uno")
    print(lista)
    print(f"Tamaño lista es:{len(lista)}")
    print("Mostrando lista dimension modificada a 3 * 12")
    lista=lista.reshape(3,12)
    print(lista)
    print("Mostrando valor del indice 2,4")
    print(lista[2,4])
    #combinacion primitiva
    arrayPrimitiva=np.random.randint(1,50,6)
    print(f"La combinacion ganadora de la primitiva sera {arrayPrimitiva}")
        
proceso()
