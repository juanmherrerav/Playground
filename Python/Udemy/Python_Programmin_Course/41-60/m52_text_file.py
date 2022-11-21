def save_text(filename, text):
    file = open (filename+'.txt', 'w')
    file.write(text)
    file.close
    print('Texto guardado')
    return True

def read_text(filename):
    filename = open (filename+'.txt', 'r')
    text = filename.read()
    filename.close
    return text

text = input('Pon aqui el texto a guardar : ')
filename = input(' Indicame el nombre del archivo :')
save_text(filename, text)
text = read_text(filename)
print("Este es el texto Guardado")
print(text)