""" Numpy exercises """
from os import sep
import sys
import numpy as np
from numpy.core.numeric import identity


def proceso():
    """
    Test code for Numpy
    """
    print(sys.version)
    print("hola")

    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    array1 = np.array(list1)
    print(list1)
    print(type(list1))
    print(array1)
    print(type(array1))

    print("-")
    print("-" * 50)
    print("-")

    list2 = [[1, 2, 4], [2, 5, 3], [3, 4, 5]]
    array2 = np.array(list2)
    print(array2)

    print("-")
    print("-" * 50)
    print("-")
    # Generacion automatica de arrays
    arr = np.arange(2,15,2)
    print(arr)

    print("-")
    print("-" * 50)
    print("matrix with zeroes")
    zero_matrix = np.zeros((4, 5))
    print(zero_matrix)

    print("-")
    print("-" * 50)
    print("matrix with ones")
    ones_matrix = np.ones((4, 5))
    print(ones_matrix)

    # Creacion de matrices con valores seriados linealmente
    print("-")
    print("-" * 50)
    print("matrix with linear values")
    matrix = np.linspace(2,6,40)
    print(matrix)

    print("-")
    print("-" * 50)
    print("matrix identity")
    identity_matrix = np.eye(7)
    print(identity_matrix)

    print("-")
    print("-" * 50)
    print("Matrix with random values using Uniform distribution between [0,1]")
    # uniform distribution [0,1]
    random_matrix = np.random.rand(4, 5)
    print(random_matrix)

    print("-")
    print("-" * 50)
    print("Matrix with random values using Standard Normal distribution (mean=0, stdev=1).")
    print("filled with random floats sampled from a univariate \"normal\" (Gaussian) distribution of mean 0 and variance 1")
    # Standard Normal distribution (mean=0, stdev=1).
    random_matrix_standard_normal = np.random.randn(30)
    print(random_matrix_standard_normal)

    print("-")
    print("-" * 50)
    print("Return random integers from the \"discrete uniform\" distribution of the specified dtype in the \"half-open\" ")
    print("interval [low, high). If high is None (the default), then results are from [0, low)")
    # Standard Normal distribution (mean=0, stdev=1).
    random_matrix_integers = np.random.randint(1,51,20)
    print(random_matrix_integers)

    print("-" * 50)
    array = np.random.randint(1,201,30)
    #reshape changes the array/matrix dimensions
    matrix = array.reshape(5,6)
    print(matrix)


    print("-" * 50)
    array = np.random.randint(1,901,200)
    #max returns the maximum value of an array
    print(f"Max value is {array.max()}")
    #argmax returns the index of the maximum value in an array
    print(f"Max value index is {array.argmax()}")

    print("-" * 50)
    #min returns the minimun value of an array
    print(f"Max value is {array.min()}")
    #argmax returns the index of the minimun value in an array
    print(f"Max value index is {array.argmin()}")

    print("-" * 50)
    print("Show elements")
    array = np.arange(0,100)
    print(f"{array}")
    print(f"{array[2]}")
    print(f"{array[5:]}")
    print(f"{array[:6]}")

    print("-" * 50)
    print("Copy Array ")
    array2 = array.copy()
    print(f" array  :{array}")
    print(f" array2  :{array2}")
    print("Array2 Change ")
    array2[4]=99999
    print(f" array  :{array}")
    print(f" array2  :{array2}")

    print("-" * 50)
    print("Matrix Operations ")
    print(f"{matrix}")
    print(f"{matrix[0]}")
    print(f"{matrix[:2]}")
    print(f"{matrix[1][2]}")

    print("33:48")


proceso()
