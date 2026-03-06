Algoritmo Parcial_Ejercicio_1L //Calificación por estudiante 
	
	Definir nota Como Entero
	Escribir " Por favor ingrese la nota del estudiante, evite el uso de decimales. "
	
	Repetir
		Leer nota
		
		Si nota < 0 o nota > 10 Entonces
			Escribir " Formato de nota no valido... intente nuevamente. "
		FinSi
		
	Hasta Que nota >= 0 y nota <= 10
	
	Si nota >= 6 Entonces
		Escribir " Aprobado, felicidades. "
	SiNo
		Si nota = 5 Entonces
			Escribir " Necesita recuperación. "
		SiNo
			Escribir " Reprobado. "
		FinSi
	FinSi
	
FinAlgoritmo
// Autor: MaWhySha