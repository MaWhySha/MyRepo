Algoritmo Parcial_Ejercicio_7E //Producto y cociente de dos números
	
    Definir num1, num2, producto, cociente Como Real // Primero definimos nuestras variables como real para poder manejar datos en decimales y enteros 
	
	Escribir " Bienvenido/Bienvenida al programa " // Establecemos un mensaje de bienvenida 
    Escribir " Ingrese el primer número: " // Indicamos lo que se le pedirá al usuario 
    Leer num1 // Almacenamos el primer número en la variable 
	
    Escribir " Ingrese el segundo número: " // Indicamos una nueva solicitud al usuario 
    Leer num2 // Guardamos el dato ingresado en nuestra otra variable 
	
    producto <- num1 * num2 // Indicamos el valor de la variable (producto)
    Escribir " El producto es: ", producto // Definimos el mensaje que acompañara al resultado de la operación 
	
    Si num2 <> 0 Entonces // Definimos una condición para evitar errores al dividir por 0
        cociente <- num1 / num2 // Indicamos el valor para la variable (cociente)
        Escribir " El cociente es: ", cociente // Definimos el mensaje que acompañara al resultado de la operación 
    SiNo // Si la condición que definimos antes no se cumple se mostrará el siguiente mensaje al usuario 
        Escribir " No se puede dividir entre 0 " // Definimos el mensaje que verá el usuario 
    FinSi // Terminamos con el proceso condicional (Si)
	
FinAlgoritmo // Finaliza todo el algoritmo 
// Autor: MaWhySha