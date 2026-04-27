# Ejercicio 3: Clasificar nota

try:
    nota = float(input("Ingresa una nota (0 a 10): "))

    if nota < 0 or nota > 10:
        print("Error: La nota debe estar entre 0 y 10")
    elif nota >= 9:
        print("Excelente")
    elif nota >= 7:
        print("Bueno")
    elif nota == 6:
        print("Aprobado")
    else:
        print("Reprobado")

except ValueError:
    print("Error: Debes ingresar una nota válida")

# MaWhySha