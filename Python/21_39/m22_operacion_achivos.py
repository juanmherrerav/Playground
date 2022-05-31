""" Operaciones con archivo """

import os

def crea_archivo(name: str):
    escritura = open(name, "w", encoding="utf-8")
    escritura.write("Hola mundo \n esto es en la linea siguiente\n\t\t Y esto en otra linea con tabulaciones")
    escritura.close()

def process():
    folder = os.getcwd()
    # imprimir contenico directorio
    listado = os.listdir(folder)
    print(listado)
    print("*"*50)
    print(type(listado))
    # filtrar archivos
    #listado.sort()
    #for archivo in listado:
    #    if archivo.endswith(".py"):
    #        print(f"Archivo Python encontrado : {archivo}")
    print("Listand contenido de directorio filtrado")
    filtrado = [archivo for archivo in listado if archivo.endswith(".py")]
    print(type(filtrado))
    print(filtrado)
    print("*"*50)
    original_filename = "hola.txt"
    original_filename_renamed = "hola_renombrado.txt"
    print("Creando archivo:"+ original_filename)
    crea_archivo(original_filename)
    listado = os.listdir(folder)
    print("Listand contenido de directorio filtrado")
    filtrado_hola = [archivo for archivo in listado if archivo.endswith(".txt")]
    print(filtrado_hola)
    print("*"*50)
    print("renombrando archivo")
    os.rename(original_filename, original_filename_renamed)
    print("Listand contenido de directorio filtrado")
    listado = os.listdir(folder)
    filtrado_hola_renombrado = [archivo for archivo in listado if archivo.endswith(".txt")]
    print(filtrado_hola_renombrado)
    print("eliminado archivo")
    os.remove(original_filename_renamed)
    print("Listand contenido de directorio filtrado")
    listado = os.listdir(folder)
    filtrado_hola_renombrado = [archivo for archivo in listado if archivo.endswith(".txt")]
    print(filtrado_hola_renombrado)

    for archivo in os.listdir():
        nombre, extension = os.path.splitext(archivo)
        print(f"nombre : {nombre} y la extension {extension}")

    # cambio directorio
    #copiar contenido
    file_to_be_copied = "inicio.txt"
    destination = "copiado.txt"
    crea_archivo(file_to_be_copied)
    #copy_file_contents(file_to_be_copied,destination=destination)
    copy_file_contents_with_open(file_to_be_copied,destination=destination)

def copy_file_contents(file_to_be_copied, destination):
    """ Copy file contents 1"""
    original = open(file_to_be_copied, "r")
    copied = open(destination,"w")
    for line in original:
        copied.write(line)
    original.close()
    copied.close()

def copy_file_contents_with_open(file_to_be_copied, destination):
    """ Copy file contents 2"""
    try:
        with open(file_to_be_copied,"r") as origin_file:
            with open(destination,"w") as dest_file:
                for line in origin_file:
                    dest_file.write(line)
    except FileNotFoundError:
        print("File not found error")



process()
