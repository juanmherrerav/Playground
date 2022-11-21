







# Crea un script de Python que muestre los numeros impares tomando como inicio y 
# fin los numeros que le indique el usuario.

inicio = int(input("Indica numero de inicio:"))
fin = int(input("Indica numero de fin:"))

def es_impar(num):
    return num % 2 == 1

for num in range(inicio, fin+1):
    if es_impar(num):
        print(f"{num}, ", end="")
else:
    print(" ")