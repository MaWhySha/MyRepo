Algoritmo Parcial_Ejercicio_5E // Solicitar un número del 1 al 10 hasta que el número sea inválido
	
    Definir num Como Entero //  Definimos nuestra variable como entero para poder operar con números enteros
    
	Escribir " Bienvenido/Bienvenida " // Mensaje que verá el usuario
    Escribir " Ingrese un número entre 1 y 10: " // Indicación que se le dará al usuario 
    Leer num // Guardamos el dato ingresado por el usuario 
    
    Mientras num >= 1 Y num <= 10 Hacer // Indicamos un bucle con una condición que determinará cuanto se repetirá
        Escribir " Número válido. " // Mensaje que acompañara el proceso indicando validez 
        Escribir " Ingrese otro número entre 1 y 10: " // Mensaje que acompañara el proceso indicando validez 
        Leer num // Guardamos el siguiente número ingresado
    FinMientras // Terminamos con la condición del bucle 
    
    Escribir " Número inválido. Fin del programa. " // Mensaje que indicara el final del proceso 
    
FinAlgoritmo // Terminá directamente todos los procesos 
// Author: MaWhySha 