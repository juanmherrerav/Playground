"""Strings o cadenas"""
def prueba_codigo():
    """Codigo Prueba"""
    string_sample = "hOla mUndo"
    print(f'strings es :{string_sample}')
    #convertir a minusculas
    print(f'Funcion strings.lower() es :{string_sample.lower()}')
    #convertir a mayusculas
    print(f'Funcion strings.upper() es :{string_sample.upper()}')
    #convertir a Capitalizada
    print(f'Funcion strings.capitalize() es :{string_sample.capitalize()}')
    #convertir a Titulo
    print(f'Funcion strings.title() es :{string_sample.title()}')
    #convertir a swapcase
    print(f'Funcion strings.swapcase() es :{string_sample.swapcase()}')
    #comprobacion
    print(f'String "{string_sample.lower()}" es minuscula :{string_sample.lower().islower()}')
    #comprobacion
    print(f'String "{string_sample}" es Numerica :{string_sample.isnumeric()}')
    #comprobacion
    number_string = "12345"
    print(f'String "{number_string}" es Numerica :{number_string.isnumeric()}')
    #comprobacion
    alfa_numerico_string = "12345abc"
    print(f'String "{alfa_numerico_string}" es alfanumerico :{alfa_numerico_string.isalnum()}')
    print(f'String "{alfa_numerico_string}" es alfabetico :{alfa_numerico_string.isalpha()}')
    print(f'String "{string_sample}" es alfabetico :{string_sample.isalpha()}')
    print(f'String "{string_sample.replace(" ", "")}" es alfabetico :{string_sample.replace(" ", "").isalpha()}')
    title_string = "Titulo"
    print(f'String "{title_string}" es Título :{title_string.istitle}')
