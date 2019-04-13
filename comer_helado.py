
apetece_helado_input = input("¿Te apetece un helado? (Si / No): ").upper()

if apetece_helado_input == "SI":
    apetece_helado = True
elif apetece_helado_input == "NO":
    apetece_helado = False
else:
    print("Entonces es que no")
    apetece_helado = False

tiene_dinero_input = input("¿Tienes dinero? (Si / No): ").upper()
esta_el_senor_helados_input = input("¿Esta el heladero? (Si / No): ").upper()
esta_tu_tia_input = input("¿Esta tu tia? (Si / No): ").upper()


apetece_helado = apetece_helado_input == "SI"
puede_permitirselo = tiene_dinero_input == "SI" or esta_tu_tia_input == "SI"
esta_el_senor_helados = esta_el_senor_helados_input == "SI"

if  apetece_helado and puede_permitirselo and esta_el_senor_helados:
    print("Pues comete un helado")
else:
    print("Pues nada")