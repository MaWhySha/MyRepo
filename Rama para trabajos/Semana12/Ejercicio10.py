# Ejercicio 10: Validar usuario y contraseña

usuario_correcto = "admin"
contrasena_correcta = "1234"

usuario = input("Ingresa tu usuario: ")
contrasena = input("Ingresa tu contraseña: ")

if usuario == usuario_correcto and contrasena == contrasena_correcta:
    print("Acceso permitido")
else:
    print("Acceso denegado")

# MaWhySha