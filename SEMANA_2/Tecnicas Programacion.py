# Abstracción
# Se ocultan los detalles internos de implementación y se expone solo lo necesario para interactuar con los objetos.
class Personaje:

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    def atributos(self):
        # Metodo que muestra los atributos relevantes del personaje.
        print(self.nombre, ":", sep="")
        print("·Fuerza:", self.fuerza)
        print("·Inteligencia:", self.inteligencia)
        print("·Defensa:", self.defensa)
        print("·Vida:", self.vida)

    def subir_nivel(self, fuerza, inteligencia, defensa):
        # Metodo que mejora los atributos del personaje.
        self.fuerza += fuerza
        self.inteligencia += inteligencia
        self.defensa += defensa

    def esta_vivo(self):
        # Devuelve True si el personaje tiene vida mayor a 0.
        return self.vida > 0

    def morir(self):
        # Cambia el estado de vida del personaje a muerto.
        self.vida = 0
        print(self.nombre, "ha muerto")

    def daño(self, enemigo):
        # Metodo para calcular el daño realizado a un enemigo.
        return self.fuerza - enemigo.defensa

    def atacar(self, enemigo):
        # Metodo que realiza un ataque a otro personaje.
        daño = self.daño(enemigo)
        enemigo.vida -= daño
        print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
        if enemigo.esta_vivo():
            print("Vida de", enemigo.nombre, "es", enemigo.vida)
        else:
            enemigo.morir()

# Herencia
# Las clases Guerrero y Mago heredan de la clase base Personaje y extienden o sobrescriben sus métodos.
class Guerrero(Personaje):

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada

    def cambiar_arma(self):
        # Metodo exclusivo de Guerrero para cambiar su arma.
        opcion = int(input("Elige un arma: (1) Acero Valyrio, daño 8. (2) Matadragones, daño 10"))
        if opcion == 1:
            self.espada = 8
        elif opcion == 2:
            self.espada = 10
        else:
            print("Número de arma incorrecta")

    def atributos(self):
        # Sobrescribe el metodo atributos para incluir el atributo espada.
        super().atributos()
        print("·Espada:", self.espada)

    def daño(self, enemigo):
        # Sobrescribe el cálculo del daño considerando el atributo espada.
        return self.fuerza * self.espada - enemigo.defensa

class Mago(Personaje):

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro

    def atributos(self):
        # Sobrescribe el metodo atributos para incluir el atributo libro.
        super().atributos()
        print("·Libro:", self.libro)

    def daño(self, enemigo):
        # Sobrescribe el cálculo del daño considerando el atributo libro.
        return self.inteligencia * self.libro - enemigo.defensa

# Polimorfismo
# Tanto Guerrero como Mago tienen implementaciones específicas del metodo daño y atributos.
def combate(jugador_1, jugador_2):
    # Metodo genérico que funciona para cualquier objeto que herede de Personaje.
    turno = 0
    while jugador_1.esta_vivo() and jugador_2.esta_vivo():
        print("\nTurno", turno)
        print(">>> Acción de ", jugador_1.nombre, ":", sep="")
        jugador_1.atacar(jugador_2)
        print(">>> Acción de ", jugador_2.nombre, ":", sep="")
        jugador_2.atacar(jugador_1)
        turno += 1
    if jugador_1.esta_vivo():
        print("\nHa ganado", jugador_1.nombre)
    elif jugador_2.esta_vivo():
        print("\nHa ganado", jugador_2.nombre)
    else:
        print("\nEmpate")

# Encapsulamiento
# Los atributos como nombre, fuerza, inteligencia, defensa y vida están protegidos
# y se acceden mediante métodos de la clase para evitar modificaciones directas inapropiadas.

# Creación de objetos y prueba de funcionalidad
personaje_1 = Guerrero("Max", 10, 20, 4, 100, 4)
personaje_2 = Mago("Lía", 5, 25, 4, 100, 3)

personaje_1.atributos()
personaje_2.atributos()

combate(personaje_1, personaje_2)


