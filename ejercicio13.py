"""
Pedir al usuario que ingrese un año y determinar si es un año bisiesto o no.
"""


def determinar_bisiesto(anno):
    if (anno % 4 == 0 and anno % 100 != 0) or anno % 400 == 0:
        print(f'El año {anno} es bisiesto')
    else:
        print(f'El año {anno}, no es bisiesto')


# Ingreso de datos
anno = int(input("Ingrese un año: "))

determinar_bisiesto(anno)
