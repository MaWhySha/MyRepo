# Ejercicio 8: Tipo de triángulo

try:
    lado1 = float(input("Ingresa el primer lado: "))
    lado2 = float(input("Ingresa el segundo lado: "))
    lado3 = float(input("Ingresa el tercer lado: "))

    if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
        print("Error: Los lados deben ser mayores que 0")
    elif lado1 + lado2 <= lado3 or lado1 + lado3 <= lado2 or lado2 + lado3 <= lado1:
        print("Error: No forma un triángulo válido")
    elif lado1 == lado2 == lado3:
        print("Triángulo equilátero")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Triángulo isósceles")
    else:
        print("Triángulo escaleno")

except ValueError:
    print("Error: Debes ingresar valores numéricos válidos")

# MaWhySha