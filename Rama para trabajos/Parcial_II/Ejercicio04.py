# Ejercicio 4: Uso de lower(), removesuffix() y find()

# 1. Tomar la palabra
texto = "CANTANDO"

# 2. Convertir a minúsculas 
texto_minuscula = texto.lower()

# 3. Eliminar el sufijo "ando"
texto_sin_sufijo = texto_minuscula.removesuffix("ando")

# 4. Encontrar la posición de la letra "t"
posicion_t = texto_sin_sufijo.find("t") + 1

# Mostrar resultados 
print("Texto original:", texto)
print("Texto minúsculas:", texto_minuscula)
print("Texto sin sufijo:", texto_sin_sufijo)
print("Posición de la letra [t]:", posicion_t)

#MaWhySha