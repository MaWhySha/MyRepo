# Ejercicio 1: Números pares en rango

while True:
    try:
        n = int(input("Ingresa un número (0 para salir): "))

        if n == 0:
            print("Programa finalizado")
            break

        for i in range(1, n + 1):
            if i % 2 == 0:
                print(i)

    except ValueError:
        print("Error: Debes ingresar un número válido")

# MaWhySha