# Importamos la librería Tkinter para crear la interfaz gráfica
import tkinter as tk
from tkinter import messagebox  # (opcional) para mostrar mensajes emergentes

# Clase principal de la aplicación
class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")           # Título de la ventana
        self.root.geometry("400x400")                 # Tamaño de la ventana

        # Campo de entrada de texto para nuevas tareas
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)                 # Margen vertical
        self.task_entry.focus()                       # Enfoca automáticamente el Entry

        # Botón para añadir tarea
        self.add_button = tk.Button(root, text="Añadir Tarea", command=self.add_task)
        self.add_button.pack(pady=5)

        # Lista donde se mostrarán las tareas
        self.task_listbox = tk.Listbox(root, width=50, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10)

        # Botón para marcar tarea como completada
        self.complete_button = tk.Button(root, text="Marcar como Completada", command=self.complete_task)
        self.complete_button.pack(pady=5)

        # Botón para eliminar tarea
        self.delete_button = tk.Button(root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.pack(pady=5)

        # Atajos de teclado
        root.bind("<Return>", lambda event: self.add_task())     # Enter para añadir tarea
        root.bind("<c>", lambda event: self.complete_task())     # C para completar
        root.bind("<d>", lambda event: self.delete_task())       # D para eliminar
        root.bind("<Delete>", lambda event: self.delete_task())  # Supr para eliminar también
        root.bind("<Escape>", lambda event: root.quit())         # Esc para cerrar la app

        # Lista interna de tareas (cada tarea es una tupla: (texto, completado))
        self.tasks = []

    # Función para añadir una nueva tarea
    def add_task(self):
        task = self.task_entry.get().strip()        # Obtenemos el texto del Entry
        if task:
            self.tasks.append((task, False))        # Agregamos la tarea como pendiente (False)
            self.update_listbox()                   # Actualizamos la lista visual
            self.task_entry.delete(0, tk.END)       # Limpiamos el Entry

    # Función para marcar como completada la tarea seleccionada
    def complete_task(self):
        selected = self.task_listbox.curselection()  # Obtenemos el índice seleccionado
        if selected:
            index = selected[0]
            task, _ = self.tasks[index]
            self.tasks[index] = (task, True)         # Marcamos como completada
            self.update_listbox()                    # Actualizamos la vista

    # Función para eliminar la tarea seleccionada
    def delete_task(self):
        selected = self.task_listbox.curselection()  # Obtenemos el índice seleccionado
        if selected:
            index = selected[0]
            self.tasks.pop(index)                    # Eliminamos la tarea
            self.update_listbox()                    # Actualizamos la lista

    # Función para actualizar el contenido del Listbox
    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)          # Limpiamos la lista
        for task, completed in self.tasks:
            # Indicamos si la tarea está completada o no
            display = f"[✔] {task}" if completed else f"[ ] {task}"
            self.task_listbox.insert(tk.END, display)  # Añadimos la tarea al Listbox

# Código principal que ejecuta la aplicación
if __name__ == "__main__":
    root = tk.Tk()                    # Creamos la ventana principal
    app = TaskManagerApp(root)       # Instanciamos la aplicación
    root.mainloop()                  # Iniciamos el bucle de eventos
