""" Manipulacion de archivos """
import os


def proceso():
    """ Proceso central de la demo """
    # Crear un directorio
    folder_name = "m_21_directorio_nuevo"
    folder_name_renamed = "m_21_directorio_renombrado"
    os.makedirs(folder_name)
    # listar el contenido del directorio
    print("-"*50)
    ls_file_list = os.listdir("./")
    ls_file_list.sort()
    print("\n".join(ls_file_list))
    print("-"*50)
    # mostrar el contenido del directorio actual
    print(os.getcwd())
    # mostrar tamaño de carpeta
    print(os.path.getsize(folder_name))
    # Comprobar si es archivo o directorio
    print(os.path.isfile(folder_name))
    print(os.path.isdir(folder_name))
    # cambiar de directorio
    os.chdir(folder_name)
    print(os.getcwd())
    print("-"*50)
    ls_file_list = os.listdir("./")
    ls_file_list.sort()
    print("\n".join(ls_file_list))
    print("-"*50)

    # volver al directorio anterior
    print("retrocediendo al directorio padre")
    os.chdir("..")
    print(os.getcwd())
    print("-"*50)
    ls_file_list = os.listdir("./")
    ls_file_list.sort()
    print("\n".join(ls_file_list))
    print("-"*50)
    #renombrar el directorio
    os.rename(folder_name,folder_name_renamed)
    
    # borrar archivo
    filename_test = "m21_archivo_salida.txt"
    os.remove(os.getcwd()+"/"+filename_test)
    # eliminar directorio

    print(os.getcwd())
    print(f"Eliminando directorio {folder_name_renamed}")
    os.rmdir(folder_name_renamed)


proceso()
