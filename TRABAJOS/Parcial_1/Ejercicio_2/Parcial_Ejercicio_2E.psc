Algoritmo Parcial_Ejercicio_2E // Suma de números positivos 
	
	Definir numero, suma Como Entero // Definimos nuestra variable como entero para almacenar datos númericos 
	suma <- 0 // Establecemos el valor inicial de la suma en 0 para comenzar 
	
	Escribir " Bienvenido/Bienvenida al programa de suma "
	Escribir " 1- Ingrese los números que deseé sumar de uno en uno"
	Escribir " 2- Para detener el programa y ver el resultado de la suma "
	Escribir "    por favor ingrese un número negativo"
	Escribir " Escriba un primer número para sumar "
	// Los datos con la variable (Escribir) nos ayudarán a mostrar una interfaz mas entendible para el usuario
	
	Repetir // Esto indica el inicio de un ciclo condicional 
		
		Leer numero // Nos permite procesar el dato ingresado por el usuario
		si numero >= 0 Entonces // Indica la condición inicial para comenzar con el ciclo 
			Escribir " Ingrese el siguiente número a sumar " // Indicativo de interfaz de usuario 
			Escribir " O ingrese un número negativo para terminar " // Indicativo de interfaz de usuario 
		FinSi // Indica que termino la primera condicional del ciclo 
		
		Si numero > 0 Entonces // Establecemos una segunda condición dentro del mismo ciclo 
			suma <- suma + numero // Establecemos lo que queremos que le suceda a nuestra variable en este caso sumarle el dato que ingresó el usuario
		FinSi // Terminamos la condicional 
	Hasta Que numero < 0 //determinamos una condición que termine con el ciclo que iniciamos 
	Escribir " La suma de los números positivos es: ", suma // Mostramos el nuevo resultado almacenado en la variable (suma)
	
FinAlgoritmo // Termina el algoritmo 
// Autor: MaWhySha