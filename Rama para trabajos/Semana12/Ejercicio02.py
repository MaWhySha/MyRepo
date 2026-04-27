# Ejercicio 2: Clasificar edad

try:
    edad = int(input("Ingresa tu edad: "))

    if edad < 0:
        print("Error: La edad no puede ser negativa")
    elif edad < 18:
        print("Eres menor de edad")
    elif edad < 60:
        print("Eres mayor de edad")
    else:
        print("Eres adulto mayor")

except ValueError:
    print("Error: Debes ingresar una edad válida")

# MaWhySha