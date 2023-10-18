"""
Calcular el factorial de un número ingresado por el usuario.
"""


def factorial(numero):
    for i in range(1, numero):
        numero *= i

    print(f'El factorial del número ingresado es: {numero}')


# Ingreso de datos
numero = int(input("Ingrese un número: "))

factorial(numero)
