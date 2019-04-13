

mi_lista = []
imput_usuario = ""

imput_usuario = input("¿Que necesitas comprar? (escribe FIN para salir): ")

while imput_usuario != "FIN":
    mi_lista.append(imput_usuario)
    imput_usuario = input("¿Que necesitas comprar? (escribe FIN para salir): ")

for item in mi_lista:
    print("Tengo que comprar {}".format(item))

print("Esta es la lista de la compra")
