# Ejercicio 9: Juego de adivinar número

import random

numero_secreto = random.randint(1, 100)
intentos = []

while True:
    try:
        intento = int(input("Adivina el número (1-100): "))
        intentos.append(intento)

        if intento == numero_secreto:
            print("¡Correcto!")
            break
        elif intento < numero_secreto:
            print("El número es mayor")
        else:
            print("El número es menor")

    except ValueError:
        print("Error: Debes ingresar un número válido")

print("Intentos realizados:")

for i in intentos:
    print(i)

print("Total de intentos:", len(intentos))

# MaWhySha