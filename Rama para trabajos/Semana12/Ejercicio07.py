# Ejercicio 7: Descuento en compra

try:
    monto = float(input("Ingresa el monto de la compra: "))

    if monto < 0:
        print("Error: El monto no puede ser negativo")
    elif monto > 100:
        descuento = monto * 0.20
        total = monto - descuento
        print("Descuento aplicado: 20%")
        print("Total a pagar:", total)
    elif monto >= 50:
        descuento = monto * 0.10
        total = monto - descuento
        print("Descuento aplicado: 10%")
        print("Total a pagar:", total)
    else:
        print("Sin descuento")
        print("Total a pagar:", monto)

except ValueError:
    print("Error: Debes ingresar un monto válido")

# MaWhySha