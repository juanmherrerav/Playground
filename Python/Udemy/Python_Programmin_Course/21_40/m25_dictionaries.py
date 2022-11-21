""" Dictionaries """
# Diccionarios son estructuras de datos tipo Clave-Valor
# se definen con llaves {}
# Se referencian elementos con [] para una dimensacion
# Se referencian elementos con [][] para dos dimensaciones

def proceso():
    diccionario = {'nombre':'Jose', 'apellidos':'Ojeda', 'tutoriales': ['Python', 'Javascript', 'Php']            }
    print(diccionario)
    print(type(diccionario))
    print(diccionario['nombre'])
    print(diccionario['tutoriales'])
    print(diccionario['tutoriales'][1])
    for clave in diccionario:
        print(clave, ":", diccionario[clave])
    #metodos de los diccionarios
    persona = dict(nombre= "Jose", apellidos= "Ojeda", edad= "48")
    print(persona)
    print(type(persona))

    # Diccionarios con 2 elementos iterables, usando metodo zip
    dictionaries_02 = dict(zip('aeiou', [1,2,3,4,5]))
    print(dictionaries_02)
    print(type(dictionaries_02))

    # Obtener lista de tuplas <clave, valor>
    print(dictionaries_02.items())

    # Obtener lista de claves
    print(dictionaries_02.keys())

    # Obtener lista de valores
    print(dictionaries_02.values())

    # Limpiar diccionario
    #dictionaries_02.clear()
    #print(dictionaries_02)

    # copiar diccionario
    copia_diccionario = dictionaries_02.copy()
    print(copia_diccionario)
    dictionaries_03 = dict.fromkeys(['a', 'e', 'i','o','u'], 34)
    print(dictionaries_03)
    print(diccionario.get('nombre'))
    key_to_search = 'amigo'
    print(f"La clave {key_to_search} existe en el diccionario? {key_to_search in diccionario}")
    print(f"Cual es el valor asociado a la clave '{key_to_search}' en el diccionario? '{diccionario.get(key_to_search)}'")

    # Eliminar una clave del diccionario
    borrado = diccionario.pop('nombre')
    print(borrado)
    print(diccionario)

    # Eliminar una clave que no existe en el diccionario
    borrado = diccionario.pop('direccion', 'No existe')
    print(borrado)
    print(diccionario)

    #Actualizar diccionario con valores de otros diccionarios, usando update
    diccionario_02 = {'provincia':'Sevilla', 'nombre':'Lucia'}
    print(diccionario)
    diccionario.update(diccionario_02)
    print(diccionario)


proceso()
