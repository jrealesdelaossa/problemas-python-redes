"""
Pedir al usuario que ingrese su peso y altura, y calcular su índice de masa corporal
(IMC) utilizando la fórmula: IMC = peso (kg) / (altura^2) (m^2).
"""


def indice_de_masa_corporal(peso, altura):
    indice = peso / (altura ** 2)
    print(f'Su índice de masa corporal es: {indice:.2f}')


# Ingreso de datos
peso = float(input("Ingrese su peso (kg): "))
altura = float(input("Ingrese su altura (m): "))

indice_de_masa_corporal(peso, altura)
