inicio = int (input( "Indicame el numero inicial : "))
fin = int (input( "Indicame el numero final : "))
print("Te muestro los numeros impares del intervalo \n")
for i in range (fin, inicio-1,-1):
     if i%2==0:
         print(i)
