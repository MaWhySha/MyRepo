Algoritmo Parcial_Ejercicio_10E // Determinar el mayor y menor al comparar dos números N 
	
    Definir num1, num2 Como Real // Definiremos primeramente las dos variables que utilizaremos como un (Real) para poder hacer uso de decimales 
	
	Escribir " Bienvenido/Bienvenida " // Ingresamos un mensaje de bienvenida que verá el usuario 
    Escribir " Por favor ingrese el primer número: " // Solicitaremos el primer dato al usuario 
    Leer num1 // Guardaremos ese dato en nuestra primer variable (num1) para usarlo después 
	
    Escribir " Ingrese el segundo número: " // Solicitamos un segundo dato al usuario 
    Leer num2 // Guardamos este nuevo dato igualmente en una segunda variable esta vez (num2) para utiliarlo después 
	
    Si num1 > num2 Entonces // Establecemos una condición para comparar ambos números 
        Escribir " El número mayor es: ", num1 // Definimos un mensaje junto con el dato de la operación (Mayor)
        Escribir " El número menor es: ", num2 // Definimos un mensaje junto con el dato de la operación (Menor)
		// Si la variable (num1) es mayor se aplicará el mensaje anterior 
		
    SiNo // Si la condición anterior resulta ser falsa procederemos de la siguiente manera 
        Si num2 > num1 Entonces // Establecemos una segunda condición para comparar ambos números de manera contraria 
            Escribir " El número mayor es: ", num2 // Definimos un mensaje junto con el dato de la operación (Mayor)
            Escribir " El número menor es: ", num1 // Definimos un mensaje junto con el dato de la operación (Menor)
			
        SiNo // Creamos una tercera condicional que procederá si las dos anteriores son falsas indicando igualdad en los datos ingresados por el usuario 
            Escribir " Ambos números son iguales " // Se determina el mensaje que se mostrará si la condicional es verdadera 
        FinSi // Indicamos el final de la condicional (Si)
    FinSi // Indicamos el final de  la condicional (Si)
	
FinAlgoritmo // Termina completamente el proceso 
// Autor: MaWhySha 