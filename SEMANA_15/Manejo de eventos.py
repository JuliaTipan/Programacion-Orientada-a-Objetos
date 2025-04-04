import tkinter as tk
from tkinter import messagebox

def agregar_tarea(event=None):  # Permite agregar con botón o tecla Enter
    tarea = entrada_tarea.get().strip()
    if tarea:
        lista_tareas.insert(tk.END, tarea)  # Agrega la tarea al Listbox
        entrada_tarea.delete(0, tk.END)  # Limpia el campo de entrada
    else:
        messagebox.showwarning("Advertencia", "La tarea no puede estar vacía.")

def marcar_completada():
    try:
        index = lista_tareas.curselection()[0]  # Obtiene la tarea seleccionada
        tarea = lista_tareas.get(index)
        lista_tareas.delete(index)
        lista_tareas.insert(tk.END, f"✔ {tarea}")  # Marca como completada
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para marcar como completada.")

def eliminar_tarea():
    try:
        index = lista_tareas.curselection()[0]  # Obtiene el indice de la tarea seleccionada
        lista_tareas.delete(index)  # Elimina la tarea
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar.")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Lista de Tareas")
root.geometry("400x400")

# Campo de entrada de tareas
entrada_tarea = tk.Entry(root, width=40)
entrada_tarea.pack(pady=10)
entrada_tarea.bind("<Return>", agregar_tarea)  # Agregar tarea con Enter

# Botones de acción
btn_agregar = tk.Button(root, text="Añadir Tarea", command=agregar_tarea)
btn_agregar.pack()

btn_completar = tk.Button(root, text="Marcar como Completada", command=marcar_completada)
btn_completar.pack()

btn_eliminar = tk.Button(root, text="Eliminar Tarea", command=eliminar_tarea)
btn_eliminar.pack()

# Lista de tareas
lista_tareas = tk.Listbox(root, width=50, height=15)
lista_tareas.pack(pady=10)

# Ejecutar la aplicación
root.mainloop()