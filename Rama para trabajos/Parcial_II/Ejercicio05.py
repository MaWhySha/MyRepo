# Ejercicio 5: Uso de swapcase() y ljust()

# 1. Cadena inicial
texto = "pYTHON"

# 2. Invertir mayúsculas y minúsculas 
texto_invertido = texto.swapcase()

# 3. Alinear a la izquierda en 15 caracteres con "*"
texto_final = texto_invertido.ljust(15, "*")

# Mostrar resultados 
print("Texto original:", texto)
print("Texto invertido:", texto_invertido)
print("Texto final:", texto_final)

#MaWhySha