
numeros_del_usuario = []
numero_del_usuario = ""

for numero in range(0, 6):
    while not  numero_del_usuario.isdigit():
        numero_del_usuario = input("Escribe un numero: ")
    numeros_del_usuario.append(int(numero_del_usuario))
    numero_del_usuario = ""

suma = 0
for numero in numeros_del_usuario:
    suma = suma + numero

numero_de_datos = 0
for numero in numeros_del_usuario:
    numero_de_datos +=1

print("La media es: ",suma / numero_de_datos)