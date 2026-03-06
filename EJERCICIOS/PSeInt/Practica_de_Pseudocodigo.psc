Algoritmo Ejemplo
	Definir Cajero, CuentaDeAhorro, CantidadSalente, Saldo, Preguntar Como Entero
	CuentaDeAhorro = 1000
	NumeroDeCuenta = 12345
	
	Escribir " Bienvenido "
	Escribir " Actividad que desea realizar "
	Escribir " 1 para consultar "
	Escribir " 2 para extraer dinero de la cuenta de ahorro "
	
	Escribir " Escriba el número de la acción a realizar "
	Leer Preguntar // Yo no quiero ser un 1 XD mejor busco otra chamba
	
	si Preguntar == 1
		Escribir " Escriba el número de cuenta a operar "
		Leer Preguntar //Es el valor del número de cuenta
		
		si Preguntar == NumeroDeCuenta
		Escribir " Su saldo es " , CuentaDeAhorro
		FinSi
	FinSi
	
	si Preguntar == 2
		Escribir " Escriba el número de cuenta a operar "
		Leer Preguntar //Es el valor del número de cuenta
		
		si Preguntar == NumeroDeCuenta
			Escribir " Escriba el monto a extraer "
			Leer  Preguntar // ES la cantidad a extraer
			
			// < =
			si Preguntar <= CuentaDeAhorro
				Saldo = CuentaDeAhorro - Preguntar
				Escribir " Procesando "
				Escribir " Su saldo actual es de " , Saldo
			FinSi
		FinSi
	FinSi
	
	
	//No pueden comenzar con número
	// OR (Te da a escoger entre dos opciones)
	// And (Te permite activarse con ambas opciones)
	// Not (No te permite activarse con niguna opción)
	// == (Si es igual)
	// <> (Si es diferente) ! = (El signo se saca utilizando ambos signos)
	
FinAlgoritmo
