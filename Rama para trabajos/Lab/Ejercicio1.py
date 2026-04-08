# Ejercicio 1
def transformar_texto(texto, opcion): #Definimos logica para las opciones
    """Crear una función que reciba un texto y un número"""
    if opcion == 1:
        return texto.upper()
    elif opcion == 2:
        return texto.lower()
    elif opcion == 3:
        return texto.capitalize()
    else:
        return None


print("=== TRANSFORMADOR DE TEXTO ===")
texto = input("Ingrese un texto: ")

while True: #Mostramos las opcines disponibles
    print("\nSeleccione una opción:")
    print("1. Convertir a MAYÚSCULAS")
    print("2. Convertir a minúsculas")
    print("3. Primera letra en mayúscula")
    print("4. Escribir un nuevo texto")
    print("5. Salir")

    try:
        opcion = int(input("Opción: "))
    except ValueError:
        print("ERROR: Debe ingresar un número válido.")
        continue

    if opcion == 5:
        print("Saliendo del programa...")
        break
    elif opcion == 4:
        texto = input("Ingrese un nuevo texto: ")
        continue

    resultado = transformar_texto(texto, opcion)

    if resultado is not None:
        print("Resultado:", resultado)
    else:
        print("Opción no válida")

    # Pregunta si quiere seguir con el mismo texto o cambiarlo
    while True:
        seguir = input("\n¿Desea seguir con este texto? (s/n): ").lower()
        if seguir == "s":
            break  # vuelve al menú con el mismo texto
        elif seguir == "n":
            texto = input("Ingrese un nuevo texto: ")
            break  # vuelve al menú con nuevo texto
        else:
            print("Ingrese 's' para sí o 'n' para no.")

#MaWhySha