Algoritmo Parcial_Ejercicio_4L // Mostrar los primeros N números pares de un número N 
    
    Definir N, i Como Entero
	
    Repetir
        Escribir "Ingrese un número N (mayor que 0):"
        Leer N
		
        Si N <= 0 Entonces
            Escribir "Número inválido. Debe ser mayor que 0."
        FinSi
    Hasta Que N > 0
	
    Escribir "Los primeros ", N, " números pares son:"
	
    Para i <- 1 Hasta N Hacer
        Escribir i * 2
    FinPara
	
FinAlgoritmo
// Autor: MaWhySha