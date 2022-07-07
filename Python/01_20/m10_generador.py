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

lista_colores=["rojo","amarillo","verde","azul"]
ni_color="rosa"
for color in lista_colores:
    print(color)
    if color ==  ni_color:
       print("color encontrado")
       break
else:
    print(f"He terminado de recorrer la lista y no se encontro '{ni_color}'")

rango_largo=range(1,10000)
print(rango_largo)
for numero in rango_largo:
    print(numero)
    if numero == 5:
        print("Numero Encontrado")
        break
else:
    print("No se encontro el numero")