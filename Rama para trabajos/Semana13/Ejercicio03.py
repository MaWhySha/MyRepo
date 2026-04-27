# Ejercicio 3: Tabla de multiplicar filtrada

while True:
    try:
        numero = int(input("Ingresa un número (-1 para salir): "))

        if numero == -1:
            print("Programa finalizado")
            break

        for i in range(1, 11):
            resultado = numero * i
            if resultado > 20:
                print(f"{numero} x {i} = {resultado}")

    except ValueError:
        print("Error: Debes ingresar un número válido")

# MaWhySha