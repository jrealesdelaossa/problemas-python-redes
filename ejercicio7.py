"""
Pedir al usuario que ingrese un número y determinar si es par o impar
"""


def es_par_o_impar(numero):
    if (numero % 2 == 0):
        print(f'El número {numero} es par')
    elif (numero % 2 != 0):
        print(f'El número {numero} es impar')
    else:
        print(f'El número {numero} no es par ni impar')


# Ingreso de datos
numero = int(input("Ingrese un número: "))


es_par_o_impar(numero)
