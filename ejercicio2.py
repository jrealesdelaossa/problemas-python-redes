"""
Pedir al usuario que ingrese la base y la altura de un triángulo, luego calcular y mostrar
su área.
"""


def calcular_area(base, altura):
    area = (base * altura) / 2
    print(f'El área del triángulo es: {area}')


# Ingreso de datos
base = float(input("Ingrese la base: "))
altura = float(input("Ingrese la altura: "))

calcular_area(base, altura)
