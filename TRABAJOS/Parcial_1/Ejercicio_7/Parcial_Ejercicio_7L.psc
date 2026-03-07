Algoritmo Parcial_Ejercicio_7L //Producto y cociente de dos números
	
    Definir num1, num2, producto, cociente Como Real
	
	Escribir " Bienvenido/Bienvenida al programa "
    Escribir " Ingrese el primer número: "
    Leer num1
	
    Escribir " Ingrese el segundo número: "
    Leer num2
	
    producto <- num1 * num2
    Escribir " El producto es: ", producto
	
    Si num2 <> 0 Entonces
        cociente <- num1 / num2
        Escribir " El cociente es: ", cociente
    SiNo
        Escribir " No se puede dividir entre 0 "
    FinSi
	
FinAlgoritmo
// Autor: MaWhySha