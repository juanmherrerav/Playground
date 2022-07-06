def menu():
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("0. Salir")
    return int(input("?__"))

def solcitudDatos():
    num1 = int(input("Dime el 1er número: "))
    num2 = int(input("Dime el 2do número: "))
    return num1,num2

def operacion(operador, num1, num2):
    if operador == "suma":
        resultado = num1 + num2
    if operador == "resta":
        resultado = num1 - num2
    if operador == "multiplica":
        resultado = num1 * num2
    if operador == "divide":
        resultado = num1 / num2
    return resultado

while True:
    opcion = menu()
    if opcion == 1:
        num1, num2 = solcitudDatos()
        print(f"El resultado de {num1} + {num2} es = ",end="")
        print(operacion("suma",num1,num2))
    if opcion == 2:
        num1, num2 = solcitudDatos()
        print(f"El resultado de {num1} - {num2} es = ",end="")
        print(operacion("resta",num1,num2))
    if opcion == 3:
        num1, num2 = solcitudDatos()
        print(f"El resultado de {num1} * {num2} es = ",end="")
        print(operacion("multiplica",num1,num2))
    if opcion == 4:
        num1, num2 = solcitudDatos()
        print(f"El resultado de {num1} / {num2} es = ",end="")
        print(operacion("divide",num1,num2))
    elif opcion == 0:
        break
