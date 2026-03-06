Algoritmo Parcial_Ejercicio_2L // Suma de números positivos 
	
	Definir numero, suma Como Entero
	suma <- 0
	
	Escribir " Bienvenido/Bienvenida al programa de suma "
	Escribir " 1- Ingrese los números que deseé sumar de uno en uno"
	Escribir " 2- Para detener el programa y ver el resultado de la suma "
	Escribir "    por favor ingrese un número negativo"
	Escribir " Escriba un primer número para sumar "
	
	Repetir
		
		Leer numero
		si numero >= 0 Entonces
			Escribir " Ingrese el siguiente número a sumar "
			Escribir " O ingrese un número negativo para terminar "
		FinSi
		
		Si numero > 0 Entonces
			suma <- suma + numero
		FinSi
	Hasta Que numero < 0
	Escribir " La suma de los números positivos es: ", suma 
	
FinAlgoritmo
// Autor: MaWhySha
