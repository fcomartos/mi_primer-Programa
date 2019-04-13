
frase_del_usuario = input("Escribe una frase: ")

espacio = " "
punto = "."
coma = ","

n_espacios = 0
n_puntos = 0
n_comas = 0

for letra in frase_del_usuario:
    if letra == espacio:
        n_espacios += 1
    if letra == punto:
        n_puntos += 1
    if letra == coma:
        n_comas +=1

print("Los espacios son {}".format(n_espacios))
print("Los puntos son {}".format(n_puntos))
print("Las comas son {}".format(n_comas))