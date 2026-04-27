# Ejercicio 2: Contador de positivos y negativos

positivos = 0
negativos = 0

while True:
    try:
        numero = float(input("Ingresa un número (0 para terminar): "))

        if numero == 0:
            break

        if numero > 0:
            positivos += 1
        else:
            negativos += 1

    except ValueError:
        print("Error: Debes ingresar un número válido")

print("Resumen:")

for i in range(2):
    if i == 0:
        print("Cantidad de positivos:", positivos)
    else:
        print("Cantidad de negativos:", negativos)

# MaWhySha