"""
Generar todos los números primos en un rango dado ingresado por el usuario.

Se hace uso de la solución al problema del ejercicio26.py
"""


def es_primo(numero):
    if numero < 2:
        return False
    elif numero == 2:
        return True
    elif numero > 2 and numero % 2 == 0:
        return False
    else:
        for i in range(3, numero):
            if numero % i == 0:
                return False

    return True


# Ingreso de datos
numero = int(input("Ingrese un número: "))

for i in range(numero+1):
    if es_primo(i):
        print('El número {} es primo'.format(i))
