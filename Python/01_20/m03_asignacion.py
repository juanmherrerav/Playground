# Dar valor a variable
precio = 225
cantidad = 3


# Calcular total
total = precio * cantidad

# resultado

print("El precio total es de :"+str(total))
print("El precio total es de :{}".format(total))

# borrar variable
del precio 
#print("El precio es :{}".format(precio))

# Da : "NameError: name 'precio' is not defined"

# reasignar

precio = 25
cantidad = 21
# Calcular total
total = precio * cantidad

print("El precio total es de :{}".format(total))


# Nombre de constantes se escriben en mayúsculas
# Nombre de variables  se escriben en minúsculas
PASSWORD = "contraseña"

# Asignar multiples variables
a,b,c,d = 1,4,"Nombre",True
print(a)
print(b)
print(c)
print(d)

# asignar mismo valor
x = y = z = 68
print(x)
print(z)
