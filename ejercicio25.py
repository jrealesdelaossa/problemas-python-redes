"""
Utilizar un bucle while para calcular el factorial de un número ingresado por el
usuario.

Resuelto en el ejercicio8.py
"""


def factorial(numero):
    for i in range(1, numero):
        numero *= i

    print(f'El factorial del número ingresado es: {numero}')


# Ingreso de datos
numero = int(input("Ingrese un número: "))

factorial(numero)
