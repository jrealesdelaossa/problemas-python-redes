"""
Pedir al usuario que ingrese dos números y determinar si el primero es divisible
por el segundo.
"""


def determinar_divisibilidad(dividendo, divisor):
    if dividendo % divisor == 0:
        print(f'El número {dividendo} es divisible por {divisor}')
    else:
        print(f'El número {dividendo} no es divisible por {divisor}')


# Ingreso de datos
numero1 = float(input("Ingrese el dividendo número: "))
numero2 = float(input("Ingrese el divisor número: "))

determinar_divisibilidad(numero1, numero2)
