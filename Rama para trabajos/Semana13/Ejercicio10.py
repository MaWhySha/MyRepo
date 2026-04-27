# Ejercicio 10: Suma acumulativa con límite

suma = 0
numeros_validos = []

while True:
    try:
        numero = float(input("Ingresa un número: "))

        if numero < 0:
            print("Número negativo, ignorado")
            continue

        suma += numero
        numeros_validos.append(numero)

        if suma > 100:
            print("La suma ha superado 100")
            break

    except ValueError:
        print("Error: Debes ingresar un número válido")

print("Números válidos ingresados:")

for n in numeros_validos:
    print(n)

print("Suma total:", suma)

# MaWhySha