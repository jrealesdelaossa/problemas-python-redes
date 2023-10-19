"""
Solicitar al usuario que ingrese una cadena y determinar si es un palindrome (se lee
igual de izquierda a derecha que de derecha a izquierda).
"""


def validar_palindrome(cadena):
    if cadena == cadena[::-1]:
        print(f'La cadena {cadena} es palindrome')
    else:
        print(f'La cadena {cadena} no es palindrome')


# Ingreso de datos
cadena = input("Ingrese una cadena: ")

validar_palindrome(cadena)
