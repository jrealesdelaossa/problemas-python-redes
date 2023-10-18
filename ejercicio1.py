"""
Solicita al usuario que ingrese su nombre y luego imprimir un mensaje de saludo
con su nombre.
"""


def saludar(nombre):
    print(f'Hola {nombre}!')


# Ingreso de datos
nombre = input("Ingrese su nombre: ")

saludar(nombre)
