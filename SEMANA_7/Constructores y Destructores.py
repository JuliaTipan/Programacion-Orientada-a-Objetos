class Libro:
    # Constructor: Inicializa los atributos del objeto
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        print(f"El libro '{self.titulo}' de {self.autor} ha sido creado.")

    # Metodo para mostrar información del libro
    def mostrar_informacion(self):
        print(f"Título: {self.titulo}, Autor: {self.autor}")

    # Destructor: Limpia recursos o realiza tareas al eliminar el objeto
    def __del__(self):
        print(f"El libro '{self.titulo}' de {self.autor} está siendo eliminado.")

# Programa principal
if __name__ == "__main__":
    # Crear una instancia de la clase Libro
    mi_libro = Libro("Crimen y Castigo", "Fiódor Dostoyesvki")
    # Llamar a un metodo de la clase
    mi_libro.mostrar_informacion()
    # Eliminar explícitamente el objeto
    del mi_libro

    print("Fin del programa.")

