"""
Implementar un juego de adivinanza en el que el programa genera un número
aleatorio y el usuario tiene un número limitado de intentos para adivinarlo.

Se hace uso de la solución al problema del ejercicio9.py
"""

import random

numero_aleatorio = random.randint(1, 100)

intentos = 10
while True:
    print("Intentos restantes: {}".format(intentos))
    numero = int(input("Ingrese un número: "))

    if numero == numero_aleatorio:
        print("Adivinaste!")
        break
    elif numero > numero_aleatorio:
        print("El número ingresado es mayor al número a adivinar")
    elif numero < numero_aleatorio:
        print("El número ingresado es menor al número a adivinar")

    intentos -= 1
    if intentos == 0:
        print("Perdiste!")
        break
