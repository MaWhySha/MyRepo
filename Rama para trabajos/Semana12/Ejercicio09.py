# Ejercicio 9: Año bisiesto

try:
    año = int(input("Ingresa un año: "))

    if año < 0:
        print("Error: El año no puede ser negativo")
    elif (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        print("Es un año bisiesto")
    else:
        print("No es un año bisiesto")

except ValueError:
    print("Error: Debes ingresar un año válido")

# MaWhySha