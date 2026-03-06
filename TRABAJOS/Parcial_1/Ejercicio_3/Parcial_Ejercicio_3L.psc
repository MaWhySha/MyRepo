Algoritmo Parcial_Ejercicio_3L // Dias de la semana interactivos 
	
    Definir numero Como Entero
    Definir salir Como Logico
	
    salir <- Falso
	
	Repetir
        Escribir " Ingrese un número del 1 al 7 (0 para salir): "
        Leer numero
		Si numero = 0 Entonces
            salir <- Verdadero
		Sino
			Si numero < 1 O numero > 7 Entonces
                Escribir " Número inválido. Intente nuevamente. "
            Sino
                Según numero Hacer
			1:
				Escribir " Lunes "
			2:
				Escribir " Martes "
			3:
				Escribir " Miércoles "
			4:
				Escribir " Jueves "
			5:
				Escribir " Viernes "
			6:
				Escribir " Sábado "
			7:
				Escribir " Domingo "
		FinSegun
	FinSi
FinSi

Hasta Que salir = Verdadero

FinAlgoritmo
// Author: MaWhySha