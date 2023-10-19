"""
Pedir al usuario que ingrese un número y determinar si es primo o no.
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

if es_primo(numero):
    print(f'El número {numero} es primo')
else:
    print(f'El número {numero} no es primo')
