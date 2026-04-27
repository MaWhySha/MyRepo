# Ejercicio 6: Día de la semana

try:
    numero = int(input("Ingresa un número del 1 al 7: "))

    if numero == 1:
        print("Lunes")
    elif numero == 2:
        print("Martes")
    elif numero == 3:
        print("Miércoles")
    elif numero == 4:
        print("Jueves")
    elif numero == 5:
        print("Viernes")
    elif numero == 6:
        print("Sábado")
    elif numero == 7:
        print("Domingo")
    else:
        print("Error: Número fuera de rango")

except ValueError:
    print("Error: Debes ingresar un número válido")

# MaWhySha