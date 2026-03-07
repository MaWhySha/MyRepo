Algoritmo Parcial_Ejercicio_9E // Definir si un número es divisible por 3 o por 5 
	
    Definir numero Como Entero // Definimos nuestra variable como (Entero) para guardar datos en formato sin decimales 
	
    Escribir " Ingrese un número: " // Definimos nuestro primer mensaje para solicitar un dato al usuario 
    Leer numero // Guardamos el dato que nos de el usario en la variable 
	
    Si numero MOD 3 = 0 Y numero MOD 5 = 0 Entonces // Indicamos las dos condiciones para validar el dato proporcionado 
        Escribir " Verdadero, es divisible entre 3 y 5 " // Establecemos el mensaje que se mostrárá si este se cumple 
		
    SiNo // Si la condición anterior es falsa parcialmente 
        Si numero MOD 3 = 0 Entonces // Indicamos una condición (A) que se debe cumplir como minimo 
            Escribir " Verdadero, es divisible entre 3 " // Establecemos el mensaje que verá el usuario 
			
        SiNo // Si ninguna de las condicones anteriores es verdad procederemos de la siguiente manera 
            Si numero MOD 5 = 0 Entonces // Indicamos una condición (B) que se deberá cumplir 
                Escribir " Verdadero, es divisible entre 5 " // Definimos el mensaje que acompañara al dato 
				
            SiNo // Si ninguna condición anterior es verdadera 
                Escribir " Falso, no es divisible entre 3 ni entre 5 " // Mostraremos el siguiente mensaje indicando el resultado al usuario 
            FinSi // Indica el fin de la variable condicional (Si)
        FinSi // Indica el fin de la variable condicional (Si)
    FinSi // Indica el fin de la variable condicional (Si)
	
FinAlgoritmo // Terminá completamente el algoritmo 
// Autor: MaWhySha