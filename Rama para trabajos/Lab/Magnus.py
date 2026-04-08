# Ejercicio 8 con interfaz gráfica
import tkinter as tk
from tkinter import messagebox

def transformar_texto(texto, opcion):
    if opcion == 1:
        return texto.upper()
    elif opcion == 2:
        return texto.lower()
    elif opcion == 3:
        return texto.capitalize()
    else:
        return None

def aplicar_transformacion():
    texto = entrada_texto.get().strip()
    opcion = opcion_var.get()
    
    if opcion not in [1, 2, 3]:
        messagebox.showerror("Error", "Seleccione una opción válida (1,2 o 3)")
        return
    
    resultado = transformar_texto(texto, opcion)
    if resultado is not None:
        etiqueta_resultado.config(text=f"Resultado: {resultado}")

def limpiar_texto():
    entrada_texto.delete(0, tk.END)
    etiqueta_resultado.config(text="Resultado:")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Transformador de Texto")

# Entrada de texto
tk.Label(ventana, text="Ingrese un texto:").pack()
entrada_texto = tk.Entry(ventana, width=40)
entrada_texto.pack()

# Selección de opción
tk.Label(ventana, text="Seleccione una opción:").pack()
opcion_var = tk.IntVar()
tk.Radiobutton(ventana, text="1. MAYÚSCULAS", variable=opcion_var, value=1).pack(anchor="w")
tk.Radiobutton(ventana, text="2. minúsculas", variable=opcion_var, value=2).pack(anchor="w")
tk.Radiobutton(ventana, text="3. Primera letra mayúscula", variable=opcion_var, value=3).pack(anchor="w")

# Botones
tk.Button(ventana, text="Aplicar transformación", command=aplicar_transformacion).pack(pady=5)
tk.Button(ventana, text="Limpiar texto", command=limpiar_texto).pack(pady=5)

# Etiqueta para resultado
etiqueta_resultado = tk.Label(ventana, text="Resultado:", font=("Arial", 12))
etiqueta_resultado.pack(pady=10)

ventana.mainloop()

#MaWhySha
"""Nota:De antemano una diculpa este lo agrego como extra ya que hasta de 
ultimo comprendi la dinamica del laboratorio, y me parecio bien experimentar 
con una pequeña prueba de interfaz grafica en python utilizando tkinder,
apesar del evidente uso de inteligencia artificial planeo esforzarme 
para comprender como funciona el flujo de trabajo con codigo y la logica
de programación que hace que todo funcione y ya a mi ritmo ir aprendiendo 
de manera mas profesional un lenguaje de programación como lo es python pero
sin depender tanto de la IA para constuir codigo y poder crear cosas por mi mismo
es solo que me gusta bastante experimentar con herramientas como estas :)"""