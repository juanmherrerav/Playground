""" Funciones """
# funcion ejemplo para determinar paridad
def esPar(numero: int) -> bool:
    """Validar paridad"""
    if numero % 2 == 0:
        #print(f"El numero {numero} es par")
        return True
    else:
        #print(f"El numero {numero} es impar")
        return False

def suma(num1:int , num2:int)-> int:
    resultado = num1 + num2
    return resultado



#numero = int(input("Dime un numero y te dire si es par o no : "))
#resultado = esPar(numero)
#if resultado:
#    print(f"El numero {numero} es par")
#else:
#    print(f"El numero {numero} es impar")

num1 = int(input("Dime un el primer numero  : "))
num2 = int(input("Dime un el segundo numero : "))
resultado = suma(num1, num2)

print(f"La suma es igual a {resultado}")