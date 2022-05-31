""" Funcion anonima"""
from functools import reduce
#Funcion Map
lista = [1,2,3,4,5,6,7,8,9,10]
print(list(map(lambda x: x**2, lista)))
#funcion filter
print(list(filter(lambda x: x%2==0, lista)))
#funcion reduce
print(reduce(lambda x,resultado: x+resultado, lista))
