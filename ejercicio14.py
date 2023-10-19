"""
Solicitar tres longitudes y determinar si pueden formar un triángulo equilátero,
isósceles o escaleno.
"""


def tipo_de_triangulo(lado1, lado2, lado3):
    if lado1 == lado2 and lado2 == lado3:
        print("El triángulo es equilátero")
    elif lado1 != lado2 and lado2 != lado3 and lado1 != lado3:
        print("El triángulo es escaleno")
    else:
        print("El triángulo es isósceles")


# Ingreso de datos
lado1 = float(input("Ingrese el primer lado: "))
lado2 = float(input("Ingrese el segundo lado: "))
lado3 = float(input("Ingrese el segundo lado: "))

tipo_de_triangulo(lado1, lado2, lado3)
