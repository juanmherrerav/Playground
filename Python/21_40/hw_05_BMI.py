







#Realiza un programa de Python que pida al usuario su estatura y peso, los almacene en variables y los muestre por pantalla. nota: la fórmula para el IMC es el peso en kilogramos dividido por la estatura en metros cuadrados

estatura = float(input("Indica tu Estatura en metros:"))
peso = float(input("Indica tu peso en kilogramos :"))

bmi = peso/(estatura**estatura)
print(f"con una estatura {estatura}[m] y con un peso de {peso}[kg] \n\
    tu Indice de masa corporal es :{bmi}")