Algoritmo Parcial_Ejercicio_1E //Calificación por estudiante 
	
	Definir nota Como Entero // Al definir la variable (nota) como entero nos permite guardar un valor en ella como un número sin decimales 
	Escribir " Por favor ingrese la nota del estudiante, evite el uso de decimales. " // Indicamos el mensaje que queremos que el usuario vea al ingresar 
	
	Repetir // Esto nos ayudará a solicitar nuevamente una cantidad si el usuario ingreso un número NO valido 
		Leer nota // Primero necesitamos guardar el dato que nos proporcionó el usuario en una variable, en este caso (nota)
		
		Si nota < 0 o nota > 10 Entonces // Este sera nuestro criterio para aprobar o denegar el dato que ingreso el usuario
			Escribir " Formato de nota no valido... intente nuevamente. " // Mensaje que el usuario vera si el dato ingresado no cumple con la condición 
		FinSi // Indica que termino un proceso condicional, en este caso (Si)
		
	Hasta Que nota >= 0 y nota <= 10 // Esto determinará cuando se dejara de solicitar al usuario que reingrese un dato y terminara el bucle condicional 
	
	Si nota >= 6 Entonces // Aqui determinaremos nuestros criterios de agrupación segun el número ingresado que ya cumplio con la condición anterior 
		Escribir " Aprobado, felicidades. " // Si la condición anterior se cumple el usuario verá el siguiente mensaje
	SiNo // Creamos una condición dependiente que actuará si la anterior no se cumple 
		Si nota = 5 Entonces // Definimos dicha condición dependiente 
			Escribir " Necesita recuperación. " // Agregamos el mensaje que queramos mostrar
		SiNo // Creamos una nueva condicional dependiente a las 2 anteriores 
			Escribir " Reprobado. " // Definimos el mensaje que se mostrará 
		FinSi // Cerramos la condición 
	FinSi // Cerramos la condición 
	
FinAlgoritmo // indicamos el final del proceso 
// Autor: MaWhySha