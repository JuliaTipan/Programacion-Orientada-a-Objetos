# Definición de la clase base con encapsulación
class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # Encapsulación con atributo privado para proteger los datos
        self.__edad = edad

    # Métodos getters para acceder a los atributos privados
    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    # Metodo para mostrar información básica de la persona
    def mostrar_info(self):
        print(f"Nombre: {self.__nombre}, Edad: {self.__edad}")

# Definición de una clase derivada (herencia desde Persona)
class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)  # Llamando al constructor de la clase base
        self.carrera = carrera

    # Sobrescritura de metodo para mostrar información del estudiante
    def mostrar_info(self):
        print(f"Nombre: {self.get_nombre()}, Edad: {self.get_edad()}, Carrera: {self.carrera}")

# Definición de otra clase con polimorfismo de argumentos múltiples
class Profesor(Persona):
    def __init__(self, nombre, edad, materia):
        super().__init__(nombre, edad)
        self.materia = materia

    # Polimorfismo con diferentes argumentos para mostrar información detallada o básica
    def mostrar_info(self, detallado=False):
        if detallado:
            print(f"Profesor: {self.get_nombre()}, Edad: {self.get_edad()}, Materia: {self.materia}")
        else:
            print(f"Profesor: {self.get_nombre()}")

# Crear instancias de las clases y demostrar su funcionalidad
persona1 = Persona("Jona", 28)
estudiante1 = Estudiante("Carlos", 23, "Ingeniería")
profesor1 = Profesor("Ing. Vargas", 40, "Física")

# Uso de los métodos para mostrar información de los objetos
print("--- Información General ---")
persona1.mostrar_info()
estudiante1.mostrar_info()
profesor1.mostrar_info(True)

# Demostración de encapsulación intentando acceder al atributo privado
print("\nIntento de acceso directo al atributo privado:")
try:
    print(persona1.__nombre)
except AttributeError:
    print("Acceso directo al atributo privado no permitido")