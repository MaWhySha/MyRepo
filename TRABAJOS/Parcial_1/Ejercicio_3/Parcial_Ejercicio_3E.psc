Algoritmo Parcial_Ejercicio_3E // Dias de la semana interactivos 
	
    Definir numero Como Entero // Definimos nuestra primera variable como un entero (Para almacenar datos sin decimales)
    Definir salir Como Logico // Creamos y definimos la variable (salir) como logico (Esto nos permite designarle un estado inicial para usarla correctamente)
	
    salir <- Falso // Le damos el estado inicial de falso a la variable antes de iniciar el proceso del bucle
	
	Repetir // El repetir es el que nos ayudará a crear un bucle condicional 
        Escribir " Ingrese un número del 1 al 7 (0 para salir): " // Mensaje que verá el usuario solicitando un número 
        Leer numero // Almacenamos ese número ingresado
		Si numero = 0 Entonces // Definimos un valor especifico que utilice nuestra variable condicional para detener el proceso
            salir <- Verdadero // Si el valor es correcto el estado de la variable cambiara a verdadero, terminando el proceso
		Sino // Mientras esa orden no suceda ocurrirá lo siguiente 
			Si numero < 1 O numero > 7 Entonces // Definimos una condición que limite valores aceptados 
                Escribir " Número inválido. Intente nuevamente. " // Indicamos un mensaje que verá el usuario si la condición no se cumplé
            Sino // Si la condición anterior es correcta, procederemos 
                Según numero Hacer // Indicamos que generará el programa según los datos aceptados 
			1:
				Escribir " Lunes "
			2:
				Escribir " Martes "
			3:
				Escribir " Miércoles "   // Aqui definimos un valor para cada dato anteriormente validado
			4:
				Escribir " Jueves "
			5:
				Escribir " Viernes "
			6:
				Escribir " Sábado "
			7:
				Escribir " Domingo "
		FinSegun // Indica el final de la agrupación anterior 
	FinSi // Finaliza el proceso de la definición de condiciones validas 
FinSi // Finaliza la primera agrupación del Si 

Hasta Que salir = Verdadero // Termina con el bucle que definimos al principio

FinAlgoritmo // Fin de todo el proceso
// Author: MaWhySha