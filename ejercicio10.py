"""
Convertir una cantidad de dólares ingresadas por el usuario a euros utilizando una 
tasa de cambio específica.
"""


def convertir_dolares_a_euros(dolares):
    tasa_de_cambio = 0.95
    euros = dolares * tasa_de_cambio
    print(f'${dolares} dólares son {euros} euros')


# Ingreso de datos
print("Convertir de dólares a euros a una tasa de 0.95")
dolares = float(input("Ingrese la cantidad de dólares a convertir: "))

convertir_dolares_a_euros(dolares)
