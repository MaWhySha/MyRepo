# Ejercicio 5: Validación de contraseña

contrasena_correcta = "1234"
intentos_fallidos = 0

while True:
    contrasena = input("Ingresa la contraseña: ")

    if contrasena == contrasena_correcta:
        print("Acceso permitido")
        break
    else:
        print("Contraseña incorrecta")
        intentos_fallidos += 1

ultimo = 0
for i in range(intentos_fallidos):
    ultimo = i + 1  
print("Cantidad de intentos fallidos:", ultimo)

# MaWhySha