# Ejercicio 2: Uso de title() y replace()

# 1. Declarar la cadena con el nombre
texto = "carlos fernando guardado garcía"

# 2. Convertir para que cada palabra inicie con mayúscula
texto_titulo = texto.title()

# 3. Reemplazar "Carlos Fernando" por "Guardado García"
texto_final = texto_titulo.replace("Carlos Fernando Guardado García", "Fernando García")

# Mostrar resultados 
print("Texto original:", texto)
print("Texto con formato title():", texto_titulo)
print("Texto final:", texto_final)

#MaWhySha