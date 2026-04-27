# Ejercicio 7: Promedio de notas

notas = []

while True:
    try:
        nota = float(input("Ingresa una nota (-1 para terminar): "))

        if nota == -1:
            break

        if nota < 0 or nota > 10:
            print("Nota inválida, se ignora")
        else:
            notas.append(nota)

    except ValueError:
        print("Error: Debes ingresar una nota válida")

suma = 0

for n in notas:
    suma += n

if len(notas) > 0:
    promedio = suma / len(notas)
    print("Promedio:", promedio)
else:
    print("No se ingresaron notas válidas")

# MaWhySha