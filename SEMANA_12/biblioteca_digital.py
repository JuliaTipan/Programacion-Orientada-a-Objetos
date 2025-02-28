class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.info = (autor, titulo)  # Tupla para autor y título (inmutable)
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.info[1]} por {self.info[0]} (Categoría: {self.categoria}, ISBN: {self.isbn})"

class Usuario:
    def __init__(self, nombre, usuario_id):
        self.nombre = nombre
        self.usuario_id = usuario_id
        self.libros_prestados = []  # Lista de libros prestados

    def __str__(self):
        return f"Usuario: {self.nombre}, ID: {self.usuario_id}, Libros prestados: {len(self.libros_prestados)}"

class Biblioteca:
    def __init__(self):
        self.libros_disponibles = {}  # Diccionario con ISBN como clave
        self.usuarios_registrados = set()  # Conjunto de IDs de usuario únicos
        self.historial_prestamos = {}  # Registro de libros prestados

    def agregar_libro(self, libro):
        self.libros_disponibles[libro.isbn] = libro
        print(f"Libro agregado: {libro}")

    def quitar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            del self.libros_disponibles[isbn]
            print(f"Libro con ISBN {isbn} eliminado.")
        else:
            print("Libro no encontrado.")

    def registrar_usuario(self, usuario):
        if usuario.usuario_id in self.usuarios_registrados:
            print("El usuario ya está registrado.")
        else:
            self.usuarios_registrados.add(usuario.usuario_id)
            self.historial_prestamos[usuario.usuario_id] = []
            print(f"Usuario registrado: {usuario}")

    def dar_de_baja_usuario(self, usuario_id):
        if usuario_id in self.usuarios_registrados:
            self.usuarios_registrados.remove(usuario_id)
            del self.historial_prestamos[usuario_id]
            print(f"Usuario con ID {usuario_id} dado de baja.")
        else:
            print("Usuario no encontrado.")

    def prestar_libro(self, usuario, isbn):
        if isbn in self.libros_disponibles and usuario.usuario_id in self.usuarios_registrados:
            libro = self.libros_disponibles.pop(isbn)
            usuario.libros_prestados.append(libro)
            self.historial_prestamos[usuario.usuario_id].append(libro)
            print(f"Libro prestado a {usuario.nombre}: {libro}")
        else:
            print("Préstamo no posible.")

    def devolver_libro(self, usuario, isbn):
        for libro in usuario.libros_prestados:
            if libro.isbn == isbn:
                usuario.libros_prestados.remove(libro)
                self.libros_disponibles[isbn] = libro
                print(f"Libro devuelto: {libro}")
                return
        print("El usuario no tiene este libro en préstamo.")

    def buscar_libro(self, criterio, valor):
        encontrados = [libro for libro in self.libros_disponibles.values() if getattr(libro, criterio) == valor]
        if encontrados:
            print("Libros encontrados:")
            for libro in encontrados:
                print(libro)
        else:
            print("No se encontraron libros con ese criterio.")

    def listar_libros_prestados(self, usuario):
        if usuario.libros_prestados:
            print(f"Libros prestados a {usuario.nombre}:")
            for libro in usuario.libros_prestados:
                print(libro)
        else:
            print("El usuario no tiene libros prestados.")

# Prueba del sistema
biblioteca = Biblioteca()
libro1 = Libro("Alicia en el pais de las maravillas", "Lewis Carrol", "Ficción", "9788408277163")
libro2 = Libro("Orgullo y Prejuicio", "Jane Austen", "Novela", "9789588925738")
usuario1 = Usuario("Carlos Vargas", 1)

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.registrar_usuario(usuario1)
biblioteca.prestar_libro(usuario1, "9789588925738")
biblioteca.listar_libros_prestados(usuario1)
biblioteca.devolver_libro(usuario1, "9789588925738")
biblioteca.listar_libros_prestados(usuario1)