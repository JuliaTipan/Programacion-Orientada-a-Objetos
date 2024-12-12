# Promedio semanal del clima (Programación Orientada a Objetos)

class Clima:
 #Clase de abtraccion que define los atributos comunes para el clima.
    def __init__(self):
        # Lista privada para encapsular las temperaturas
        self.__temperaturas = []

    def ingresar_temperaturas(self):
        #Solicita al usuario ingresar las temperaturas para 7 días.
        print("Ingresa las temperaturas en grados Celsius para los próximos 7 días:")
        for dia in range(1, 8):
            temp = float(input(f"Temperatura del día {dia}: "))
            self.__temperaturas.append(temp)

    def obtener_temperaturas(self):
        #Metodo protegido para obtener las temperaturas (encapsulamiento).
        return self.__temperaturas


class ClimaPromedio(Clima):
    #Clase que hereda de ClimaBase y añade funcionalidad para calcular el promedio.
    def calcular_promedio(self):
        #Calcula el promedio de las temperaturas.
        temperaturas = self.obtener_temperaturas()
        if not temperaturas:
            print("Error: No se han ingresado temperaturas.")
            return 0
        return sum(temperaturas) / len(temperaturas)


# Clase polimorfismo para otro tipo de cálculo (por ejemplo, máximo y mínimo)
class ClimaExtremos(Clima):
    #Clase que hereda de ClimaBase y permite calcular extremos (máximo y mínimo).

    def calcular_extremos(self):
        #Devuelve el valor máximo y mínimo de las temperaturas.

        temperaturas = self.obtener_temperaturas()
        if not temperaturas:
            print("Error: No se han ingresado temperaturas.")
            return None, None
        return max(temperaturas), min(temperaturas)


# Programa principal
def main():
# Programa principal que demuestra encapsulamiento, herencia y polimorfismo.
    print("Bienvenido al programa de cálculo del promedio y extremos del clima.\n")

    # Crear una sola instancia para ingresar las temperaturas
    clima = Clima()
    clima.ingresar_temperaturas()

    # Utilizar la misma instancia para calcular el promedio
    clima_promedio = ClimaPromedio()
    clima_promedio._Clima__temperaturas = clima.obtener_temperaturas()  # Compartir temperaturas
    promedio = clima_promedio.calcular_promedio()
    print(f"\nEl promedio de las temperaturas de la semana es: {promedio:.2f} °C")

    # Utilizar la misma instancia para calcular extremos
    clima_extremos = ClimaExtremos()
    clima_extremos._Clima__temperaturas = clima.obtener_temperaturas()  # Compartir temperaturas
    max_temp, min_temp = clima_extremos.calcular_extremos()
    print(f"La temperatura máxima es: {max_temp:.2f} °C")
    print(f"La temperatura mínima es: {min_temp:.2f} °C")

# Ejecutar el programa
if __name__ == "__main__":
    main()
