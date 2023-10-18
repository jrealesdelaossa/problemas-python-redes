"""
Solicitar la temperatura en grados Celsius al usuario y convertirla a grados Fahrenheit.
"""


def convertir_celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    print(f'{celsius}°C = {fahrenheit}°F')


# Ingreso de datos
grados_celsius = float(input("Ingrese la temperatura en grados Celsius: "))

convertir_celsius_a_fahrenheit(grados_celsius)
