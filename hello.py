

nombre_principal = "KIKO"

nombre = input("Hola, ¿cómo te llamas? ").upper()

if nombre == nombre_principal:
    print("Hola Kiko, eres el jefe")
else:
    print("Buenos días {}, ¿En qué puedo ayudarte?".format(nombre))
