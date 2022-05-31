""" lists manipulation"""


def process_list():
    list_example = [1, 2, 3.0, "Jose", [7, 8], 12, 15, 15, 15, 12]
    print(type(list_example))
    print(list_example)
    # Ubicar item individual de una dimension
    print(list_example[2])
    # Ubicar item individual de dos dimension
    print(list_example[3][1])
    # Ubicar rango de items
    print(list_example[1:4])
    # Ubicar rango con salto
    print(list_example[2:5:2])

    # ciclo
    for element in list_example:
        print(element)

    # Adding items
    list_example.append(10)
    list_example.append("Lucia")
    # añadir todo como un elemento
    list_example.append([2, 3, 6, 8, 9])
    print(list_example)
    # añadir todo como elementos individuales
    list_example.extend([4, 5, 2, 4])
    print(list_example)
    list_example.remove("Jose")
    print(list_example)
    print(list_example.index("Lucia"))
    print(list_example.count(2))
    print(list_example.count(15))

    list_example.reverse()
    print(list_example)

    shopping_list = ['bread', 'potatoes', 'kiwis']
    print(type(shopping_list))
    print(shopping_list)

    # Crear lista desde variables
    bread_ammount = 5
    bread_price = 0.4000
    total = bread_ammount * bread_price
    purchase = [bread_ammount, bread_price, total]
    print(purchase)
    purchase2 = [3, 0.60, 3*0.60]
    purchase3 = [4, 0.50, 4*0.50]
    orders = [purchase, purchase2, purchase3]
    print(orders)
    # empty list
    empty_list = []
    print(empty_list)
    print(type(empty_list))

    shopping_list.append("pears")
    shopping_list.insert(2, "bananas")
    print(shopping_list)
    print(f"longitud de lista {len(shopping_list)}")

    # how to add elements using a cicle
    square_list = []
    for numero in range(1, 11):
        square_list.append(numero * numero)
    print(f"Squares are :{square_list}")
    print(f"Min Squares is :{min(square_list)}")
    print(f"Max Squares is :{max(square_list)}")
    print(f"Sum of the Squares is :{sum(square_list)}")


    print("check if and item is in the list")
    print(f"Is 1 in squareare_list {1 in square_list}")
    print(f"Is 3 in squareare_list {3 in square_list}")


process_list()
