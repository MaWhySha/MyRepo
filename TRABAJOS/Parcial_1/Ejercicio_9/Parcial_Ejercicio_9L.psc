Algoritmo Parcial_Ejercicio_9L // Definir si un número es divisible por 3 o por 5 
	
    Definir numero Como Entero
	
    Escribir "Ingrese un número:"
    Leer numero
	
    Si numero MOD 3 = 0 Y numero MOD 5 = 0 Entonces
        Escribir "Verdadero, es divisible entre 3 y 5"
		
    SiNo
        Si numero MOD 3 = 0 Entonces
            Escribir "Verdadero, es divisible entre 3"
			
        SiNo
            Si numero MOD 5 = 0 Entonces
                Escribir "Verdadero, es divisible entre 5"
				
            SiNo
                Escribir "Falso, no es divisible entre 3 ni entre 5"
            FinSi
        FinSi
    FinSi
	
FinAlgoritmo
// Autor: MaWhySha