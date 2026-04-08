# Ejercicio 4
def transformar_lista(lista, opcion):
    """
    Recibe una lista de palabras y un número.
    Aplica la transformación correspondiente a cada palabra y las muestra.
    """
    for palabra in lista:
        if opcion == 1:
            print(palabra.upper(), end=" ")
        elif opcion == 2:
            print(palabra.lower(), end=" ")
        elif opcion == 3:
            print(palabra.capitalize(), end=" ")
        else:
            print("\nOpción no válida")
            return
    print()  # Salto de línea al final de la lista


print("=== TRANSFORMADOR DE LISTA DE PALABRAS ===")

# Entrada inicial
entrada = input("Ingrese palabras separadas por espacios: ").strip()
while entrada == "":
    entrada = input("ERROR: Debe ingresar al menos una palabra: ").strip()
lista_palabras = entrada.split()

while True:
    print("\nOpciones:")
    print("1. Convertir todas a MAYÚSCULAS")
    print("2. Convertir todas a minúsculas")
    print("3. Primera letra de cada palabra en mayúscula")
    print("4. Cambiar la lista de palabras")
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
        entrada = input("Ingrese nuevas palabras separadas por espacios: ").strip()
        while entrada == "":
            entrada = input("ERROR: Debe ingresar al menos una palabra: ").strip()
        lista_palabras = entrada.split()
        continue

    transformar_lista(lista_palabras, opcion)

    # Pregunta si quiere seguir con la misma lista
    while True:
        seguir = input("\n¿Desea seguir con esta lista? (s/n): ").lower()
        if seguir == "s":
            break
        elif seguir == "n":
            entrada = input("Ingrese nuevas palabras separadas por espacios: ").strip()
            while entrada == "":
                entrada = input("ERROR: Debe ingresar al menos una palabra: ").strip()
            lista_palabras = entrada.split()
            break
        else:
            print("Ingrese 's' para sí o 'n' para no.")

#MaWhySha