


operacion = input("¿Que operacion quieres realizar: (suma, resta, multiplicacion, division) ")

operacion = 0


primer_numero = float(input("Primer numero: "))
segundo_numero = float(input("Segundo numero: "))

if operacion == "suma":
    print("El resultado es: ", primer_numero + segundo_numero)
elif operacion == "resta":
    print("El resultado es: ", primer_numero - segundo_numero)
elif operacion == "multiplicacion":
    print("El resultado es: ", primer_numero * segundo_numero)
elif operacion == "division":
    print("El resultado es: ", primer_numero / segundo_numero)