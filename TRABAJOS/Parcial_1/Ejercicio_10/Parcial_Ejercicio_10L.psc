Algoritmo Parcial_Ejercicio_10L // Determinar el mayor y menor al comparar dos números N 
	
    Definir num1, num2 Como Real
	
	Escribir " Bienvenido/Bienvenida "
    Escribir " Por favor ingrese el primer número: "
    Leer num1
	
    Escribir " Ingrese el segundo número: "
    Leer num2
	
    Si num1 > num2 Entonces
        Escribir " El número mayor es: ", num1
        Escribir " El número menor es: ", num2
		
    SiNo
        Si num2 > num1 Entonces
            Escribir " El número mayor es: ", num2
            Escribir " El número menor es: ", num1
			
        SiNo
            Escribir " Ambos números son iguales "
        FinSi
    FinSi
	
FinAlgoritmo
// Autor: MaWhySha 