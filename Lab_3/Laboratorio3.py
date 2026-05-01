# Sistema de parqueo - Laboratorio 3

capacidad = 10
ocupados = 0

autos = 0
motos = 0
camiones = 0

while True:
    print("\n===== SISTEMA DE PARQUEO =====")
    print("1. Ingresar vehículo")
    print("2. Retirar vehículo")
    print("3. Mostrar estado")
    print("4. Salir")
    
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        if ocupados < capacidad:
            print("\nTipo de vehículo:")
            print("1. Auto")
            print("2. Moto")
            print("3. Camión")
            
            tipo = input("Ingrese tipo: ")

            match tipo:
                case "1":
                    autos += 1
                    ocupados += 1
                    print("Auto ingresado correctamente")
                case "2":
                    motos += 1
                    ocupados += 1
                    print("Moto ingresada correctamente")
                case "3":
                    camiones += 1
                    ocupados += 1
                    print("Camión ingresado correctamente")
                case _:
                    print("Tipo inválido")
        else:
            print("Parqueo lleno")

    elif opcion == "2":
        if ocupados > 0:
            print("\nTipo de vehículo a retirar:")
            print("1. Auto")
            print("2. Moto")
            print("3. Camión")

            tipo = input("Ingrese tipo: ")

            match tipo:
                case "1":
                    if autos > 0:
                        autos -= 1
                        ocupados -= 1
                        print("Auto retirado")
                    else:
                        print("No hay autos")
                case "2":
                    if motos > 0:
                        motos -= 1
                        ocupados -= 1
                        print("Moto retirada")
                    else:
                        print("No hay motos")
                case "3":
                    if camiones > 0:
                        camiones -= 1
                        ocupados -= 1
                        print("Camión retirado")
                    else:
                        print("No hay camiones")
                case _:
                    print("Tipo inválido")
        else:
            print("El parqueo está vacío")

    elif opcion == "3":
        print("\n===== ESTADO DEL PARQUEO =====")

        for i in range(ocupados):
            print(f"Espacio ocupado #{i+1}")

        disponibles = capacidad - ocupados

        print(f"\nCapacidad total: {capacidad}")
        print(f"Ocupados: {ocupados}")
        print(f"Disponibles: {disponibles}")
        print(f"Autos: {autos}")
        print(f"Motos: {motos}")
        print(f"Camiones: {camiones}")

    elif opcion == "4":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción inválida, intente de nuevo")

# MaWhySha