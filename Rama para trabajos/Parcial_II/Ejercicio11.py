# Ejercicio 11: Uso de center() y funciones combinadas

# 1. Cadena inicial
texto = "  el nido matinal  "

# 2. Limpiar espacios y convertir a formato título
texto_limpio = texto.strip()
texto_titulo = texto_limpio.title()

# 3. Centrar en 30 caracteres con "-"
texto_final = texto_titulo.center(30, "-")

# Mostrar resultados
print("Texto original:", texto)
print("Texto procesado:", texto_titulo)
print("Texto centrado:", texto_final)

#MaWhySha