# Ejercicio 5: mini calculadora

try:
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    operacion = input("Ingresa la operación (+, -, *, /): ")

    if operacion == "+":
        print("Resultado:", num1 + num2)
    elif operacion == "-":
        print("Resultado:", num1 - num2)
    elif operacion == "*":
        print("Resultado:", num1 * num2)
    elif operacion == "/":
        if num2 == 0:
            print("Error: No se puede dividir entre cero")
        else:
            print("Resultado:", num1 / num2)
    else:
        print("Error: Operación no válida")

except ValueError:
    print("Error: Debes ingresar números válidos")

# MaWhySha