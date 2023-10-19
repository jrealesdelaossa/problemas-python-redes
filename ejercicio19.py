"""
Solicitar una calificación numérica y convertirla a una letra (A, B, C, D o F) según
una escala predefinida.
"""


def convertir_nota(nota):
    if (nota >= 90 and nota <= 100):
        return 'A'
    elif (nota >= 80 and nota <= 89):
        return 'B'
    elif (nota >= 70 and nota <= 79):
        return 'C'
    elif (nota >= 60 and nota <= 69):
        return 'D'
    elif (nota >= 0 and nota <= 59):
        return 'F'


# Ingreso de datos
nota = int(input("Ingrese una nota: "))

nota_convertida = convertir_nota(nota)

print(f'La nota {nota} es {nota_convertida}')
