""" Emular sentencia switch en Python, usando diccionarios """

def get_monnth(num: int) -> str:
    month ={
        1: 'Enero',  
        2: 'Febrero',
        3: 'Marzo',
        4: 'Abril',
        5:  'Mayo',
        6:  'Junio',
        7:  'Julio',
        8:  'Agosto',
        9:  'Septiembre',
        10: 'Octubre',
        11: 'Noviembre',
        12: 'Diciembre'
    }
    return month.get(num, "Mes no valido")

def process():
    print(get_monnth(3))
    mes = int(input("Introduce un mes: "))
    print(get_monnth(mes))



process()
