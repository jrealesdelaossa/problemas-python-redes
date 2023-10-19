"""
Pedir al usuario que ingrese un número entero y calcular la suma de sus dígitos.
"""


def suma_digitos(cadena):
    lista_digitos = list(map(int, cadena))
    return sum(lista_digitos)


# Ingreso de datos
cadena = input("Ingrese un número: ")

suma = suma_digitos(cadena)

print(f'La suma de los dígitos de {cadena} es {suma}')
