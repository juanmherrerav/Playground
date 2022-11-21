user_list = input('Dame una lista de colores separados por comas : ')
user_list = user_list.replace(' ','')
user_list = set( user_list.split(',') )
colors_list = []
for color in user_list:
    colors_list.append(color)
colors_list.sort()
print(colors_list)
