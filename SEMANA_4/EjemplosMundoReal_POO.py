# Clase que representa una habitación de hostal
class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero  # Número de la habitación
        self.tipo = tipo  # Tipo de habitación (individual, doble, suite, etc.)
        self.precio = precio  # Precio por noche
        self.disponible = True  # Estado de disponibilidad

    # Metodo para reservar una habitación
    def reservar(self):
        if self.disponible:
            self.disponible = False
            print(f"Habitación {self.numero} reservada exitosamente.")
        else:
            print(f"La habitación {self.numero} ya está reservada.")

    # Metodo para liberar una habitación
    def liberar(self):
        self.disponible = True
        print(f"Habitación {self.numero} ha sido liberada.")

# Clase que representa un hostal
class Hostal:
    def __init__(self, nombre):
        self.nombre = nombre  # Nombre del hostal
        self.habitaciones = []  # Lista de habitaciones disponibles en el hostal

    # Metodo para agregar una habitación al hostal
    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    # Metodo para mostrar las habitaciones disponibles en el hostal
    def mostrar_habitaciones_disponibles(self):
        print(f"Habitaciones disponibles en {self.nombre}:")
        for habitacion in self.habitaciones:
            if habitacion.disponible:
                print(f"Número: {habitacion.numero}, Tipo: {habitacion.tipo}, Precio: {habitacion.precio}")

# Crear un hostal y algunas habitaciones
hostal = Hostal("Hostal Blue")
hab1 = Habitacion(10, "Individual", 30)
hab2 = Habitacion(12, "Doble", 50)

# Agregar habitaciones al hostal
hostal.agregar_habitacion(hab1)
hostal.agregar_habitacion(hab2)

# Interacciones con el sistema
hostal.mostrar_habitaciones_disponibles()
hab1.reservar()
hostal.mostrar_habitaciones_disponibles()
hab1.liberar()
hostal.mostrar_habitaciones_disponibles()

