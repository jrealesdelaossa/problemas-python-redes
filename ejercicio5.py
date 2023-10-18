"""
Solicitar al usuario que ingrese tres números y calcular el promedio de esos números.
"""


def calcular_promedio(numero1, numero2, numero3):
    promedio = (numero1 + numero2 + numero3) / 3
    print(f'El promedio de los números ingresados es: {promedio}')


numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
numero3 = float(input("Ingrese el tercer número: "))

calcular_promedio(numero1, numero2, numero3)
