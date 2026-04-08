# Ejercicio 6
def transformar_y_contar(texto, opcion):
    """
    Recibe un texto y un número.
    Aplica la transformación correspondiente:
    1 = mayúsculas, 2 = minúsculas, 3 = primera letra en mayúscula.
    Devuelve la cantidad de caracteres del texto transformado.
    """
    if opcion == 1:
        resultado = texto.upper()
    elif opcion == 2:
        resultado = texto.lower()
    elif opcion == 3:
        resultado = texto.capitalize()
    else:
        print("Opción inválida")
        return None

    print("Resultado:", resultado)
    return len(resultado)


print("=== TRANSFORMADOR DE TEXTO CON LONGITUD ===")

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

    cantidad = transformar_y_contar(texto, opcion)
    if cantidad is not None:
        print("Cantidad de caracteres del resultado:", cantidad)

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