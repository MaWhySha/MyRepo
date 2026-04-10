# Ejercicio 7: Uso de zfill() y endswith()

# 1. Texto numerico
texto = "42"

# 2. Rellenar con ceros a la izquierda hasta longitud 5
texto_relleno = texto.zfill(5)

# 3. Verificar si termina en "2"
termina_en_2 = texto_relleno.endswith("2")

# Mostrar resultados 
print("Texto original:", texto)
print("Texto con ceros:", texto_relleno)
print("¿Termina en [2]?:", termina_en_2)

#MaWhySha