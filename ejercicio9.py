"""
Generar un número aleatorio entre 1 y 100 y pedir al usuario que adivine el número.
"""

import random

numero_aleatorio = random.randint(1, 100)

while True:
    numero = int(input("Ingrese un número: "))

    if numero == numero_aleatorio:
        print("Adivinaste!")
        break
    elif numero > numero_aleatorio:
        print("El número ingresado es mayor al número a adivinar")
    elif numero < numero_aleatorio:
        print("El número ingresado es menor al número a adivinar")
