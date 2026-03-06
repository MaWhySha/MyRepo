Algoritmo Codigo_Lab_Limpio
	
    Definir numero Como Real 
    Definir divisor Como Real 
    Definir contador Como Entero 
    Definir continuar Como Logico 
	
    contador <- 0 
    continuar <- Verdadero 
	
    Escribir "Ingrese un numero mayor que 2:" 
    Leer numero 
	
    Escribir "Ingrese el divisor:" 
    Leer divisor 
	
    Repetir 
		
        numero <- numero / divisor 
        contador <- contador + 1 
		
        Escribir "Resultado actual: ", numero 
		
        continuar <- NO (numero < 2) 
		
    Hasta Que continuar = Falso O divisor = 0 
	
    Escribir "Numero final: ", numero 
    Escribir "Cantidad de divisiones: ", contador 
	
FinAlgoritmo 
