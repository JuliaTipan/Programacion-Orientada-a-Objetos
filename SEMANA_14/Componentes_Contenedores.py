import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry  # Asegurar la instalación tkcalendar con 'pip install tkcalendar'

# Crear la ventana principal
root = tk.Tk()
root.title("Agenda Personal")  # Título de la ventana
root.geometry("500x400")  # Tamaño de la ventana

# Función para agregar un evento
def agregar_evento():
    """Añade un evento a la lista si todos los campos están completos."""
    fecha = entry_fecha.get()
    hora = entry_hora.get()
    descripcion = entry_descripcion.get()
    if fecha and hora and descripcion:
        tree.insert("", "end", values=(fecha, hora, descripcion))  # Agrega el evento a la tabla
        entry_fecha.set_date("")  # Limpia el campo de fecha
        entry_hora.delete(0, tk.END)  # Limpia el campo de hora
        entry_descripcion.delete(0, tk.END)  # Limpia el campo de descripción
    else:
        messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")  # Muestra advertencia

# Función para eliminar un evento
def eliminar_evento():
    """Elimina el evento seleccionado de la lista."""
    seleccionado = tree.selection()
    if seleccionado:
        tree.delete(seleccionado)  # Elimina el evento seleccionado
    else:
        messagebox.showwarning("Advertencia", "Seleccione un evento para eliminar")  # Muestra advertencia

# Crear Frame para entradas
frame_entrada = tk.Frame(root)
frame_entrada.pack(pady=10)

# Campos de entrada
tk.Label(frame_entrada, text="Fecha:").grid(row=0, column=0)
entry_fecha = DateEntry(frame_entrada, width=12, background='darkblue', foreground='white', borderwidth=2)
entry_fecha.grid(row=0, column=1)

tk.Label(frame_entrada, text="Hora:").grid(row=1, column=0)
entry_hora = tk.Entry(frame_entrada)
entry_hora.grid(row=1, column=1)

tk.Label(frame_entrada, text="Descripción:").grid(row=2, column=0)
entry_descripcion = tk.Entry(frame_entrada)
entry_descripcion.grid(row=2, column=1)

# Botones
frame_botones = tk.Frame(root)
frame_botones.pack()

btn_agregar = tk.Button(frame_botones, text="Agregar Evento", command=agregar_evento)
btn_agregar.grid(row=0, column=0, padx=5, pady=5)

btn_eliminar = tk.Button(frame_botones, text="Eliminar Evento", command=eliminar_evento)
btn_eliminar.grid(row=0, column=1, padx=5, pady=5)

btn_salir = tk.Button(frame_botones, text="Salir", command=root.quit)
btn_salir.grid(row=0, column=2, padx=5, pady=5)

# Tabla de eventos
frame_tabla = tk.Frame(root)
frame_tabla.pack()

# Definir columnas de la tabla
columns = ("Fecha", "Hora", "Descripción")
tree = ttk.Treeview(frame_tabla, columns=columns, show="headings")

# Configurar encabezados de la tabla
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=120)

tree.pack()

# Ejecutar la aplicación
tk.mainloop()

