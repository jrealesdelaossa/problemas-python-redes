"""
Solicita al usuario que ingrese un número y determinar si es positivo, negativo o cero.
"""


def determinar_signo(numero):
    if numero > 0:
        print(f'El número {numero} es positivo')
    elif numero < 0:
        print(f'El número {numero} es negativo')
    else:
        print(f'El número {numero} es cero')


# Ingreso de datos
numero = float(input("Ingrese un número: "))

determinar_signo(numero)
