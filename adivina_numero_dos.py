

numero_a_adivinar = int(input("Escribe el numero secreto entre 1 y 10 "))

numero_usuario = int(input("¿Cual es tu numero?: "))


while numero_usuario != numero_a_adivinar:
        print("Ese no es el numero, intentalo otra vez")
        numero_usuario = int(input("¿Cual es tu numero?: "))

        if numero_usuario == numero_a_adivinar:
         print("Has ganado")