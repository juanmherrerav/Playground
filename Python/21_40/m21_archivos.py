""" Escribir a archivos """


def proceso():
    """ Proceso de creacion y lectura de archivos"""
    filename_test = "m21_archivo_salida.txt"
    escritura = open(filename_test, "w", encoding="utf-8")
    escritura.write(
        "Hola mundo \n esto es en la linea siguiente\n\t\t Y esto en otra linea con tabulaciones")
    escritura.close()

    # Lectura del archivo

    lectura = open(filename_test, "r", encoding="utf-8")
    print("Leyendo archivo linea por linea:")
    line = lectura.readline()
    while line:
        print(f'|{line}')
        line = lectura.readline()
    lectura.close()


proceso()
