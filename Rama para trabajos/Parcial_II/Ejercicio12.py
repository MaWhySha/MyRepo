# Ejercicio 12: Uso de prefijos/sufijos y transformación

# 1. Nombre de archivo
texto = "ING.CarlosFernando.txt"

# 2. Remover el sufijo ".txt"
texto_sin_sufijo = texto.removesuffix(".txt")

# 3. Remover el prefijo "ING. "
texto_sin_prefijo = texto_sin_sufijo.removeprefix("ING.")

# 4. Convertir a minúsculas
texto_final = texto_sin_prefijo.lower()

# Mostrar resultados
print("Texto original:", texto)
print("Texto final:", texto_final)

#MaWhySha