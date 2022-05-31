#Funcion que crea objeto generador
def impares():
    for numero in range (1,50,2):
        yield numero

generador = impares()
print(f"{generador} es una variable de tipo {type(generador)}")
print("**"*40)
# iterar generador en ciclo for
for numero in generador:
    print(numero)
print("**"*40)
# Generador en una linea debe ser () en vez de []
mylist = (x*x for x in range(3))
for i in mylist:
    print(i)
print("**"*40)

# Generador iterando item a item
generador = impares()
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))