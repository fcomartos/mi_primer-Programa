

numeros_usuario = []
numero_del_usuario = ""

while len(numeros_usuario) < 5:
    while not numero_del_usuario.isdigit():

        numero_del_usuario = input("Dime un numero: ")
    numeros_usuario.append(int(numero_del_usuario))
    numero_del_usuario = ""

print(numeros_usuario)

numero_pequeno = numeros_usuario[0]

for numero in numeros_usuario:
    if numero < numero_pequeno:
        numero_pequeno = numero

print("El numero más pequeño es {} ".format(numero_pequeno))
