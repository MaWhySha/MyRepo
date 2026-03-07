Algoritmo Parcial_Ejercicio_4E // Mostrar los primeros N números pares de un número N 
    
    Definir N, i Como Entero // Definimos (N) e (I) como nuestras variables para guardar datos númericos en formato de entero
	
    Repetir // Aqui indicamos el inicio de nuestro bucle condicional 
        Escribir "Ingrese un número N (mayor que 0):" // ESte será el mensaje que verá el usuario al solicitarle que ingrese un dato
        Leer N // Identificamos ese dato ingresado
		
        Si N <= 0 Entonces // Definimos una condición dentro del bucle para datos NO admitidos 
            Escribir "Número inválido. Debe ser mayor que 0." // Mostramos un mensaje para indicarle al usuario que fue lo que ocurrió
        FinSi // Determinamos el final de la condición 
    Hasta Que N > 0 // Definimos que condición se debe cumplir para terminar el bucle 
	
	// Cuando el bucle termine procederemos con lo sigiente
    Escribir "Los primeros ", N, " números pares son:" // Esto indicara el mensaje que acompañara el proceso siguiente 
	
    Para i <- 1 Hasta N Hacer // Esto hace que la variable (i) comience desde 1 hasta el número indicado en la variable (N)
        Escribir i * 2       // Aqui se tomarán los datos almacenados en la variable (i) y se multiplicarán por 2 y el valor resultante será mostrado en pantalla 
    FinPara // Aqui se indica el final de la situación
	
FinAlgoritmo // Termina todo el proceso 
// Autor: MaWhySha