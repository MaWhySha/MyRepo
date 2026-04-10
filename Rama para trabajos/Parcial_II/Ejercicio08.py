# Ejercicio 8: Uso de count() y splitlines()

# 1. Bloque de texto de 3 lineas, tomado del poema de la guia :)
texto = """Es porque un pajarito de la montaña ha 
hecho en el hueco de un árbol, su nido matinal, que 
el árbol amanece con música en el pecho"""

# 2. Normalizar texto [Para poder tomar en cuenta todas las "a"]
texto_normal = texto.lower().replace("á", "a")

# 3. Contar cuantas veces aparece la letra [a] en el texto
cantidad_a = texto_normal.count("a")

# 4. Dividir el texto en lineas
lineas = texto.splitlines()

# Mostrar resultados 
print("Cantidad de [a]:", cantidad_a)
print("Líneas del poema:")
for linea in lineas:
    print(linea)

#MaWhySha