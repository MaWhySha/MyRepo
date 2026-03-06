Algoritmo Codigo_Lab_Explicado// Aqui se determina el inició del algoritmo y se le asigna un nombre 
	
    // Declaración de variables
    Definir numero Como Real // Esto guardara el valor que se le asigne y se ha definido para almacenar números con decimales
    Definir divisor Como Real // Esto guardara el valor que se le asigne y se ha definido pra almacenar números con decimales
    Definir contador Como Entero // Esto guardara la cantidad de veces que el proceso anterior se realice y este se puedra definir con enteros
    Definir continuar Como Logico // Esto designa a la variable la capacidad de depender de una condición que puede ser verdadera o falsa 
	
    contador <- 0 // Indica el punto de partida del contador en este caso 0
    continuar <- Verdadero // Al indicar que esta condición es verdadera le permite arrancar con el proceso hasta que se cambie dicha condición
	
    // Entrada de datos
    Escribir "Ingrese un numero mayor que 2:" // Esto muestra un mensaje para solicitar al usuario que ingrese un número 
    Leer numero // Esto leera el dato ingresado y lo guardara en la variable numero
	
    Escribir "Ingrese el divisor:" // Esto muestra un mensaje para solicitar al usuario que ingrese un número que hara de divisor 
    Leer divisor // Esto leera el dato ingresado y lo guardara en la variable divisor
	
    Repetir // Esto define una variable que comience con el proceso que dependera de una condición 
			// A diferencia de la variable mientras la variable repetir cumple la misma función pero comenzara a operar antes de verificar dicha condicion 
		
        numero <- numero / divisor // Esto indica que se hara con la variable anterior Numero que en este caso se dividira entre la variable Divisor
        contador <- contador + 1 // Esto guardara el dato de cada vez que se repita el proceso de división sumando +1 en cada vuelta del ciclo
		
        Escribir "Resultado actual: ", numero // Esta parte mostrará en pantalla cada resultado por vuelta hasta que se termine el proceso 
		
        continuar <- NO (numero < 2) // Esto determinará la condición que detendrá el ciclo 
		
    Hasta Que continuar = Falso O divisor = 0 // Aqui esta lo que permite que el proceso se detenga si la condición se cumple 
	
    Escribir "Numero final: ", numero // Luego de terminar el proceso se mostrará en pantalla el ultimo valor luego de cumplir la condición
    Escribir "Cantidad de divisiones: ", contador // Tambien se mostrará en pantalla el dato guardado en la variable contador
	// Esto indica la cantidad de veces que se repitió el ciclo antes de que se cumpliera la condición 
FinAlgoritmo //Esto indica el final de todo el algoritmo 

// Nota, hay ciertos valores que por su naturaleza rompen el codigo tales como.
// Divisor = 1, este generará un bucle infinito dado que la condición de Numero < 2 nunca se cumple.
// Divisor = 0, Dado que no se puede dividir entre 0 el programa se rompe.
// Dividor = -1, Si el divisor es negativo no romperá como tal el codigo pero solo ejecutará un paso antes de detenerse.
// Divisor = 0.5, Si el número divisor es un número decimal se crea una situación que tiende a infinito.
