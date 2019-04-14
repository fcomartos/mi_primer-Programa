

texto_usuario = input("Escribe una frase: ")

vocales = ["a", "e", "i", "o", "u"]
vocales_texto_usuario = []

for letra in texto_usuario:
    if letra in vocales:
        vocales_texto_usuario.append(letra)


print(vocales_texto_usuario)