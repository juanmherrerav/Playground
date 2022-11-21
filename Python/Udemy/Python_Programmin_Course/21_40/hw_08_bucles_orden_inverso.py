







# Crea un script que pregunte al usuario numero inicial y final 
# y muestre los numeros pares que se incluyen dentro del intervalo mostrandolos en orden inverso.

inicio = int(input("Indica numero de inicio:"))
fin = int(input("Indica numero de fin:"))

def es_par(num):
    return num % 2 == 0

print(f"Numeros pares mostrados en orden inverso:")

for num in range(fin, inicio-1, -1):
    if es_par(num):
        print(f"{num}, ", end="")
else:
    print(" ")