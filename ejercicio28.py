"""
Usar un bucle for para mostrar la tabla de multiplicar de un número ingresado por el
usuario.
"""


def mostrar_tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f'{numero} x {i} = {numero * i}')


# Ingreso de datos

numero = int(input("Ingrese un número: "))

mostrar_tabla_multiplicar(numero)
