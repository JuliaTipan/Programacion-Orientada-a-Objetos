import tkinter as tk  # Importamos la librería Tkinter para la GUI
from tkinter import messagebox  # Importamos messagebox para mostrar advertencias

# Función para agregar un elemento a la lista
def agregar_elemento():
    elemento = entrada.get()  # Obtenemos el texto ingresado en el campo de entrada
    if elemento:
        lista.insert(tk.END, elemento)  # Agregamos el elemento a la lista
        entrada.delete(0, tk.END)  # Limpiamos el campo de entrada
    else:
        messagebox.showwarning("Advertencia", "El campo de texto está vacío.")  # Mostramos una advertencia si el campo está vacío

# Función para limpiar la lista
def limpiar_lista():
    lista.delete(0, tk.END)  # Eliminamos todos los elementos de la lista

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Gestor de Lista")  # Establecemos el título de la ventana
ventana.geometry("300x300")  # Definimos el tamaño de la ventana

# Etiqueta para indicar la función del campo de entrada
etiqueta = tk.Label(ventana, text="Ingrese un elemento:")
etiqueta.pack(pady=5)

# Campo de entrada para que el usuario ingrese un elemento
entrada = tk.Entry(ventana, width=30)
entrada.pack(pady=5)

# Botón para agregar elementos a la lista
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_elemento)
boton_agregar.pack(pady=5)

# Lista donde se mostrarán los elementos agregados
lista = tk.Listbox(ventana, width=40, height=10)
lista.pack(pady=5)

# Botón para limpiar la lista
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_lista)
boton_limpiar.pack(pady=5)

# Iniciamos el bucle principal de la aplicación para que la GUI funcione
ventana.mainloop()