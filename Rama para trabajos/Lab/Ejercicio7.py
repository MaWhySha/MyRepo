# Ejercicio 7
def transformar_secuencial_detallado(texto, lista_opciones):
    """
    Recibe un texto y una lista de números (1,2,3).
    Aplica cada transformación en orden y muestra cada resultado,
    indicando cuál opción fue aplicada.
    Devuelve el resultado final del texto.
    """
    resultado = texto
    for i, opcion in enumerate(lista_opciones, start=1):
        if opcion == 1:
            resultado = resultado.upper()
            print(f"Resultado opción {opcion}: {resultado}")
        elif opcion == 2:
            resultado = resultado.lower()
            print(f"Resultado opción {opcion}: {resultado}")
        elif opcion == 3:
            resultado = resultado.capitalize()
            print(f"Resultado opción {opcion}: {resultado}")
        else:
            print(f"Opción inválida en la lista: {opcion}")
            return None
    return resultado


print("=== TRANSFORMADOR DE TEXTO SECUENCIAL DETALLADO ===")

# Entrada inicial
texto = input("Ingrese un texto: ").strip()

while True:
    print("\nOpciones disponibles para transformación:")
    print("1 = mayúsculas, 2 = minúsculas, 3 = primera letra en mayúscula")
    print("4 = Cambiar el texto")
    print("5 = Salir")

    entrada = input("Ingrese una o varias opciones separadas por espacios (ej: 1 3): ").strip()

    if entrada == "":
        print("ERROR: Debe ingresar al menos una opción.")
        continue

    if entrada == "5":
        print("Saliendo del programa...")
        break
    elif entrada == "4":
        texto = input("Ingrese un nuevo texto: ").strip()
        continue

    try:
        lista_opciones = [int(x) for x in entrada.split()]
    except ValueError:
        print("ERROR: Solo se permiten números separados por espacios.")
        continue

    # Validar que todas las opciones sean 1,2 o 3
    if not all(op in [1, 2, 3] for op in lista_opciones):
        print("ERROR: Solo se permiten opciones 1, 2 o 3.")
        continue

    print("\n--- Resultados ---")
    resultado_final = transformar_secuencial_detallado(texto, lista_opciones)
    print(f"Resultado final del texto: {resultado_final}")

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