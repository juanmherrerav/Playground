nombre  = input("dime tu  nombre: ")
print("Hola , {}".format(nombre))
print("Hola , " + nombre, end=" ")
print("Hola , " , nombre + "\n\n\n")
print(f"Hola , {nombre}"+ "\t\t\testo esta separado por tabulaciones")


# Ojo que input captura un str
numero = int(input("Dime un número: "))
nunumero2 = int(input("Dime otro número: "))

resultado = numero + nunumero2
print(f"La suma  de {numero} mas {nunumero2} es igual a {resultado}")