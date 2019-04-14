
numeros_del_usuario = []
numero_del_usuario = ""

for numero in range(0, 6):
    while not  numero_del_usuario.isdigit():
        numero_del_usuario = input("Escribe un numero: ")
    numeros_del_usuario.append(int(numero_del_usuario))
    numero_del_usuario = ""

print(numeros_del_usuario)

largo_lista = 0

for item in numeros_del_usuario:
    largo_lista += 1

print("Largo de la lista es: {}".format(largo_lista))