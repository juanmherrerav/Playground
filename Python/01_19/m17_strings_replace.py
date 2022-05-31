""" Reemplazo de Strings """


def string_replace():
    """String Replace examples"""
    texto = "Esto es un texto para el ejemplo que vamos a realizar"
    print(f'El string empieza con: "Esto" {texto.startswith("Esto")}')
    print(
        f'El string termina con: "Realizar" {texto.endswith("Realizar".lower())}')
    # Alinear texto
    # Centrado
    texto_len = len(texto)
    print(f"El string '{texto}' mide {texto_len} caracteres")
    print(f"{texto.center(80, '*')}")
    print(f"{texto.center(texto_len+7 , '*')}")
    # Izquierda
    print("Texto alineado a la izquierda")
    print(f"{texto.ljust(80, '-')}")
    # Derecha
    print("Texto alineado a la derecha")
    print(f"{texto.rjust(80, '0')}")

    # eliminar espacios en blanco
    texto_whitespace = "     Esto es una cadena con espacios en blanco y algunos caracteres raros *-/6535-*-\\j      "
    print("eliminar espacios en blanco")
    print(f"Texto con espacios en blanco '{texto_whitespace}'")
    print(f"Texto sin espacios en blanco '{texto_whitespace.strip()}'")

    # Sustituir caracteres
    texto_sustituir = texto_whitespace.replace("-", "hola")
    print(f"Texto original   '{texto_whitespace}'")
    print(f"Texto sustituido '{texto_sustituir}'")

string_replace()
