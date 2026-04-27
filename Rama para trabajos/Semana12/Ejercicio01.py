# Ejercicio 1: Clasificar un número

try:
    numero = float(input("Ingresa un número: "))

    if numero > 0:
        print("El número es positivo")
    elif numero < 0:
        print("El número es negativo")
    else:
        print("El número es cero")

except ValueError:
    print("Error: Debe ingresar un número válido")

# MaWhySha