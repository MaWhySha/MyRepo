# Ejercicio 4: Número par o impar

try:
    numero = int(input("Ingresa un número: "))

    if numero % 2 == 0:
        print("El número es par")
    else:
        print("El número es impar")

except ValueError:
    print("Error: Debes ingresar un número válido")

# MaWhySha