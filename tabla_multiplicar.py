

numero_tabla = int(input("Escribe el número de la tabla que quieres: "))

for multiplo in range(-10, 0):

        print("{} x {} = {}".format(numero_tabla, abs(multiplo), abs(numero_tabla * multiplo)))