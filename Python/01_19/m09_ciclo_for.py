# Tabla de multiplicar 

tabla = int(input("Cual tabla quieres calcular ? : "))
print(f"Tabla del {tabla}")

print("**"*40)

for contador in range(1,11):
    resultado = tabla * contador
    print(f"{tabla} X {contador} = {resultado}")
    if contador == 4:
        print("El contador es igual a 4")
        break
    contador = contador + 1
print("**"*40)

print(f"Contador es {contador}")
print("Fin de la tabla")

nombres = ["Jose", "M Mar", "Lucy", "Eva"]
for nombre in nombres:
    print(f"Hola, {nombre}")
for numero in range(100):
    print(f"{numero}")