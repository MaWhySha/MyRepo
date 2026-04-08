# Ejercicio 8
def transformar_texto(texto, opcion):
    """
    Recibe un texto y un número (1,2,3).
    Aplica la transformación correspondiente:
    1 = mayúsculas, 2 = minúsculas, 3 = primera letra en mayúscula.
    Devuelve el texto transformado.
    """
    if opcion == 1:
        return texto.upper()
    elif opcion == 2:
        return texto.lower()
    elif opcion == 3:
        return texto.capitalize()
    else:
        print("Opción inválida")
        return None


print("=== TRANSFORMADOR DE TEXTO ===")

# Entrada inicial
texto = input("Ingrese un texto: ").strip()

while True:
    print("\nOpciones:")
    print("1. Convertir a MAYÚSCULAS")
    print("2. Convertir a minúsculas")
    print("3. Primera letra en mayúscula")
    print("4. Cambiar el texto")
    print("5. Salir")

    try:
        opcion = int(input("Seleccione una opción: "))
    except ValueError:
        print("ERROR: Debe ingresar un número válido.")
        continue

    if opcion == 5:
        print("Saliendo del programa...")
        break
    elif opcion == 4:
        texto = input("Ingrese un nuevo texto: ").strip()
        continue

    resultado = transformar_texto(texto, opcion)
    if resultado is not None:
        print("Resultado:", resultado)

    # Pregunta si quiere seguir con el mismo texto
    while True:
        seguir = input("\n¿Desea seguir con este texto? (s/n): ").lower()
        if seguir == "s":
            break
        elif seguir == "n":
            texto = input("Ingrese un nuevo texto: ").strip()
            break
        else:
            print("Ingrese 's' para sí o 'n' para no.")

#MaWhySha