# Tabla de multiplicar 

tabla = int(input("Cual tabla quieres calcular ? : "))
contador = 1
print(f"Tabla del {tabla}")
print("**"*40)
while ( contador < 11) :
    resultado = tabla * contador
    print(f"{tabla} X {contador} = {resultado}")
    if contador == 4:
        print("El contador es igual a 4")
        break
    contador = contador + 1
print("**"*40)
print("Fin de la tabla")