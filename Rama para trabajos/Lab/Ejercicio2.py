# Ejercicio 2
def transformar_y_mostrar(palabra, opcion):
    """Recibe una palabra y un número, aplica la transformación y muestra el resultado"""
    if opcion == 1:
        print("Resultado:", palabra.upper())
    elif opcion == 2:
        print("Resultado:", palabra.lower())
    elif opcion == 3:
        print("Resultado:", palabra.capitalize())
    else:
        print("Opción no válida")


print("=== TRANSFORMADOR DE PALABRAS ===")

# Validación para que solo sea una palabra
palabra = input("Ingrese una palabra: ").strip()
while " " in palabra or palabra == "":
    print("ERROR: Debe ingresar solo una palabra sin espacios")
    palabra = input("Ingrese una palabra: ").strip()

while True:
    print("\nOpciones:")
    print("1. Convertir a MAYÚSCULAS")
    print("2. Convertir a minúsculas")
    print("3. Primera letra en mayúscula")
    print("4. Cambiar la palabra")
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
        palabra = input("Ingrese una nueva palabra: ").strip()
        while " " in palabra or palabra == "":
            print("ERROR: Debe ingresar solo una palabra sin espacios")
            palabra = input("Ingrese una palabra: ").strip()
        continue

    transformar_y_mostrar(palabra, opcion)

    # Pregunta si quiere seguir con la misma palabra
    while True:
        seguir = input("\n¿Desea seguir con esta palabra? (s/n): ").lower()
        if seguir == "s":
            break
        elif seguir == "n":
            palabra = input("Ingrese una nueva palabra: ").strip()
            while " " in palabra or palabra == "":
                print("ERROR: Debe ingresar solo una palabra sin espacios")
                palabra = input("Ingrese una palabra: ").strip()
            break
        else:
            print("Ingrese 's' para sí o 'n' para no.")
#MaWhySha