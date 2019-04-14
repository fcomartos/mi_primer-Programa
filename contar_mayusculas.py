frase_del_usuario = input("Escribe una frase: ")

n_mayusculas = 0

for letra in frase_del_usuario:
    if letra.isupper():
        n_mayusculas += 1

print("Las mayusculas son {}".format(n_mayusculas))

mayusculas = len([letra for letra in frase_del_usuario if letra.isupper()])
print("Mayusculas: {}".format(mayusculas))
