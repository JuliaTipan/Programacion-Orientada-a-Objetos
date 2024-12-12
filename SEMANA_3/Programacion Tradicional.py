# Función para ingresar las temperaturas diarias
def ingresar_temperaturas():
    temperaturas = []
    print("Ingresa las temperaturas en grados Celsius para los próximos 7 días:")
    for dia in range(1, 8):
        temp = float(input(f"Temperatura del día {dia}: "))
        temperaturas.append(temp)
    return temperaturas

# Función para calcular el promedio de las temperaturas
def calcular_promedio(temperaturas):
    total = sum(temperaturas)
    return total / len(temperaturas)

# Programa principal
def main():
    print("Bienvenido al programa de cálculo del promedio semanal de temperaturas.\n")
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)
    print(f"\nEl promedio de las temperaturas de la semana es: {promedio:.2f} °C")

# Ejecutar el programa
if __name__ == "__main__":
    main()


