# Ejercicio 6: Uso de casefold() e isalpha()

# 1. Texto inicial, mi nombre
texto = "Carlos Fernando Guardado García"

# 2. Aplicar normalización fuerte 
texto_normalizado = texto.casefold()

# 3. Quitar los espacios para devuelva true
texto_sin_espacios = texto_normalizado.replace(" ", "")

# 4. Verificar si solo contiene letras
contiene_solo_letras = texto_sin_espacios.isalpha()

# Mostrar resultados 
print("Texto original:", texto)
print("Texto normalizado:", texto_normalizado)
print("¿Solo contiene letras?:", contiene_solo_letras)

#MaWhySha