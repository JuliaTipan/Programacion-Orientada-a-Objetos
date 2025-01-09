# Programa para convertir grados Celsius a Fahrenheit
# Desarrollado para demostrar el uso de tipos de datos, identificadores y convenciones en Python

# Definición de una función para la conversión de temperatura
def convertir_celsius_a_fahrenheit(celsius: float) -> float:
    """Convierte grados Celsius a Fahrenheit.
    celsius: temperatura en grados Celsius (tipo float)
    return: temperatura convertida a Fahrenheit (tipo float)
    """
    return (celsius * 9/5) + 32

# Entrada de datos proporcionada por el usuario
temperatura_celsius = float(input("Ingrese la temperatura en grados Celsius: "))

# Conversión de la temperatura usando la función definida anteriormente
temperatura_fahrenheit = convertir_celsius_a_fahrenheit(temperatura_celsius)

# Salida del resultado formateado con dos decimales
print(f"La temperatura en Fahrenheit es: {temperatura_fahrenheit:.2f} °F")

# Validación adicional para determinar si la temperatura es alta
# Se considera alta si supera los 100 grados Fahrenheit
es_temperatura_alta = temperatura_fahrenheit > 100
print(f"¿La temperatura es alta? {es_temperatura_alta}")

# Explicación de identificadores:
# - convertir_celsius_a_fahrenheit: función que realiza la conversión de temperatura.
# - celsius: argumento de la función, representa la temperatura en grados Celsius.
# - temperatura_celsius: variable que almacena la entrada del usuario.
# - temperatura_fahrenheit: variable que almacena el resultado de la conversión.
# - es_temperatura_alta: variable booleana que indica si la temperatura es alta o no.