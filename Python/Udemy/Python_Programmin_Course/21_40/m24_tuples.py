""" Tuples """


def tuples_process():
    # Tupples are inmutable list
    # lists are defined with [] - brackets
    # tuples are defined with () - parenthesis

    colors = ("green", "yellow", "red", "blue")
    print(type(colors))
    print(f"The whole tuple is {colors}")
    print(f" a subset from start or index zero  to index 1 is {colors[:2]}")

    tupla = ()
    print(tupla)
    print(type(tupla))

    try:
        colors[2] = "rose"
    except:
        print("Can not assign values to tuples after creation due to immutability, colors[2] = \"rose\" failed")
 

tuples_process()
