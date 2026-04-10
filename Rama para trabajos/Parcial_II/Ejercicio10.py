# Ejercicio 10: Uso de isalnum() y separación

# 1. Cadena inicial
texto = "Python2026"

# 2. Verificar si es alfanumérico
es_alfanumerico = texto.isalnum()

# 3. Si lo es, convertimos a minúsculas y luego separamos 
if es_alfanumerico:
    texto_minuscula = texto.lower()
    texto_separado = texto_minuscula.replace("2026", "")

    print("Texto en minúsculas:", texto_minuscula)
    print("Texto separado:", texto_separado)
else:
    print("El texto no es alfanumérico")

#MaWhySha