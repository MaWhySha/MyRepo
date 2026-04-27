# Ejercicio 4: Suma de números impares

suma_impares = 0
impares = []

while True:
    try:
        numero = int(input("Ingresa un número (0 para terminar): "))

        if numero == 0:
            break

        if numero % 2 != 0:
            suma_impares += numero
            impares.append(numero)

    except ValueError:
        print("Error: Debes ingresar un número válido")

print("Suma de impares:", suma_impares)

print("Números impares ingresados:")
for num in impares:
    print(num)

# MaWhySha