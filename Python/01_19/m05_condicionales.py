# Suma              : +
# Resta             : -
# Multiplicacion    : *
# Division          : /
# Division Entera   : //
# Exponenciación    : **
# Resto División    : %
# Negativo          : - 
# Menor que         : <
# Mayor que         : >
# igual que         : ==
# distinto que      : !=
# Menor o igual que : <=
# y lógico          : and
# o lógico          : or
# negación lógica   : not

print(f"not 3>5     resulta en {not 3>5}")
print(f"3>5 and 2<6 resulta en {3>5 and 2<6}")
print(f"3>1 or 4<2  resulta en {3>1 or 4<2}")

print("-"*40)

numero1 = int(input("Dime el primer numero : "))
numero2 = int(input("Dime el segundo numero y te digo cual es mayor : "))

if (numero1>numero2):
    print(f"El número {numero1} es mayor que {numero2}")
elif (numero1 < numero2):
    print(f"El número {numero1} es menor que {numero2}")
else:
    print("Los dos numeros son iguales")
print("hemos terminado de comparar")

# Edades paea tarifa
edad1 = int(input("Dime tu edad y te dare tu tarifa : "))
if (edad1<5):
    precio = 0
elif (edad1<15):
    precio = 5
elif (edad1<65):
    precio = 20    
else:
    precio = 15
print("Tu tarifa para entrer es :"+str(precio))
